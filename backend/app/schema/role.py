from app import ma
from app.model.sales import Product
from marshmallow import Schema, fields, ValidationError, pre_load

class RoleSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("userID", "role_name")

class UserSchema(Schema):
    userID = fields.String()
    fname = fields.String()
    lname = fields.String()
    

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)
users_schema = UserSchema(many=True)