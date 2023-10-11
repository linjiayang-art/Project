from flask.views import MethodView
from flask import jsonify, request, current_app
from backend.apis.v1 import api_v1
from backend.models.system import UserInfo
from sqlalchemy import select
from backend.core.extensions import db,csrf
from backend.apis.auth.auth import generate_token
from flask_wtf.csrf import generate_csrf


class IndexAPI(MethodView):

    def get(self):
        return jsonify({
            "api_version": "1.0",
            "api_base_url": "http://example.com/api/v1",

        })


class TokenAPI(MethodView):
    decorators=[csrf.exempt]
    def post(self):
        data = request.get_json()
        data=dict(data)
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
        token,expiration=token_data[0],token_data[1]
        csrf_token = generate_csrf(current_app.config['SECRET_KEY'])
        data = {
            'access_token': token,
            'status_text': expiration,
            'csrf_token': csrf_token
        }
        return jsonify(code=200, msg='登录成功', data=data)


api_v1.add_url_rule('/', view_func=IndexAPI.as_view('index'), methods=['GET'])

api_v1.add_url_rule('/login',view_func=TokenAPI.as_view('token'),methods=['POST'])