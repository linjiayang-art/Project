from marshmallow import Schema, fields, ValidationError, pre_load


class CustomerInfoSchema(Schema):
    agent = fields.String(required=True)
    chipNo = fields.String(required=True)
    createData = fields.String(required=True)
    createUser = fields.String(required=True)
    customerNo = fields.String(required=True)
    id = fields.String(required=True)
    isDeleted = fields.String(required=True)


class CheckResultSchema(Schema):
    check_data = fields.String(required=True)
    checktype = fields.String(required=True)
    create_data = fields.String(required=True)
    id = fields.String(required=True)
    isdeleted = fields.String(required=True)
    lotno = fields.String(required=True)
    producttype = fields.String(required=True)
    tape_num = fields.String(required=True)
    unit_qty = fields.String(required=True)
