from app import db



class Busines(db.Model):
    __tablename__ = 'business'

    busID = db.Column(db.Integer, primary_key=True, unique=True)
    busName = db.Column(db.String(100))
    busemail = db.Column(db.String(255))
    busaddress = db.Column(db.String(100))
    telephone = db.Column(db.String(100))

class User(db.Model):
    __tablename__ = 'user'

    userID = db.Column(db.String(5), primary_key=True, unique=True)
    fname = db.Column(db.String(25))
    lname = db.Column(db.String(25))
    user_address = db.Column(db.String(50))
    phone = db.Column(db.String(10))


class Credential(db.Model):
    __tablename__ = 'credentials'

    userID = db.Column(db.ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
    role = db.Column(db.String(10))
    email = db.Column(db.String(50), primary_key=True)
    user_password = db.Column(db.String(255))
    pass_salt = db.Column(db.String(50))

    user = db.relationship('User')