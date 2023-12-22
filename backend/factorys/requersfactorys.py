from flask import request,jsonify,Request
from backend.core.extensions import db
from flask_sqlalchemy.model import Model
from sqlalchemy import select,insert
import typing as t
from backend.models.system import UserInfo,Menu

model_dict={
        'USERINFO':UserInfo,
        'MENU':Menu
    }

def query_factory_list(
        query_model:str|None,
        request:t.Optional[Request]|None
    )->list:

    orm_model=model_dict.get(query_model,None)

    if  orm_model is None:
        return []
    
    # 获取表的所有列对象
    columns =orm_model.__table__.c
    columns_list = [ column.name for column in columns]
    query=select(orm_model)
    for param_name, param_value in request.args.items():
        if param_name in columns_list:
            column_attr = getattr(orm_model, param_name)
            query = query.filter(column_attr.like(f'%{param_value}%'))
    results=[]
    result=db.paginate(
        query,
        page=request.args.get('page',1,type=int),
        per_page=request.args.get('per_page',10,type=int)
    )
    for i in result.items:
        results.append(i.to_dict())
    return results

def query_factory_item(
        query_model:str|None,
        id:int|None
    )->dict:
    orm_model=model_dict.get(query_model,None)
    if  orm_model is None:
        return {}
    result=db.session.execute(select(orm_model).filter_by(id=id,is_deleted=0)).scalar()
    if result is None:
        return {}
    result=result.to_dict()
    return result
