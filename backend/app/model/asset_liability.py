from app import db 
from app.model.auth import Busines
from app.model.financial_statement import Financialstmt

class Asset(db.Model):
    __tablename__ = 'asset'

    asset_id = db.Column(db.String(10), primary_key=True)
    a_name = db.Column(db.String(100))
    lifeSpan = db.Column(db.Integer)
    a_type = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)
    a_value = db.Column(db.DECIMAL(10, 0))
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

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

    asset_id = db.Column(db.ForeignKey('asset.asset_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    a_name = db.Column(db.String(100))
    lifeSpan = db.Column(db.Integer)
    a_type = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)
    a_value = db.Column(db.DECIMAL(10, 2))
    ca_id = db.Column(db.String(10), primary_key=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    asset = db.relationship('Asset')
    busines = db.relationship('Busines')

    def ___init__(self, lifeSpan):
        super().__init__() 


class Noncurrentasset(db.Model):
    __tablename__ = 'noncurrentasset'

    asset_id = db.Column(db.ForeignKey('asset.asset_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    a_name = db.Column(db.String(100))
    lifeSpan = db.Column(db.Integer)
    a_type = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)
    a_value = db.Column(db.DECIMAL(10, 2))
    nca_id = db.Column(db.String(10), primary_key=True)
    AccumDep = db.Column(db.DECIMAL(10, 2))
    disposalAmt = db.Column(db.DECIMAL(10, 2))
    depType = db.Column(db.String(100))
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

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


class Liability(db.Model):
    __tablename__ = 'liability'

    liab_id = db.Column(db.String(5), primary_key=True, unique=True)
    liab_type = db.Column(db.String(100))
    liab_name = db.Column(db.String(100))
    Amt_owed = db.Column(db.DECIMAL(10, 2))
    borw_DATE = db.Column(db.Date)
    loan_period = db.Column(db.Integer)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    busines = db.relationship('Busines')

class Currentliability(db.Model):
    __tablename__ = 'currentliability'

    liab_id = db.Column(db.ForeignKey('liability.liab_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    cliab_id = db.Column(db.String(10), primary_key=True, unique=True)
    liab_type = db.Column(db.String(100))
    liab_name = db.Column(db.String(100))
    Amt_owed = db.Column(db.DECIMAL(10, 2))
    borw_DATE = db.Column(db.Date)
    loan_period = db.Column(db.Integer)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    busines = db.relationship('Busines')
    liab = db.relationship('Liability')


class Longtermliability(db.Model):
    __tablename__ = 'longtermliability'

    liab_id = db.Column(db.ForeignKey('liability.liab_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    Itliab_id = db.Column(db.String(10), primary_key=True, unique=True)
    liab_type = db.Column(db.String(100))
    liab_name = db.Column(db.String(100))
    Amt_owed = db.Column(db.DECIMAL(10, 2))
    borw_DATE = db.Column(db.Date)
    loan_period = db.Column(db.Integer)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    busines = db.relationship('Busines')
    liab = db.relationship('Liability')


class Expense(db.Model):
    __tablename__ = 'expense'

    expenseID = db.Column(db.String(10), primary_key=True, unique=True)
    extype = db.Column(db.String(100))
    exname = db.Column(db.String(100))
    DATEIncurred = db.Column(db.Date())
    expenseAmt = db.Column(db.DECIMAL(10, 2))



class Purchase(db.Model):
    __tablename__ = 'purchase'

    purchaseID = db.Column(db.String(10), primary_key=True, unique=True)
    p_DATE = db.Column(db.Date)
    p_item = db.Column(db.String(100))
    p_quantity = db.Column(db.Integer)
    p_price = db.Column(db.DECIMAL(10, 2))
    busID = db.Column(db.ForeignKey('business.busID'), index=True)
    stmtID = db.Column(db.ForeignKey('financialstmt.stmtID'), index=True)

    busines = db.relationship('Busines')
    financialstmt = db.relationship('Financialstmt')

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