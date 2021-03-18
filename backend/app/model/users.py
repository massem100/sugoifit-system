# from . import user
from app import db
from werkzeug.security import generate_password_hash
from datetime import date
from flask_login._compat import unicode
from datetime import datetime
# from flask_login import UserMixin
# from sqlalchemy import Column, DECIMAL, Date, DateTime, Enum, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

Base = db.declarative_base()
metadata = Base.metadata


class User(UserMixin, Base, db.Model):
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
        
       
        
    def test(self, set):
        return set

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User "{}">'.format(self.id)
    
# class Owner(User, UserMixin): 

#     def __init__(self, id, role, username):
#         self.id = id
#         self.username = username
#         self.role = role


# class Employee(User):
#     def __init__(self, id, hireDate):
#         self.id = id
#         self.hireDate = hireDate


# if __name__ == '__main__':    
#     Pat = User('0019', 'Patty', 'Pat', 'Lazarus', 'female' )
#     Bob = Owner('high','bob')
#     print (Bob)
#     print (Pat)
#     result = Bob.test('child working')
#     print (result)

#     result = Pat.test('parent working')
#     print (result)
#     print (Bob.is_authenticated)