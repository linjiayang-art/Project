from marshmallow import Schema, fields, ValidationError, pre_load


class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

class UserInfoSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    id=fields.String(required=True)
    userno=fields.String(required=True)
    username=fields.String(required=True)
    password_hash = fields.String(required=True)
    email=fields.String(required=True)