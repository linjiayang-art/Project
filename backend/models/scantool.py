from backend.core.extensions import db
#from flask_login import UserMixin
from sqlalchemy import Column,String,Integer,Text,Boolean, DateTime,BigInteger
from datetime import datetime
from backend.models.system import BasicMode

class CustomerInfo(db.Model,BasicMode):
    __tablename__ = 'customerinfo'
    id=Column(Integer,primary_key=True)
    customerNo =Column(String(255))
    chipNo = Column(String(255))
    agent = Column(String(255))
    createData = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    createUser =Column(String(255))
    isDeleted = Column(String(255))


class CheckLot(db.Model,BasicMode):
    __tablename__ = 'checklot'
    id=Column(Integer,primary_key=True)
    checktype = Column(String(255))
    lotno = Column(String(255))
    producttype = Column(String(255))
    tape_num = Column(Integer, default=1)
    unit_qty = Column(Integer)
    check_data = Column(Text)
    create_data = Column(DateTime, default=datetime.utcnow, index=True)
    isdeleted = Column(Boolean, default=False)
