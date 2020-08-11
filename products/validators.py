from marshmallow import ValidationError, validates_schema


def validate_name(name):
    if len(name) < 3 or len(name) > 55:
        raise ValidationError("Invalid product name")

def validate_value(value):
    if value <=0 or value > 9999.9:
        raise ValidationError("Invalid value")

def validate_stock(stock):
    if stock <= -1:
        raise ValidationError("Invalid stock value")
