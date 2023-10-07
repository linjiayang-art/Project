from backend.core.extensions import db
from flask_login import UserMixin
from sqlalchemy import Column,String,Integer,Text,Boolean, DateTime

from werkzeug.security import generate_password_hash, check_password_hash

class UserInfo(db.Model,UserMixin):
    id=Column(Integer,primary_key=True)
    userno=Column(String(255))
    username=Column(String(255))
    password = Column(String(128))
    
    @property
    def password(self):
        raise AttributeError('Write-only property!')

    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password, password)