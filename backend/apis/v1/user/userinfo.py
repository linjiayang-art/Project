from backend.apis.v1 import api_v1
from flask.views import MethodView
from flask import jsonify
from backend.models.system import UserInfo
from sqlalchemy import select

class UserApi(MethodView):

    decorators=[]
    def get(self):
        return jsonify(code=200,msg='ok',data='ok')
    

api_v1.add_url_rule('userinfo',view_func=UserApi.as_view('userinfo'),methods=['GET'])