from app import db
from werkzeug.security import generate_password_hash
from datetime import date
from flask_login._compat import unicode
from datetime import datetime
from flask_login import UserMixin


class User(UserMixin,db.Model):
    __tablename__ = 'user'

    userID = db.Column(db.String(5), primary_key=True, unique=True)
    fname = db.Column(db.String(25))
    lname = db.Column(db.String(25))
    user_address = db.Column(db.String(50))
    phone = db.Column(db.String(10))  

    def __init__(self,id, f_name, l_name, user_address, phone):
        self.id= id
        self.f_name = f_name
        self.l_name = l_name
        self.user_address = user_address
        self.phone = phone
        
       
        
    def test(set):
        return set

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User "{}">'.format(self.id)

