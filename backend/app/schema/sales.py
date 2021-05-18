from app import ma
from app.model.sales import Product
from marshmallow import Schema, fields, ValidationError, pre_load


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")

class BusinessSchema(Schema):
    busID = fields.String()

class CustomerSchema(Schema):
    custID = fields.String()
    fname = fields.String()
    lname = fields.String()
    trn = fields.Float()
    email = fields.String()
    address = fields.String()

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

class InvoiceSchema(Schema):
    invoiceID = fields.String()
    custID = fields.Nested(CustomerSchema, validate=must_not_be_blank)
    busID = fields.Nested(BusinessSchema, validate=must_not_be_blank)
    invoice_DATE = fields.DateTime(dump_only=True)
    tax_tot = fields.Float()

class OrderSchema(Schema):
    orderID = fields.String()
    order_tot = fields.Float()
    order_DATE = fields.DateTime(dump_only=True)

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
invoices_schema = InvoiceSchema(many=True)
customer_schema = CustomerSchema()
order_schema = OrderSchema()