from backend.core.extensions import db
from flask_login import UserMixin
from sqlalchemy import Column,String,Integer,Text,Boolean, DateTime,BigInteger
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class BasicMode():
    create_user=Column(String(255))
    create_date=Column(DateTime,default=datetime.utcnow)
    last_modification_time=Column(DateTime)
    is_deleted=Column(Boolean,default=False)

class UserInfo(db.Model,UserMixin,BasicMode):
    __tablename__='user_info'
    id=Column(Integer,primary_key=True)
    userno=Column(String(255))
    username=Column(String(255))
    password_hash = Column(String(128))
    email=Column(String(255))
    

    def __str__(self) -> str:
        return self.email

    @property
    def password(self):
        raise AttributeError('Write-only property!')

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

class Menu(db.Model,BasicMode):
    __tablename__ = 'sys_menu'
    id = Column(BigInteger, primary_key=True)
    parent_id = Column(BigInteger)
    menu_path = Column(String(80))
    component = Column(String(80))
    redirect_url = Column(String(80))
    menu_name = Column(String(80))  # title
    menu_icon = Column(String(80))
    menu_type = Column(String(80))
    menu_visible = Column(Boolean, default=True)
    menu_perm = Column(String(80))
    menu_sort = Column(BigInteger)


class SYSRole(db.Model,BasicMode):
    __tablename__='sys_role'
    id = Column(Integer, primary_key=True)
    rolename =Column(String(50))
    code = Column(String(50))
    sort = Column(String(50))
    rolestatus = Column(String(50))

class SysRoleMenu(db.Model,BasicMode):
    __tablename__ = 'sys_role_menu'
    id = Column(BigInteger, primary_key=True)
    # relationship
    role_id = Column(BigInteger)
    menu_id = Column(BigInteger)

class SysUserRole(db.Model,BasicMode):
    __tablename__ = 'sys_user_role'
    id = Column(BigInteger, primary_key=True)
    # relationship
    user_id = Column(BigInteger)
    role_id = Column(BigInteger)


