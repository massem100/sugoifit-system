# from app import db
# from app.model.auth import User

# class Accounttype(db.Model):
#     __tablename__ = 'accounttype'

#     typeID = db.Column(db.String(10), primary_key=True)
#     accountCategory = db.Column(db.String(100)) 


# class Account(db.Model):
#     __tablename__ = 'account'

#     accountID = db.Column(db.String(10), primary_key=True)
#     accountName = db.Column(db.String(100))
#     typeID = db.Column(db.ForeignKey('accounttype.typeID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     accounttype = db.relationship('Accounttype')


# class Voucher(db.Model):
#     __tablename__ = 'voucher'

#     vouchID = db.Column(db.String(5), primary_key=True, unique=True)
#     accountID = db.Column(db.ForeignKey('account.accountID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     vType = db.Column(db.Enum('creditVoucher', 'debitVoucher'))
#     vDATE = db.Column(db.Date)
#     authBy = db.Column(db.ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     prepBy = db.Column(db.ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     account = db.relationship('Account')
#     user = db.relationship('User', primaryjoin='Voucher.authBy == User.userID')
#     user1 = db.relationship('User', primaryjoin='Voucher.prepBy == User.userID')


# class Credit(Voucher):
#     __tablename__ = 'credit'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID'), primary_key=True)
#     accountID = db.Column(db.ForeignKey('account.accountID'), nullable=False, index=True)
#     sourceNo = db.Column(db.Integer)
#     Amount = db.Column(db.DECIMAL(10, 2))
#     Narration = db.Column(db.String(100))

#     account = db.relationship('Account')


# class Creditvoucher(Voucher):
#     __tablename__ = 'creditvoucher'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID'), primary_key=True)
#     vDATE = db.Column(db.Date)
#     credit = db.Column(db.DECIMAL(10, 2))
#     authBy = db.Column(db.ForeignKey('user.userID'), index=True)
#     prepBy = db.Column(db.ForeignKey('user.userID'), index=True)

#     user = db.relationship('User', primaryjoin='Creditvoucher.authBy == User.userID')
#     user1 = db.relationship('User', primaryjoin='Creditvoucher.prepBy == User.userID')


# class Debit(Voucher):
#     __tablename__ = 'debit'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID'), primary_key=True)
#     accountID = db.Column(db.ForeignKey('account.accountID'), nullable=False, index=True)
#     sourceNo = db.Column(db.Integer)
#     Amount = db.Column(db.DECIMAL(10, 2))
#     Narration = db.Column(db.String(100))

#     account = db.relationship('Account')


# class Debitvoucher(Voucher):
#     __tablename__ = 'debitvoucher'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID'), primary_key=True)
#     vDATE = db.Column(db.Date)
#     debit = db.Column(db.DECIMAL(10, 2))
#     authBy = db.Column(db.String(100))
#     prepBy = db.Column(db.String(100))


# class Voucherdetail(Voucher):
#     __tablename__ = 'voucherdetails'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
#     sourceNo = db.Column(db.Integer)
#     Amount = db.Column(db.DECIMAL(10, 2))
#     Narration = db.Column(db.String(100))


# class Supportdoc(db.Model):
#     __tablename__ = 'supportdoc'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
#     sourceNo = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
#     docName = db.Column(db.String(100))
#     docDATE = db.Column(db.Date)

#     voucher = db.relationship('Voucher')

