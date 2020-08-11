from typing import ValuesView
from marshmallow import Schema, fields

class ProductSchema(Schema):
    name = fields.Str()
    value = fields.Float()
    discount_value = fields.Float()
    stock = fields.Int()