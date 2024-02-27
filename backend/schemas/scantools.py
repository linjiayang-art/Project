from marshmallow import Schema, fields, ValidationError, pre_load


class CustomerInfoSchema(Schema):
    agent = fields.String(required=True)
    chipNo = fields.String(required=True)
    createData = fields.String(required=True)
    createUser = fields.String(required=True)
    customerNo = fields.String(required=True)
    id = fields.String(required=True)
    isDeleted = fields.String(required=True)
