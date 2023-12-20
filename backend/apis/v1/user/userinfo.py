from backend.apis.v1 import api_v1
from flask.views import MethodView
from flask import jsonify, current_app, request
from backend.models.system import UserInfo, Menu
from sqlalchemy import select, Result, Tuple
from backend.core.extensions import db
from sqlalchemy.orm import class_mapper
from backend.apis.auth.auth import auth_required
from backend.factorys.requersfactorys  import query_factory

class UserInfosAPI(MethodView):
    decorators=[auth_required]
    def get(self):
        page=request.args.get('page',1,type=int)
        users=select(UserInfo).filter_by(isdeleted=0)
        user_results=db.paginate(

        )


class UserAPI(MethodView):
    #decorators = [auth_required]

    def get(self):
        results=query_factory(UserInfo,request=request)
        return jsonify(code=200,msg='ok',data=results)
        page = request.args.get('page', 1, type=int)

        per_page = current_app.config['BACKEND_POST_PER_PAGE']

        pagination = db.paginate(
            select(UserInfo).order_by(UserInfo.id.desc()),
            page=page,
            per_page=per_page,
        )
        result = []
        for u in pagination.items:
            result.append(u.to_dict())
        return jsonify(code=200, msg='ok', data=result)





api_v1.add_url_rule('userinfo', view_func=UserAPI.as_view(
    'userinfo'), methods=['GET'])

