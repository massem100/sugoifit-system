from flask import current_app
from app import db
from app.model.auth import Busines
import enum 


class Financialstmt(db.Model):
    __tablename__ = 'financialstmt'

    stmtID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    fs_name = db.Column(db.String(50), nullable= False, unique=True)

    def __init__(self, fs_name):
        self.fs_name = fs_name

    def __repr__(self):
        return 'Financial Statement {} {} '.format(self.stmtID, self.fs_name)
    

class FinancialStatementType(enum.Enum):
    balance_sheet = 'balance sheet'
    income_statement = 'income statement'
    cash_flow_statement = 'cash flow statement'

class Financialstmtline(db.Model):
    __tablename__ = 'financialstmtline'

    lineID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    line_name = db.Column(db.String(250))
    tag = db.Column(db.String(50))
    sequences = db.relationship('Financialstmtlineseq', backref = "financialstmtline")
    desc = db.relationship('Financialstmtdesc', backref = 'financialstmtline')
    
    def __init__(self,  tag, line_name):
        self.line_name = line_name
        self.tag = tag
        


class Financialstmtdesc(db.Model):
    __tablename__ = 'financialstmtdesc'
    __table_args__ = tuple(
        [db.UniqueConstraint('busID',
                          'fsLineID',
                          'fiscalYear',
                          'fiscalPeriod')])
    fStmtDescID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'),nullable=False, unique=True)
    fsLineID = db.Column(db.ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
    fiscalYear = db.Column(db.Integer)
    fiscalPeriod = db.Column(db.Date)
    fillingDATE = db.Column(db.Date)
    startDATE = db.Column(db.Date)
    endDATE = db.Column(db.Date)
    amount = db.Column(db.Float)

    # busines = db.relationship('Busines')

    def __init__(self, fStmtDescID, busID, fsLineID, fiscalPeriod, fillingDATE, fiscalYear, startDATE, endDATE, amount):
        self.fStmtDescID = fStmtDescID
        self.busID = busID
        self.fsLineID = fsLineID
        self.fiscalPeriod = fiscalPeriod
        self.fillingDATE = fillingDATE
        self.fiscalYear = fiscalYear
        self.startDATE = startDATE
        self.endDATE = endDATE
        self.amount = amount


class Financialstmtlinealia(db.Model):
    __tablename__ = 'financialstmtlinealias'

    
    aliasID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    lineID = db.Column(db.ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    lineAlias = db.Column(db.String(50), nullable= False, unique=True)


    financialstmtline = db.relationship('Financialstmtline')
    

    def __init__(self, lineID, fsStmtID, aliasID, lineAlias):
        self.lineID = lineID
        self.fsStmtID = fsStmtID
        self.aliasID = aliasID
        self.lineAlias = lineAlias


class Financialstmtlineseq(db.Model):
    __tablename__ = 'financialstmtlineseq'

    lineSeqID = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    fsStmtID = db.Column(db.ForeignKey('financialstmt.stmtID', ondelete='CASCADE', onupdate='CASCADE'),  nullable=False, index=True)
    fsStmtLineID = db.Column(db.ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    sequence = db.Column(db.Integer)
    db.UniqueConstraint(fsStmtID,fsStmtLineID)

    financialstmt = db.relationship('Financialstmt')


    def __init__(self, sequence, fsStmtID, fsStmtLineID): 
        # self.lineSeqID = lineSeqID
        self.fsStmtID = fsStmtID
        self.fsStmtLineID = fsStmtLineID 
        self.sequence = sequence


