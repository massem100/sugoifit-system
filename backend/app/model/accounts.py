from app import db 
from app.model.auth import Busines
from app.model.financial_statement import Financialstmt
import enum

"""
--------------------------------------- General Ledger Tables ----------------------------------------------------------
"""
class GeneralLedger(db.Model): 
    __tablename__ = 'genledger'

    ledgerID = db.Column(db.String(80), primary_key=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    Year = db.Column(db.Date)

    busines = db.relationship('Busines')

class GeneraLedgerDetails(db.Model): 
    __tablename__ = 'ledgerdetails'

    ledgerDetailsID = db.Column(db.Integer, primary_key= True)
    ledgerID = db.Column(db.ForeignKey('genledger.ledgerID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    accountName = db.Column(db.String(250))
    accountBalance = db.Column(db.String(250))

    busines = db.relationship('Busines')
    genLedger = db.relationship('GeneralLedger')

"""
--------------------------------------- General Ledger Accounts Tables------------------------------------------------
              ------------------------------------- Assets ----------------------------------------------
"""
class Asset(db.Model):
    __tablename__ = 'asset'

    assetID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    assetName = db.Column(db.String(100))
    lifeSpan = db.Column(db.Integer)
    assetType = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
    
    busines = db.relationship('Busines')

    def __init__(self, id, name, acquisDate, lifeSpan, valueAtCost):
        self.id = id
        self.name = name
        self.acquisDate = acquisDate
        self.lifeSpan = lifeSpan
        self.assetValue = assetValue

    def __repr__(self):
        return '<Asset "{}" "{}">'.format(self.id, self.name)

class Currentasset(db.Model):
    __tablename__ = 'currentasset'

    assetID = db.Column(db.ForeignKey('asset.assetID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    caID= db.Column(db.String(10), primary_key=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    assetName = db.Column(db.String(100))
    lifeSpan = db.Column(db.Integer)
    assetType = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)   
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    asset = db.relationship('Asset')
    busines = db.relationship('Busines')

    def ___init__(self, lifeSpan):
        super().__init__() 


class Noncurrentasset(db.Model):
    __tablename__ = 'noncurrentasset'

    assetID = db.Column(db.ForeignKey('asset.assetID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    ncaID = db.Column(db.String(10), primary_key=True)
    assetName = db.Column(db.String(100))
    lifeSpan = db.Column(db.Integer)
    assetType = db.Column(db.String(100))
    AccumDep = db.Column(db.DECIMAL(10, 2))
    disposalAmt = db.Column(db.DECIMAL(10, 2))
    depType = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)   
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   
    asset = db.relationship('Asset')
    busines = db.relationship('Busines')

    def __init__(self, accumDep, depType, disposalAmt, lifeSpan ):
        super().__init__()
    

    def straightLineDep(self, assetCost, salvageVal, lifeSpan):
        return (assetCost - salvageVal)/lifeSpan
    
    def DDMethod(self,assetCost,lifeSpan):
        dep_rate = (1/lifeSpan)*2
        return assetCost*dep_rate

    def UnitsOfProd(self, unitsProduced, lifeSpanInUnits, assetCost, salvageVal):
        dep_expense = (unitsProduced / lifeSpanInUnits) * (assetCost - salvageVal)
        return dep_expense

    def SumYearDigits(self):
        pass

"""
--------------------------------------- Liabilities----------------------------------------------------------
"""
class Liability(db.Model):
    __tablename__ = 'liability'

    liabID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    liabName = db.Column(db.String(100))
    liabType = db.Column(db.String(100))
    borwDATE = db.Column(db.Date)
    dueDATE  = db.Column(db.Date)
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   

    busines = db.relationship('Busines')

class Currentliability(db.Model):
    __tablename__ = 'currentliability'

    liabID = db.Column(db.ForeignKey('liability.liabID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    cliabID = db.Column(db.String(10), primary_key=True, unique=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    liabType = db.Column(db.String(100))
    liabName = db.Column(db.String(100))
    borwDATE = db.Column(db.Date)
    dueDATE  = db.Column(db.Date)
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   
    
    busines = db.relationship('Busines')
    liab = db.relationship('Liability')


class Longtermliability(db.Model):
    __tablename__ = 'longtermliability'

    liabID= db.Column(db.ForeignKey('liability.liabID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    LtliabID = db.Column(db.String(10), primary_key=True, unique=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    liabType = db.Column(db.String(100))
    liabName = db.Column(db.String(100))
    borwDATE = db.Column(db.Date)
    dueDATE  = db.Column(db.Date)
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   
    
    busines = db.relationship('Busines')
    liab = db.relationship('Liability')

"""
--------------------------------------- Expenses ----------------------------------------------------------
"""
class OperatingExpense(db.Model):
    __tablename__ = 'opex'

    opexID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    opexName = db.Column(db.String(100))
    dateIncurred = db.Column(db.Date())
    expenseCategory = db.Column(db.String(80))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    
    busines = db.relationship('Busines')
   

class NonOperatingExpense(db.Model):
    __tablename__ = 'nonopex'

    nOpexID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    nOpexName = db.Column(db.String(100))
    dateEarned = db.Column(db.Date())
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    busines = db.relationship('Busines')

"""
--------------------------------------- Revenues ----------------------------------------------------------
"""
class OperatingRevenue(db.Model):
    __tablename__ = 'oprev'

    opRevenueID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    oprevName = db.Column(db.String(100))
    dateEarned = db.Column(db.Date())
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    
    busines = db.relationship('Busines')
   
class NonOperatingRevenue(db.Model):
    __tablename__ = 'nonoprev'

    nopRevenueID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    nOprevName = db.Column(db.String(100))
    dateEarned = db.Column(db.Date())
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    
    busines = db.relationship('Busines')

"""
--------------------------------------- Equity ----------------------------------------------------------
"""
class ShareholdersEquity(db.Model):
    __tablename__ = 'equity'

    equityID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    equityName = db.Column(db.String(100))
    date = db.Column(db.Date())
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    busines = db.relationship('Busines')


   




"""
DepType - straight line method, double declining, units of production, sum of years digits
assetCost- the current value of the asset - Depreciation is applied on a continual basis so
each year it is subtracted from the previous year value. 

Prob do this decision in the route and not class 
def depreciationCalc(self, depType, assetName,assetCost):
if depType == "Straight-Line Method": 
dep_expense = straightLineDep(assetCost, salvageVal, lifeSpan)
elif depType == "Double Decline Method":
dep_expense = DDMethod(db.Model)
elif depType == "Units of Production":
dep_expense = UnitsOfProd(db.Model)
elif depType = "Sum of Years Digits": 
dep_expense = SumYearDigits(db.Model)

assetCost -= dep_expense
"""