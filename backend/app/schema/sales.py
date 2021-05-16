from app import ma
from app.model.sales import Product
from marshmallow import Schema, fields, ValidationError, pre_load


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")

class BusinessSchema(Schema):
    busID = fields.String()


class ProductSchema(Schema):
    prodID = fields.String()
    busID = fields.Nested(BusinessSchema, validate=must_not_be_blank)
    prodName = fields.String()
    unit_price = fields.Float()
    Unit = fields.Float()
    limitedTime = fields.DateTime(dump_only=True)
    taxPercent = fields.Float()
    prodStatus = fields.String()
    image = fields.String()

# class ServiceSchema(Schema):
#     prodID = fields.String()
#     busID = fields.Nested(BusinessSchema, validate=must_not_be_blank)
#     prodName = fields.String()
#     unit_price = fields.Float()
#     Unit = fields.Float()
#     limitedTime = fields.DateTime(dump_only=True)
#     taxPercent = fields.Float()
#     prodStatus = fields.String()
#     image = fields.String()


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
business_schema = BusinessSchema()    