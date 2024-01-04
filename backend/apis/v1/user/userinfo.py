from backend.apis.v1 import api_v1
from flask.views import MethodView
from flask import jsonify, current_app, request
from backend.models.system import UserInfo, Menu
from sqlalchemy import select, Result, Tuple
from backend.core.extensions import db
from sqlalchemy.orm import class_mapper
from backend.apis.auth.auth import auth_required
from backend.factorys.requersfactorys  import query_factory_item,query_factory_list 

from backend.schemas.userschemas import UserInfoSchema


class UserInfoAPI(MethodView):
    #decorators=[auth_required]
    def get(self,id):
        if id is None:
            return jsonify(code=404,msg='未获取到数据明细')
        userschema= UserInfoSchema()
        user =db.session.execute(select(UserInfo).filter_by(is_deleted=False,id=id)).scalar()
        result=userschema.dump(user)
        #result=query_factory_item('USERINFO',id)
        return jsonify(code=200,msg='ok',data=result)


class UserInfoSAPI(MethodView):
    decorators = [auth_required]
    def get(self):
        results=query_factory_list('USERINFO',request=request)
        return jsonify(code=200,msg='ok',data=results)
  


class TestUserScalar(MethodView):
    def get(self):
        userschema= UserInfoSchema()
        user =db.session.execute(select(UserInfo).filter_by(userno='admin', is_deleted=False)).scalar()
        result=userschema.dump(user)
        result=userschema.dump(user)
        return {"messasg":"test","user":result}

api_v1.add_url_rule('userinfo/<int:id>', view_func=UserInfoAPI.as_view('userinfo'), methods=['GET'])

api_v1.add_url_rule('userinfo', view_func=UserInfoSAPI.as_view('userinfos'), methods=['GET'])

api_v1.add_url_rule('testuser', view_func=TestUserScalar.as_view('testuser'), methods=['GET'])
