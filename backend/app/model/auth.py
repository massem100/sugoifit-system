from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
import enum 
from datetime import datetime

class Busines(db.Model, UserMixin):
    __tablename__ = 'business'

    busID = db.Column(db.String(100), primary_key=True, unique=True)
    busName = db.Column(db.String(100))
    busemail = db.Column(db.String(255))
    busaddress = db.Column(db.String(100))
    telephone = db.Column(db.String(100))
    date_joined = db.Column(db.DateTime(), nullable= False)
    employees = db.relationship('UserCredential', backref='business')
    
    

    def ___init__(self, busID, busName, date_joined, busemail = None, busaddress= None, telephone= None):
        self.busID = busID
        self.busName = busName
        self.date_joined = date_joined 
        self.busemail = busemail
        self.busaddress = busaddress
        self.telephone = telephone

    def get_id(self):
        try:
            return unicode(self.busID)  # python 2 support
        except NameError:
            return str(self.busID)  # python 3 support

      # Represent the structure of the User object
    def __repr__(self): 
        return '<Business {}, {}>'.fomrat(self.busID, self.busName)



class User(db.Model, UserMixin):
    __tablename__ = 'user'

    userID = db.Column(db.String(100), primary_key=True, unique=True)
    fname = db.Column(db.String(25))
    lname = db.Column(db.String(25))
    user_address = db.Column(db.String(50))
    phone = db.Column(db.String(10))
    user_credentials = db.relationship('UserCredential', backref = 'user', uselist = False)
    date_joined = db.Column(db.DateTime())

    def __init__(self, userID, fname, lname, user_address, phone):  
        self.userID = userID
        self.fname = fname
        self.lname = lname
        self.user_address = user_address
        self.phone = phone 
        self.date_joined = datetime.now()

    #Implement a get user id function 
    def get_id(self):
        try:
            return unicode(self.userID)  # python 2 support
        except NameError:
            return str(self.userID)  # python 3 support

    # Represent the structure of the User object
    def __repr__(self): 
        name = self.fname + '' + self.lname
        return '<User {} ,{}}>'.format(self.userID, name)


# roles = db.Table('roles',db.Model.metadata,
#     db.Column('role_name', db.String(30), db.ForeignKey('role.role_name'), primary_key=True),
#     db.Column('userID', db.String(100), db.ForeignKey('usercredentials.userID'), primary_key=True)
# )

class UserCredential(db.Model, UserMixin):
    __tablename__ = 'usercredentials'

    cid = db.Column(db.Integer, primary_key= True, autoincrement = True)
    userID = db.Column(db.String(100), db.ForeignKey('user.userID'), nullable=False, unique = True)
    active = db.Column(db.Boolean, nullable=False, default=False )
    user_email = db.Column(db.String(50), unique=True)
    user_password = db.Column(db.String(255))
    busID = db.Column(db.String(200), db.ForeignKey('business.busID'))
    roles = db.relationship('Role', backref='usercredentials', lazy='dynamic')
    
    def __init__(self, userID, busID, user_email, user_password, active = False, cid = None):  
        self.cid = cid
        self.userID = userID
        self.busID = busID
        self.user_email = user_email
        self.user_password = generate_password_hash(user_password,method = 'pbkdf2:sha256')
        self.active = active

    def get_id(self):
        try:
            return unicode(self.cid)  # python 2 support
        except NameError:
            return str(self.cid)  # python 3 support

    def is_active(self):
        """Flask-Login: return True if the user is active."""
        return self.active
    def __repr__(self): 
        return "<User Credentials {} UserID:{}".format(self.cid, self.userID)

# class RoleType(enum.Enum): 
#   owner = 'Business Owner'
#   employee = 'Employee'
#   manager = 'Financial Manager'
  
class Role(db.Model, UserMixin):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.ForeignKey('usercredentials.userID'))
    role_name = db.Column(db.String(30), nullable =False)
   