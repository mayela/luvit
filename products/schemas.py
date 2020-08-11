from marshmallow import Schema, fields

from .validators import validate_name, validate_value, validate_stock


class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(validate=validate_name)
    value = fields.Float(validate=validate_value)
    discount_value = fields.Float()
    stock = fields.Int(validate=validate_stock)
