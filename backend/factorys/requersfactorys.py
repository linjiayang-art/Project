from flask import request,jsonify
from backend.core.extensions import db
from flask_sqlalchemy.model import Model
from sqlalchemy import select
import typing as t

def query_factory(query_model:t.Optional[Model],request=None  )->list:
    
    results=[]
    query_model=select(query_model)
    result=db.paginate(
        query_model,
        page=request.args.get('page',1,type=int),
        per_page=request.args.get('per_page',10,type=int)
    )
    for i in result.items:
        results.append(i.to_dict())
    return results