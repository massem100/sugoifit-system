from app import db 
from app.model.auth import Busines
 
class Financialstmt(db.Model):
    __tablename__ = 'financialstmt'

    stmtID = db.Column(db.String(10), primary_key=True, unique=True)
    fs_name = db.Column(db.String(50))


class Financialstmtline(db.Model):
    __tablename__ = 'financialstmtline'

    lineID = db.Column(db.Integer, primary_key=True, unique=True)
    line_name = db.Column(db.String(50))
    lineDesc = db.Column(db.String(50))


class Financialstmtdesc(db.Model):
    __tablename__ = 'financialstmtdesc'

    fStmtDescID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    companyID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)
    fsLineID = db.Column(db.ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)
    fiscalPeriod = db.Column(db.Date)
    fillingDATE = db.Column(db.Date)
    fiscalYear = db.Column(db.Integer)
    startDATE = db.Column(db.Date)
    endDATE = db.Column(db.Date)
    unit = db.Column(db.DECIMAL(10, 2))

    busines = db.relationship('Busines')
    financialstmtline = db.relationship('Financialstmtline')


class Financialstmtlinealia(db.Model):
    __tablename__ = 'financialstmtlinealias'

    lineID = db.Column(db.ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)
    fsStmtID = db.Column(db.ForeignKey('financialstmt.stmtID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    aliasID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    lineAlias = db.Column(db.String(50))

    financialstmt = db.relationship('Financialstmt')
    financialstmtline = db.relationship('Financialstmtline')


class Financialstmtlineseq(db.Model):
    __tablename__ = 'financialstmtlineseq'

    lineSeqID = db.Column(db.Integer, primary_key=True, nullable=False)
    fsStmtID = db.Column(db.ForeignKey('financialstmt.stmtID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    fsStmtLineID = db.Column(db.ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    sequence = db.Column(db.Integer)

    financialstmt = db.relationship('Financialstmt')
    financialstmtline = db.relationship('Financialstmtline')