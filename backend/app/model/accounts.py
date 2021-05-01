from flask import current_app
from app import db 
from app.model.auth import Busines
from app.model.financial_statement import Financialstmt
import enum

# db = current_app.db
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

class CurrentAsset(db.Model):
    __tablename__ = 'currentasset'

    caID= db.Column(db.Integer, primary_key=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    assetName = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)   
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

   
    busines = db.relationship('Busines')

    def ___init__(self, caID, busID,  assetName, acquisDATE, tag, related_entry, Balance, BalanceDC, debitBalance=0, creditBalance =0):
        self.busID = busID 
        self.caID = caID
        self.assetName = assetName 
        self.lifeSpan = lifeSpan
        self.acquisDATE = acquisDATE
        self.tag = tag
        self.related_entry = related_entry
        self.debitBalance = debitBalance
        self.creditBalance = creditBalance
        self.Balance = Balance
        self.BalanceDC = BalanceDC       
    
    def __repr__(self): 
        return "<Current Asset {}, {}>".format(self.caID, self.assetName)
    
    def debit(caID, tag, related_entry, asset_name, balance, balanceDC, lst): 
        balance += float(lst[4])
        debitEntry = CurrentAsset(caID = caID, busID = lst[0],  assetName = asset_name, 
                                            acquisDATE = lst[3], tag = tag,  related_entry = related_entry, 
                                            Balance = balance, BalanceDC = balanceDC, debitBalance = lst[4])
        return debitEntry 

    def credit(caID, tag, related_entry, asset_name, balance, balanceDC, lst): 
        balance -= float(lst[4])
        creditEntry =  CurrentAsset(caID = caID, busID = lst[0],  assetName = asset_name, 
                                    acquisDATE = lst[3], tag = tag, related_entry = related_entry, 
                                    Balance = balance, BalanceDC = balanceDC, creditBalance = lst[4])
        return creditEntry
    

class NonCurrentAsset(db.Model):
    __tablename__ = 'noncurrentasset'

    ncaID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)    
    assetName = db.Column(db.String(100))
    tag = db.Column(db.String(50))
    lifeSpan = db.Column(db.Integer)
    accumDep = db.Column(db.DECIMAL(10, 2))
    disposalAmt = db.Column(db.DECIMAL(10, 2))
    depType = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)   
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   
    busines = db.relationship('Busines')

    def __init__(self, ncaID, busID, assetName, lifeSpan, depType, acquisDATE, tag,
                related_entry, Balance, BalanceDC, accumDep = 0, disposalAmt =0,debitBalance =0, creditBalance=0):
        self.busID = busID 
        self.ncaID = ncaID
        self.assetName = assetName 
        self.lifeSpan = lifeSpan
        self.tag = tag
        self.accumDep = accumDep
        self.disposalAmt = disposalAmt
        self.depType = depType
        self.acquisDATE = acquisDATE
        self.related_entry = related_entry
        self.debitBalance = debitBalance    
        self.creditBalance = creditBalance
        self.Balance = Balance
        self.BalanceDC = BalanceDC       
    
    def debit(ncaID, tag, related_entry, asset_name, balance, balanceDC, lst): 
        balance += float(lst[4])
        debitEntry = NonCurrentAsset(ncaID= ncaID, busID = lst[0], assetName = asset_name, lifeSpan = lst[1],
                                     depType = lst[2], acquisDATE = lst[3], tag = tag, related_entry = related_entry, 
                                     Balance = balance, BalanceDC = balanceDC, debitBalance = lst[4])
        return debitEntry
    
    def credit(ncaID, tag, related_entry, asset_name, balance, balanceDC, lst): 
        balance -= float(lst[4])
        creditEntry = NonCurrentAsset(ncaID= ncaID, busID = lst[0], assetName = asset_name, lifeSpan = lst[1], 
                                      depType = lst[2], acquisDATE = lst[3], tag = tag,  related_entry = related_entry,  
                                      Balance = balance, BalanceDC = balanceDC, creditBalance = lst[4])
        return creditEntry
    
     
    def straightLineDep(assetCost, salvageVal, lifeSpan):
        return (assetCost - salvageVal)/lifeSpan
    
    def DDMethod(assetCost,lifeSpan):
        dep_rate = (1/lifeSpan)*2
        return assetCost*dep_rate

    def UnitsOfProd(unitsProduced, lifeSpanInUnits, assetCost, salvageVal):
        dep_expense = (unitsProduced / lifeSpanInUnits) * (assetCost - salvageVal)
        return dep_expense

    def SumYearDigits():
        pass
    
    def __repr__(self): 
        return "<Non Current Asset {}, {} >".format(self.ncaID, self.assetName)
"""
--------------------------------------- Liabilities----------------------------------------------------------
"""

class Currentliability(db.Model):
    __tablename__ = 'currentliability'

    cliabID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    liabName = db.Column(db.String(100))
    borwDATE = db.Column(db.Date)
    dueDATE  = db.Column(db.Date)
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   
    
    busines = db.relationship('Busines')
    
    def __init__(self, cliabID, busID, liabName, borwDATE, dueDATE, tag, related_entry, Balance, BalanceDC, debitBalance = 0, creditBalance =0): 
        self.cliabID = cliabID 
        self.busID = busID 
        self.liabName = liabName
        self.borwDATE = borwDATE
        self.dueDATE = dueDATE
        self.tag = tag
        self.related_entry = related_entry
        self.debitBalance = debitBalance
        self.creditBalance = creditBalance
        self.Balance = Balance 
        self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Current Liability {}, {}>".format(self.cliabID, self.liabName)

    def debit(cliabID, tag, related_entry, liab_name, balance, balanceDC, lst): 
        balance -= float(lst[3])
        debitEntry= Currentliability(cliabID = cliabID, busID =lst[0], liabName = liab_name,
                                     borwDATE = lst[1], dueDATE = lst[2], tag = tag, related_entry = related_entry,
                                     Balance = balance, BalanceDC = balanceDC, debitBalance = lst[3])
        return debitEntry
    
    def credit(cliabID, tag, related_entry, liab_name, balance, balanceDC, lst): 
        balance += float(lst[3])
        creditEntry = Currentliability(cliabID = cliabID, busID =lst[0], liabName = liab_name,
                                       borwDATE = lst[1], dueDATE =lst[2], tag = tag, related_entry = related_entry,
                                       Balance = balance, BalanceDC = balanceDC, creditBalance = lst[3])
        return creditEntry


class Longtermliability(db.Model):
    __tablename__ = 'longtermliability'

    LtliabID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    liabName = db.Column(db.String(100))
    borwDATE = db.Column(db.Date)
    dueDATE  = db.Column(db.Date)
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   
    
    busines = db.relationship('Busines')

    def __init__(self, LtliabID, busID, liabName, borwDATE, dueDATE, tag,  related_entry, Balance, BalanceDC, debitBalance =0, creditBalance =0): 
        self.LtliabID = LtiabID 
        self.busID = busID 
        self.liabName = liabName
        self.borwDATE = borwDATE
        self.dueDATE = dueDATE
        self.tag = tag
        self.related_entry = related_entry
        self.debitBalance = debitBalance
        self.creditBalance = creditBalance
        self.Balance = Balance 
        self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Long Term Liability {}, {}>".format(self.LtliabID, self.liabName)
    
    def debit(LtliabID, tag, related_entry, liab_name, balance, balanceDC, lst): 
        balance -= float(lst[3])
        debitEntry= Longtermliability(LtliabID = LtliabID, busID =lst[0], liabName = liab_name,
                                     borwDATE = lst[1], dueDATE = lst[2], tag= tag, related_entry = related_entry,
                                     Balance = balance, BalanceDC = balanceDC, debitBalance = lst[3])
        return debitEntry
        # lst= [busID,  borrow_date, dueDate, amount]
    def credit(LtliabID, tag, related_entry, liab_name, balance, balanceDC, lst): 
        balance += float(lst[3])
        creditEntry = Longtermliability(LtliabID = LtliabID, busID =lst[0], liabName = liab_name,
                                       borwDATE = lst[1], dueDATE = lst[2], tag = tag, related_entry = related_entry,
                                       Balance = balance, BalanceDC = balanceDC, creditBalance = lst[3])
        return creditEntry
    

   
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
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    
    busines = db.relationship('Busines')

    def __init__(self, opexID, busID, opexName, dateIncurred, expenseCategory,tag, related_entry,
                 Balance, balanceDC, debitBalance =0, creditBalance =0): 
        self.opexID =opexID 
        self.busID = busID 
        self.opexName = opexName 
        self.dateIncurred = dateIncurred
        self.expenseCategory = expenseCategory
        self.tag = tag
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        self.Balance = Balance  
        self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Operating Expense {},{}".format(self.opexID, self.opexName)
    
    def debit(opexID, tag, related_entry, exp_name, balance, balanceDC, lst): 
        balance += float(lst[3])
        debitEntry = OperatingExpense(opexID= opexID, busID =lst[0], opexName = exp_name, dateIncurred = lst[1],
                                      expenseCategory =lst[2], tag = tag, related_entry=related_entry, 
                                      balance = balance, balanceDC = balanceDC, debitBalance =lst[3])
        return debitEntry
    
    def credit(opexID,tag, related_entry, exp_name, balance, balanceDC, lst): 
        balance -= float([3])
        creditEntry = OperatingExpense(opexID= opexID, busID =lst[0], opexName = exp_name, dateIncurred = lst[1],
                                      expenseCategory =lst[2], tag = tag, related_entry =related_entry, 
                                      balance = balance, balanceDC = balanceDC, creditBalance =lst[3])
        return creditEntry
    
 
   

class NonOperatingExpense(db.Model):
    __tablename__ = 'nonopex'

    nOpexID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    nOpexName = db.Column(db.String(100))
    dateIncurred = db.Column(db.Date())
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    busines = db.relationship('Busines')

    def __init__(self, nOpexID, busID, nOpexName, dateIncurred, tag, related_entry, Balance, BalanceDC, debitBalance =0, creditBalance=0): 
        self.nOpexID = nOpexID 
        self.busID = busID 
        self.nOpexName = nOpexName 
        self.dateIncurred = dateIncurred
        self.tag = tag
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        self.Balance = Balance 
        self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Non Operating Expense {},{}".format(self.nOpexID, self.nOpexName)
    
     
    def debit(nOpexID, tag, related_entry, exp_name, balance, balanceDC, lst): 
        balance += float(lst[2])
        debitEntry = OperatingExpense(opexID= nOpexID, busID =lst[0], nOpexName = exp_name, dateIncurred = lst[1], tag = tag,
                                      related_entry=related_entry, Balance = balance, BalanceDC = balanceDC, debitBalance =lst[2])
        return debitEntry
    
    def credit(nOpexID, tag, related_entry, exp_name, balance, balanceDC, lst): 
        balance -= float([2])
        creditEntry = OperatingExpense(opexID= opexID, busID =lst[0], opexName = exp_name, dateIncurred = lst[1], tag = tag,
                                      related_entry =related_entry, Balance = balance, BalanceDC = balanceDC, creditBalance =lst[2])
        return creditEntry
   
   
"""
--------------------------------------- Revenues ----------------------------------------------------------
"""
class OperatingRevenue(db.Model):
    __tablename__ = 'oprev'

    opRevenueID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    oprevName = db.Column(db.String(100))
    dateEarned = db.Column(db.Date())
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    
    busines = db.relationship('Busines')

    def __init__(self, opRevenueID, busID, oprevName, dateEarned, tag, related_entry, Balance, BalanceDC, debitBalance = 0, creditBalance =0): 
        self.opRevenueID = opRevenueID
        self.busID = busID 
        self.oprevName = oprevName
        self.dateEarned = dateEarned
        self.tag = tag
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        self.Balance = Balance 
        self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Operating Revenue{},{}".format(self.opRevenueID, self.oprevName)
    
    def debit(opRevenueID, tag, related_entry, rev_name, balance, balanceDC, lst): 
        balance -= float(lst[2])
        debitEntry = OperatingRevenue(opRevenueID = opRevenueID, busID = lst[0], oprevName = rev_name, dateEarned = lst[1], tag = tag,
                                      related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, debitBalance = lst[2])
        return debitEntry
    
    def credit(opRevenueID,tag,  related_entry, rev_name, balance, balanceDC, lst):
        balance += float(lst[2])
        creditEntry = OperatingRevenue(opRevenueID = opRevenueID, busID = lst[0], oprevName = rev_name, dateEarned = lst[1], tag = tag,
                                      related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, creditBalance = lst[2])
        return creditEntry
   
   
class NonOperatingRevenue(db.Model):
    __tablename__ = 'nonoprev'

    nopRevenueID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    nOprevName = db.Column(db.String(100))
    dateEarned = db.Column(db.Date())
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    
    busines = db.relationship('Busines')

    def __init__(self, nopRevenueID, busID, nOprevName, dateEarned, tag, related_entry, Balance, BalanceDC, debitBalance =0, creditBalance=0): 
        self.nopRevenueID = nopRevenueID
        self.busID = busID 
        self.nOprevName = nOprevName
        self.dateEarned = dateEarned
        self.tag = tag
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        self.Balance = Balance 
        self.BalanceDC = Balance

    def __repr__(self): 
        return "<Non Operating Revenue{},{}".format(self.nopRevenueID, self.nOprevName)
    
    def debit(nopRevenueID, tag, related_entry, rev_name, balance, balanceDC, lst): 
        balance -= float(lst[2])
        debitEntry = NonOperatingRevenue(nopRevenueID = nopRevenueID, busID = lst[0], nOprevName = rev_name, dateEarned = lst[1], tag = tag,
                                      related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, debitBalance = lst[2])
        return debitEntry
    
    def credit(nopRevenueID, tag, related_entry, rev_name, balance, balanceDC, lst):
        balance += float(lst[2])
        creditEntry = NonOperatingRevenue(nopRevenueID = nopRevenueID, busID = lst[0], nOprevName = rev_name, dateEarned = lst[1], tag = tag,
                                      related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, creditBalance = lst[2])
        return creditEntry
    
   
   

"""
--------------------------------------- Equity ----------------------------------------------------------
"""
class ShareholdersEquity(db.Model):
    __tablename__ = 'equity'

    equityID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    equityName = db.Column(db.String(100))
    date = db.Column(db.Date())
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    busines = db.relationship('Busines')

    def ___init__(self, equityID, busID, equityName, date, tag, related_entry, Balance, BalanceDC, debitBalance =0, creditBalance= 0): 
        self.equityID = equityID
        self.busID =busID 
        self.equityName =equityName
        self.date =date 
        self.tag = tag
        self.related_entry =related_entry
        self.debitBalance =debitBalance
        self.creditBalance =creditBalance
        self.Balance = Balance
        self.BalanceDC = BalanceDC
    
    def __repr__(self): 
        return "<Equity {}, {}>".format(self.equityID, self.equityName)
    
    def debit(equityID, tag, related_entry, equity_name, balance, balanceDC, lst): 
        balance -= float(lst[2])
        debitEntry = ShareholdersEquity(equityID = equityID, busID = lst[0], equityName = equity_name, date = lst[1], tag = tag,
                                        related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, debitBalance =lst[2])
        return debitEntry
    
    def credit(equityID, tag, related_entry, equity_name, balance, balanceDC, lst): 
        balance += float(lst[2])
        creditEntry = ShareholdersEquity(equityID = equityID, busID = lst[0], equityName = equity_name, date = lst[1], tag = tag,
                                        related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, creditBalance =lst[2])
        return creditEntry
    
 



