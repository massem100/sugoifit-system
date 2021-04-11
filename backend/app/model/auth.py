from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class Busines(db.Model):
    __tablename__ = 'business'

    busID = db.Column(db.String(100), primary_key=True, unique=True)
    busName = db.Column(db.String(100))
    busemail = db.Column(db.String(255))
    busaddress = db.Column(db.String(100))
    telephone = db.Column(db.String(100))
    employees = db.relationship('UserCredential', backref='business')
    date_added = db.Column(db.DateTime())

    def ___init__(self, busID, busName, busemail, telephone):
        self.busID = busID
        self.busName = busName 
        self.busemail = busemail
        self.telephone = telephone
        self.date_added = datetime.now()
  


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
    # def get_id(): 
    #   return 

    # Represent the structure of the User object
    def __repr__(self): 
      return '<User %r>' % (self.userID)

roles = db.Table('roles',
    db.Column('role_name', db.Integer, db.ForeignKey('role.role_name'), primary_key=True),
    db.Column('userID', db.Integer, db.ForeignKey('usercredentials.userID'), primary_key=True)
)

class UserCredential(db.Model):
    __tablename__ = 'usercredentials'

    cid = db.Column(db.Integer, primary_key= True, autoincrement = True)
    userID = db.Column(db.String(100), db.ForeignKey('user.userID'), primary_key=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=False )
    user_email = db.Column(db.String(50), unique=True)
    user_password = db.Column(db.String(255))
    busID = db.Column(db.String(200), db.ForeignKey('business.busID'))
    roles = db.relationship('Role', secondary=roles, lazy='subquery', backref=db.backref('usercredentials', lazy='dynamic'))
    
    def __init__(self, userID, busID, user_email, user_password, roles, active):  
      self.userID = userID
      self.busID = busID
      self.roles = roles
      self.user_email = user_email
      self.user_password = generate_password_hash(user_password,method = 'pbkdf2:sha256')
      self.active = active; 

    def is_active(self):
      """Flask-Login: return True if the user is active."""
      return self.active

class RoleType(enum.Enum): 
  owner = 'Business Owner'
  employee = 'Employee'
  manager = 'Financial Manager'
  
class Role(db.Model):
    __tablename__ = 'role'

    rolename = db.Column(db.String(30), primary_key=True)

 