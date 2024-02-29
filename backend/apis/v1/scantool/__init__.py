from flask import jsonify, request, g, make_response
from  backend.apis.v1 import api_v1
from flask.views import MethodView  # import MethodView Class


from backend.schemas.scantools import CustomerInfoSchema,CheckResultSchema
from backend.core.extensions import db,csrf
from backend.apis.auth.auth import auth_required
from backend.models.scantool import  CustomerInfo,CheckLot
# import pandas as pd

from sqlalchemy import select

class CustomerAPI(MethodView):
    #decorators=[auth_required]
    def get(self):
        chipNo=request.args.get('chipNo',None)
        customerNo=request.args.get('customerNo',None)
        agent=request.args.get('agent',None)
        custom=select(CustomerInfo)
        if chipNo is not None:
            custom=custom.filter(CustomerInfo.chipNo.like(f'%{chipNo}%') )
        if customerNo is  not None:
            custom=custom.filter(CustomerInfo.customerNo.like(f'%{customerNo}%') )
        if agent is  not None:
            custom=custom.filter(CustomerInfo.agent.like(f'%{agent}%') )
        custom=custom.filter_by(isDeleted=False)
        res=db.session.execute(custom).scalars()
        result=[]
        for i in res:
            customer=CustomerInfoSchema()
            cus=customer.dump(i)
            result.append(cus)
        return jsonify(code='200',msg='获取客户数据成功',data=result)
    def post(self):
        formdata:dict=request.get_json()
        agent,chipNo,customerNo=formdata.get('agent',None),formdata.get('chipNo',None),formdata.get('customerNo',None)
        # userinfo= g.current_user
        # userid=userinfo.userid
        userid='admin'
        cus=db.session.execute(select(CustomerInfo).filter_by(agent=agent,chipNo=chipNo,customerNo=customerNo)).scalar()
        if cus is not None and cus.isDeleted==False:
            return jsonify(code='201',msg='已存在相同数据',data='已存在相同数据')
        cus=CustomerInfo(agent=agent,chipNo=chipNo,customerNo=customerNo,createUser=userid)
        db.session.add(cus)
        db.session.commit()
        return jsonify(code='200',msg='新增成功',data='新增成功')
    def delete(self):
        id=request.args.get('id')
        cus=CustomerInfo.query.filter_by(id=id).first()
        if cus is None:
            return jsonify(code='201',msg='删除失败,未查询到改数据',data='删除失败')
        if cus.isDeleted==True:
            return jsonify(code='201',msg='删除失败,该数据已经删除',data='删除失败')
        cus.isDeleted=True
        db.session.commit()
        return jsonify(code='200',msg='删除成功',data=1)
    def put(self):
        chipNo=request.args.get('chipNo',None)
        customerNo=request.args.get('customerNo',None)
        agent=request.args.get('agent',None)
        id=request.args.get('id',None)
        cus=db.session.execute(select(CustomerInfo).filter_by(id=id)).scalar()
        if cus is None:
             return jsonify(code='201',msg='错误,未获取到改数据',data='新增成功')
        cus.chipNo=chipNo
        cus.agent=agent
        cus.customerNo=customerNo
        db.session.commit()

        return jsonify(code='200',msg='修改成功',data='修改成功')

class PackageCheckLot(MethodView):
    decorators=[csrf.exempt]
    def get(self):
        return jsonify(name='sadsaf',asdsa='sadad')
        pass
    def post(self):
        data=request.json
        try:
            if 'tableData' in data:
                package_lot=str(data['tableData']['package_lot'])
                tape_lot=str(data['tableData']['tape_lot'])
            else:
                package_lot=str(data['package_lot'])
                tape_lot=str(data['tape_lot'])
        except KeyError:
            return jsonify(code=201,msg='非法请求,公司系统,不要乱搞',data='erro')
       
        #load
        #加工卷盘
        tape_list=tape_lot.split(" ")
        if  tape_list.__len__()<2:
            return jsonify(code=201,msg='卷盘数据不全,请检查',data='erro')
        tape_s_type,tape_s_lot=tape_list[0],tape_list[1]
        #加工下,万一有P就给他抹掉

        #加工铝箔袋,先申明下变量
        customer=''
        package_s_type=''
        package_s_lot=''
        qty=0
        package_list=package_lot.split(" ")
        if  package_list.__len__()<5:
            return jsonify(code=201,msg='包装数据不全,请检查',data='erro')
        for i in package_list:
            if tape_s_type in i:
                package_s_type=i
            if tape_s_lot in i:
                package_s_lot=i
            if str(i[0:1])=='Q':
                i=i[1::]
            try:
                i=int(i)
                if isinstance(i,int) and i<2000:
                    qty=i
            except ValueError:
                pass
        #客户编码就默认第一行吧
        customer=package_list[0]
        #拿到之后就判断下带P这些情况华为默认P ,1P,1T
        if customer[0:1]=='P':
            customer=customer[1::]
        if package_s_type[0:2]=='1P':
            package_s_type=package_s_type[2::]
        if package_s_lot[0:2]=='1T':
            package_s_lot=package_s_lot[2::]
        if tape_s_lot not in package_s_lot:
            return jsonify(code=201,msg='批号不一致,请检查',data='erro')
        if tape_s_type not in package_s_type:
            return jsonify(code=201,msg='产品型号不一致,请检查',data='erro')

        cus = CustomerInfo.query.filter_by(customerNo=customer,isDeleted=0,chipNo=tape_s_type).first()
        if cus is None:
            return jsonify(code=201,msg='客户代码:%s,产品型号:%s 未维护'%(customer,tape_s_type),data='erro')

        check_data=tape_lot+';'+package_lot
        ckecklot=CheckLot(checktype='包装比对',lotno= tape_s_lot,producttype=tape_s_type,unit_qty=qty,check_data=check_data)
        db.session.add(ckecklot)
        db.session.commit()
        return jsonify(code='200',msg='比对成功',data='success',statusText='比对成功')
        pass

class PackageCheckBox(MethodView):
    decorators=[csrf.exempt]
    def post(self):
        data=request.json
        try:
            if 'tableData' in data:
                package_lot=str(data['tableData']['package_lot'])
                tape_lot=str(data['tableData']['tape_lot'])
            else:
                package_lot1=str(data['package_lot1'])
                box_lot1=str(data['box_lot1'])
                package_lot2=str(data['package_lot2'])
                box_lot2=str(data['box_lot2'])
                package_lot3=str(data['package_lot3'])
                box_lot3=str(data['box_lot3'])
                p_l=[package_lot1,package_lot2,package_lot3]
                b_l=[box_lot1,box_lot2,box_lot3]
        except KeyError:
            return jsonify(code=201,msg='非法请求,公司系统,不要乱搞',data='erro')
        #load
        qty=0
        for p,i in zip(p_l,b_l):
            if p!=i:
                p=str(p)
                i=str(i)
                return jsonify(code=201,msg='对不数据不一致,包装 %s,外箱%s'%(p,i) ,data='erro')
            package_list=p.split(" ")
            if package_list==['']:
                continue
            customer,package_s_lot,package_s_type=package_list[0],package_list[4],package_list[1]

            #now data
            #如果有P则走这个，否则走正常
            if package_s_type[0:2]=='1P' and customer[0:1] =='P':
                tape_s_type=package_s_type[2::]
                customer=customer[1::]
                tape_s_lot=package_s_lot[2:7]
            else:
                tape_s_type=package_s_type
                customer=customer
                tape_s_lot=package_s_lot
            cus = CustomerInfo.query.filter_by(customerNo=customer,isDeleted=0,chipNo=tape_s_type).first()
            if cus is None:
                tape_s_type=package_s_type
                customer=customer
                tape_s_lot=package_s_lot
                cus = CustomerInfo.query.filter_by(customerNo=customer,isDeleted=0,chipNo=tape_s_type).first()
                if cus is None:
                    return jsonify(code=201,msg='客户代码:%s,产品型号:%s 未维护'%(customer,tape_s_type),data='erro')
            _qty=package_list[2]
            try:
                unit_qty=int(_qty[1:])
            except:
                unit_qty=0
            qty+=unit_qty
        check_data=str(p_l+b_l)

        ckecklot=CheckLot(checktype='外箱对比',lotno= tape_s_lot,producttype=tape_s_type,unit_qty=qty,check_data=check_data)
        db.session.add(ckecklot)
        db.session.commit()
        return jsonify(code='200',msg='比对成功',data='success',statusText='比对成功')

class PackageResult(MethodView):
    #decorators=[auth_required]
    def get(self):
        producttype=request.args.get('producttype','')
        checktype=request.args.get('checktype','')
        lotno=request.args.get('lotno','')
        pages=int(request.args.get('pages',1))
        results=[]
        checklot=select(CheckLot)
        if  producttype != '':
            checklot=checklot.filter(CheckLot.producttype.like(f'%{producttype}%'))
        if  checktype != '':
            checklot=checklot.filter(CheckLot.checktype.like(f'%{checktype}%'))
        if  lotno != '':
            checklot=checklot.filter(CheckLot.lotno.like(f'%{lotno}%'))
        checklot= checklot.filter_by(isdeleted=False).order_by(CheckLot.id.desc())
        result=db.paginate(
        checklot,
        page=pages,
        error_out=False,
        per_page=15)
        checkresult=CheckResultSchema()
        for i in result:
            r=checkresult.dump(i)
            results.append(r)
        return jsonify(code='200',msg='获取数据成功',data=results)

api_v1.add_url_rule('/customer',view_func=CustomerAPI.as_view('customer'),methods=['GET','POST','PUT','DELETE'])
api_v1.add_url_rule('/packagechecklot',view_func=PackageCheckLot.as_view('packagechecklot'),methods=['GET','POST'])
api_v1.add_url_rule('/packagecheckbox',view_func=PackageCheckBox.as_view('packagecheckbox'),methods=['POST'])
api_v1.add_url_rule('/packageresult',view_func=PackageResult.as_view('packageresult'),methods=['GET'])