from flask.views import MethodView
from flask import jsonify, request, current_app, json
from backend.apis.v1 import api_v1
from backend.models.system import UserInfo, Menu
from sqlalchemy import select
from backend.core.extensions import db, csrf
from backend.apis.auth.auth import generate_token, auth_required
from flask_wtf.csrf import generate_csrf
from backend.forms.systemform import MenuFrom
from apispec import APISpec

# spec=APISpec(
#     title='my-project',
#     version='1.0.0',
#     openapi_version='3.0.2',
#     info=dict(description="A minimal gist API"),
# )

# spec.components.schema('User',schema=UserInfo)



class IndexAPI(MethodView):

    def get(self):
        return jsonify({
            "api_version": "1.0",
            "api_base_url": "http://example.com/api/v1",

        })

# with current_app.test_request_context():
#     spec.path(view='api_v1.index')
# print(dict(spec.to_dict()["paths"]["/api_v1.index"]))



class TokenAPI(MethodView):
    decorators = [csrf.exempt]

    def post(self):
        data = request.get_json()
        data = dict(data)
        userno = data.get('userno', None)
        password = data.get('password', None)
        if userno is None or password is None:
            return jsonify(code='401', msg='请完善表单后再提交')

        user = select(UserInfo).filter_by(userno=userno, is_deleted=False)
        user = db.session.execute(user).scalar()
        if user is None:
            return jsonify(code='401', msg='用户不存在,请检查用户编号是否正确')
        if user.validate_password(password=password) == False:
            return jsonify(code='401', msg='用户密码错误,请检查用户密码否正确')

        token_data = generate_token(user=user)
        token, expiration = token_data[0], token_data[1]
        csrf_token = generate_csrf(current_app.config['SECRET_KEY'])
        data = {
            'access_token':token,
            'status_text': expiration,
            'csrf_token': csrf_token
        }
        return jsonify(code=200, msg='登录成功', data=data)


class MenusAPI(MethodView):
    decorators = [auth_required]

    def generate_menu(self, menu_items: list, parent_id: int):
        result = []
        for p_m in menu_items:
            p_m = dict(p_m)
            if p_m['parent_id'] == parent_id:
                submenu = self.generate_menu(menu_items, p_m['id'])
                if submenu:
                    p_m['child'] = submenu
                result.append(p_m)
        return result

    def get(self):
        menu_orgin_list = []
        main_menus = db.session.execute(
            select(Menu).filter_by(is_deleted=0).order_by(Menu.id.asc())
        )
        for p_m in main_menus.scalars():
            menu_orgin_list.append(p_m.menu_dict)
        result = self.generate_menu(menu_orgin_list, 0)
        return jsonify(code=200, msg='ok', data=result)

    def post(self):
        form_data = MenuFrom()
        if form_data.validate_on_submit() == False:
            return jsonify(code=201, msg='请完善表单后在进行提交', data=None)
        menu_dict = {}
        for i in form_data:
            if i.data is not None:
                menu_dict[i.name] = i.data
        menu = Menu(**menu_dict)
        menu_check = db.session.execute(
            select(Menu).filter_by(**menu_dict)).scalar()
        if menu_check is not None:
            return jsonify(code=201, msg='已存在该条数据', data=None)
        db.session.add(menu)
        db.session.commit()
        return jsonify(code=200, msg='新增成功', data=None)


class MenuAPI(MethodView):
    decorators = [auth_required]
    def get(self,menu_id):
        pass


class RouterAPI(MethodView):
    def get(self):
        main_menus = db.session.execute(
            select(Menu).filter_by(isdeleted=0).order_by(Menu.id.asc())
        )
        menu_orgin_list = []
        for p_m in main_menus.scalars():
            print(p_m)
            menu_orgin_list.append(p_m)
        a= self.generate_menu(menu_orgin_list,0)
        return jsonify(code='200', msg='一切ok', data=a)
    def generate_menu( self,menu_items: list, parent_id: int):
        result = []
        for p_m in menu_items:
            router_dict=dict(p_m.router_dict)
            if int(p_m.parent_id) == parent_id:
                print(router_dict)
                submenu = self.generate_menu(menu_items,int(p_m.id))
                if submenu:
                    router_dict['children'] = submenu
                result.append(router_dict)
        return result
        
        """   #userinfo= g.current_user
        userinfo= g.current_user
        roleids=[]
        roleresult=SysUserRole.query.filter_by(user_id=userinfo.userid).all()
        for i in roleresult:
            roleids.append(i.role_id)
        if roleids==[]:
            roleids.append('3')
        main_menus = db.session.execute(
            select(Menu,Menu.id).join(SysRoleMenu,Menu.id==SysRoleMenu.menu_id).\
                filter(SysRoleMenu.role_id.in_(roleids),Menu.isdeleted==0).order_by(Menu.menu_sort.asc())
        ).all()
        menu_orgin_list = []
        for p_m in main_menus:
            menu_orgin_list.append(p_m[0])
        a= generate_menu(menu_orgin_list,0)
        return jsonify(code='200', msg='一切ok', data=a) """


api_v1.add_url_rule('/', view_func=IndexAPI.as_view('index'), methods=['GET'])

api_v1.add_url_rule(
    '/login', view_func=TokenAPI.as_view('token'), methods=['POST'])
api_v1.add_url_rule(
    '/menus', view_func=MenusAPI.as_view('menus'), methods=['GET', 'POST'])

api_v1.add_url_rule(
    '/menu/<int:menu_id>',view_func=MenuAPI.as_view('menu',methods=['GET','POST','PUT','DELETE'])
)