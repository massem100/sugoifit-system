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
    accountName = db.Column(db.String(250))
    accountBalance = db.Column(db.String(250))

    genLedger = db.relationship('GeneralLedger')

"""
--------------------------------------- General Ledger Accounts Tables------------------------------------------------
              ------------------------------------- Assets ----------------------------------------------
"""

class CurrentAsset(db.Model):
    __tablename__ = 'currentasset'

    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    ledgerID = db.Column(db.ForeignKey('genledger.ledgerID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    assetName = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)   
    tag = db.Column(db.String(50))
    lifeSpan = db.Column(db.Integer)
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

   
    genLedger = db.relationship('GeneralLedger')

    def ___init__(self, id, ledgerID,  assetName, acquisDATE, tag, lifeSpan, related_entry, Balance, BalanceDC, debitBalance=0, creditBalance =0):
        self.ledgerID = ledgerID 
        self.id =id
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
        return "<Current Asset {}, {}>".format(self.id, self.assetName)
    
    def debit(id, related_entry,  tag, asset_name, balance, balanceDC, lst): 
        balance += float(lst[2])
        debitEntry = CurrentAsset(id = id, ledgerID = lst[0],  assetName = asset_name, 
                                            acquisDATE = lst[1], tag = tag, lifeSpan= lst[3], related_entry = related_entry, 
                                            Balance = balance, BalanceDC = balanceDC, debitBalance = lst[2])
        return debitEntry 

    def credit(id, related_entry,  tag, asset_name, balance, balanceDC, lst): 
        balance -= float(lst[2])
        creditEntry =  CurrentAsset(id = id, ledgerID = lst[0],  assetName = asset_name, 
                                    acquisDATE = lst[1], tag = tag, lifeSpan= lst[3], related_entry = related_entry, 
                                    Balance = balance, BalanceDC = balanceDC, creditBalance = lst[2])
        return creditEntry
    

class NonCurrentAsset(db.Model):
    __tablename__ = 'noncurrentasset'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ledgerID = db.Column(db.ForeignKey('genledger.ledgerID', ondelete='CASCADE', onupdate='CASCADE'), index=True)    
    assetName = db.Column(db.String(100))
    tag = db.Column(db.String(50))
    lifeSpan = db.Column(db.Integer)
    totalUnits = db.Column(db.Integer)
    depType = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)   
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    genLedger = db.relationship('GeneralLedger')

    def __init__(self, id, ledgerID, assetName, lifeSpan, depType, acquisDATE, tag,  related_entry, 
                  Balance, BalanceDC, totalUnits=0, debitBalance =0, creditBalance=0):
        self.ledgerID = ledgerID 
        self.id = id
        self.assetName = assetName 
        self.lifeSpan = lifeSpan
        self.tag = tag
        self.depType = depType
        self.totalUnits = totalUnits
        self.acquisDATE = acquisDATE
        self.related_entry = related_entry
        self.debitBalance = debitBalance    
        self.creditBalance = creditBalance
        self.Balance = Balance
        self.BalanceDC = BalanceDC       
    
    def debit(id, related_entry,  tag, asset_name, balance, balanceDC, lst): 
        balance += float(lst[4])
        debitEntry = NonCurrentAsset(id= id, ledgerID = lst[0], assetName = asset_name, lifeSpan = lst[1],
                                     depType = lst[2], acquisDATE = lst[3], tag = tag, related_entry = related_entry, 
                                     Balance = balance, BalanceDC = balanceDC, debitBalance = lst[4])
        return debitEntry
    
    def credit(id, related_entry,  tag, asset_name, balance, balanceDC, lst): 
        balance -= float(lst[4])
        creditEntry = NonCurrentAsset(id= id, ledgerID = lst[0], assetName = asset_name, lifeSpan = lst[1], 
                                      depType = lst[2], acquisDATE = lst[3], tag = tag,  related_entry = related_entry,  
                                      Balance = balance, BalanceDC = balanceDC, creditBalance = lst[4])
        return creditEntry
    
    def calcDepExpense(dep_type,  assetCost, lifeSpan=0.00, totalUnits=0, salvageVal=0.00, remainingLife=0): 
        if dep_type=="Straight-Line Method": 
            return NonCurrentAsset.straightLineDep(AssetCost = assetCost, SalvageVal = salvageVal, LifeSpan = lifeSpan)
        elif dep_type == "Declining Balance":
            return NonCurrentAsset.DDMethod(AssetCost = assetCost, LifeSpan = lifeSpan)
        elif dep_type == "Units of Production":  
            return NonCurrentAsset.UnitsOfProd(TotalUnits = totalUnits, AssetCost = assetCost, SalvageVal = salvageVal)
            
        else: 
            # to be calculated 
            sumDigits= 0
            for i in range(1, len(lifeSpan)+1): 
                print(i)
                sumDigits += i
                    
            return NonCurrentAsset.SumYearDigits(RemainingLife=remainingLife, SumDigits = sumDigits, 
                                        AssetCost = assetCost, SalvageVal = salvageVal)

    def straightLineDep(**kwargs):
        return (kwargs.get("AssetCost", 0 ) - kwargs.get("SalvageVal", 0 ))/ kwargs.get("LifeSpan", 0 )

    def DDMethod(**kwargs):
        dep_rate = (1/kwargs.get("LifeSpan", 0 ))*2
        return kwargs.get("AssetCost", 0 )*dep_rate

    def UnitsOfProd(**kwargs):
        dep_expense = (kwargs.get("AssetCost", 0 ) - kwargs.get("SalvageVal", 0 )) / kwargs.get('TotalUnits', 0)
        return dep_expense

    def SumYearDigits(**kwargs):
        dep_expense = (kwargs.get("remainingLife", 0 ) / kwargs.get("sumDigits", 0 )) *\
                      (kwargs.get("assetCost", 0 ) - kwargs.get("salvageVal", 0 ))
        return dep_expense
    
    def __repr__(self): 
        return "<Non Current Asset {}, {} >".format(self.id, self.assetName)
"""
--------------------------------------- Liabilities----------------------------------------------------------
"""

class Currentliability(db.Model):
    __tablename__ = 'currentliability'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    ledgerID = db.Column(db.ForeignKey('genledger.ledgerID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    liabName = db.Column(db.String(100))
    borwDATE = db.Column(db.Date)
    loanPeriods = db.Column(db.Integer)
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   
    genLedger = db.relationship('GeneralLedger')
    
    def __init__(self, id, ledgerID, liabName, borwDATE, loanPeriods, tag, related_entry, Balance, BalanceDC, debitBalance = 0, creditBalance =0): 
        self.id = id 
        self.ledgerID = ledgerID 
        self.liabName = liabName
        self.borwDATE = borwDATE
        self.loanPeriods = loanPeriods
        self.tag = tag
        self.related_entry = related_entry
        self.debitBalance = debitBalance
        self.creditBalance = creditBalance
        self.Balance = Balance 
        self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Current Liability {}, {}>".format(self.id, self.liabName)

    def debit(id, related_entry,  tag, liab_name, balance, balanceDC, lst): 
        balance -= float(lst[3])
        debitEntry= Currentliability(id = id, ledgerID =lst[0], liabName = liab_name,
                                     borwDATE = lst[1], loanPeriods= lst[2], tag = tag, related_entry = related_entry,
                                     Balance = balance, BalanceDC = balanceDC, debitBalance = lst[3])
        return debitEntry
    
    def credit(id, related_entry,  tag, liab_name, balance, balanceDC, lst): 
        balance += float(lst[3])
        creditEntry = Currentliability(id = id, ledgerID =lst[0], liabName = liab_name,
                                       borwDATE = lst[1], loanPeriods =lst[2], tag = tag, related_entry = related_entry,
                                       Balance = balance, BalanceDC = balanceDC, creditBalance = lst[3])
        return creditEntry


class Longtermliability(db.Model):
    __tablename__ = 'longtermliability'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    ledgerID = db.Column(db.ForeignKey('genledger.ledgerID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    liabName = db.Column(db.String(100))
    borwDATE = db.Column(db.Date)
    loanPeriods = db.Column(db.Integer)
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   
    
    genLedger = db.relationship('GeneralLedger')

    def __init__(self, id, ledgerID, liabName, borwDATE, loanPeriods, tag,  related_entry, Balance, BalanceDC, debitBalance =0, creditBalance =0): 
        self.id = id
        self.ledgerID = ledgerID 
        self.liabName = liabName
        self.borwDATE = borwDATE
        self.loanPeriods = loanPeriods
        self.tag = tag
        self.related_entry = related_entry
        self.debitBalance = debitBalance
        self.creditBalance = creditBalance
        self.Balance = Balance 
        self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Long Term Liability {}, {}>".format(self.id, self.liabName)
    
    def debit(id, related_entry,  tag, liab_name, balance, balanceDC, lst): 
        balance -= float(lst[3])
        debitEntry= Longtermliability(id = id, ledgerID =lst[0], liabName = liab_name,
                                     borwDATE = lst[1], loanPeriods = lst[2], tag= tag, related_entry = related_entry,
                                     Balance = balance, BalanceDC = balanceDC, debitBalance = lst[3])
        return debitEntry
        # lst= [ledgerID,  borrow_date, dueDate, amount]
    def credit(id, related_entry,  tag, liab_name, balance, balanceDC, lst): 
        balance += float(lst[3])
        creditEntry = Longtermliability(id = id, ledgerID =lst[0], liabName = liab_name,
                                       borwDATE = lst[1], loanPeriods= lst[2], tag = tag, related_entry = related_entry,
                                       Balance = balance, BalanceDC = balanceDC, creditBalance = lst[3])
        return creditEntry
    

   
"""
--------------------------------------- Expenses ----------------------------------------------------------
"""
class OperatingExpense(db.Model):
    __tablename__ = 'opex'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    ledgerID = db.Column(db.ForeignKey('genledger.ledgerID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    opexName = db.Column(db.String(100))
    dateIncurred = db.Column(db.Date())
    expenseCategory = db.Column(db.String(80))
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    genLedger = db.relationship('GeneralLedger')

    def __init__(self, id, ledgerID, opexName, dateIncurred, expenseCategory,tag, related_entry,
                 Balance, balanceDC, debitBalance =0, creditBalance =0): 
        self.id =id 
        self.ledgerID = ledgerID 
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
        return "<Operating Expense {},{}".format(self.id, self.opexName)
    
    def debit(id, related_entry,  tag, exp_name, balance, balanceDC, lst): 
        balance += float(lst[3])
        debitEntry = OperatingExpense(id= id, ledgerID =lst[0], opexName = exp_name, dateIncurred = lst[1],
                                      expenseCategory =lst[2], tag = tag, related_entry=related_entry, 
                                      balance = balance, balanceDC = balanceDC, debitBalance =lst[3])
        return debitEntry
    
    def credit(id, related_entry,  tag, exp_name, balance, balanceDC, lst): 
        balance -= float([3])
        creditEntry = OperatingExpense(id= id, ledgerID =lst[0], opexName = exp_name, dateIncurred = lst[1],
                                      expenseCategory =lst[2], tag = tag, related_entry =related_entry, 
                                      balance = balance, balanceDC = balanceDC, creditBalance =lst[3])
        return creditEntry
    
 
   

class NonOperatingExpense(db.Model):
    __tablename__ = 'nonopex'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    ledgerID = db.Column(db.ForeignKey('genledger.ledgerID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    nOpexName = db.Column(db.String(100))
    dateIncurred = db.Column(db.Date())
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    genLedger = db.relationship('GeneralLedger')

    def __init__(self, id, ledgerID, nOpexName, dateIncurred, tag, related_entry, Balance, BalanceDC, debitBalance =0, creditBalance=0): 
        self.id = id 
        self.ledgerID = ledgerID 
        self.nOpexName = nOpexName 
        self.dateIncurred = dateIncurred
        self.tag = tag
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        self.Balance = Balance 
        self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Non Operating Expense {},{}".format(self.id, self.nOpexName)
    
     
    def debit(id, related_entry,  tag, exp_name, balance, balanceDC, lst): 
        balance += float(lst[2])
        debitEntry = OperatingExpense(id= id, ledgerID =lst[0], nOpexName = exp_name, dateIncurred = lst[1], tag = tag,
                                      related_entry=related_entry, Balance = balance, BalanceDC = balanceDC, debitBalance =lst[2])
        return debitEntry
    
    def credit(id, related_entry,  tag, exp_name, balance, balanceDC, lst): 
        balance -= float([2])
        creditEntry = OperatingExpense(id= id, ledgerID =lst[0], opexName = exp_name, dateIncurred = lst[1], tag = tag,
                                      related_entry =related_entry, Balance = balance, BalanceDC = balanceDC, creditBalance =lst[2])
        return creditEntry
   
   
"""
--------------------------------------- Revenues ----------------------------------------------------------
"""
class OperatingRevenue(db.Model):
    __tablename__ = 'oprev'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    ledgerID = db.Column(db.ForeignKey('genledger.ledgerID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    oprevName = db.Column(db.String(100))
    dateEarned = db.Column(db.Date())
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))


    genLedger = db.relationship('GeneralLedger')

    def __init__(self, id, ledgerID, oprevName, dateEarned, tag, related_entry, Balance, BalanceDC, debitBalance = 0, creditBalance =0): 
        self.id = id
        self.ledgerID = ledgerID 
        self.oprevName = oprevName
        self.dateEarned = dateEarned
        self.tag = tag
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        self.Balance = Balance 
        self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Operating Revenue{},{}".format(self.id, self.oprevName)
    
    def debit(id, related_entry,  tag, rev_name, balance, balanceDC, lst): 
        balance -= float(lst[2])
        debitEntry = OperatingRevenue(id = id, ledgerID = lst[0], oprevName = rev_name, dateEarned = lst[1], tag = tag,
                                      related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, debitBalance = lst[2])
        return debitEntry
    
    def credit(id, related_entry,  tag, rev_name, balance, balanceDC, lst):
        balance += float(lst[2])
        creditEntry = OperatingRevenue(id = id, ledgerID = lst[0], oprevName = rev_name, dateEarned = lst[1], tag = tag,
                                      related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, creditBalance = lst[2])
        return creditEntry
   
   
class NonOperatingRevenue(db.Model):
    __tablename__ = 'nonoprev'

    id= db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    ledgerID = db.Column(db.ForeignKey('genledger.ledgerID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    nOprevName = db.Column(db.String(100))
    dateEarned = db.Column(db.Date())
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))


    genLedger = db.relationship('GeneralLedger')

    def __init__(self, id, ledgerID, nOprevName, dateEarned, tag, related_entry, Balance, BalanceDC, debitBalance =0, creditBalance=0): 
        self.id= id
        self.ledgerID = ledgerID 
        self.nOprevName = nOprevName
        self.dateEarned = dateEarned
        self.tag = tag
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        self.Balance = Balance 
        self.BalanceDC = Balance

    def __repr__(self): 
        return "<Non Operating Revenue{},{}".format(self.id, self.nOprevName)
    
    def debit(id, related_entry,  tag, rev_name, balance, balanceDC, lst): 
        balance -= float(lst[2])
        debitEntry = NonOperatingRevenue(id= id, ledgerID = lst[0], nOprevName = rev_name, dateEarned = lst[1], tag = tag,
                                      related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, debitBalance = lst[2])
        return debitEntry
    
    def credit(id, related_entry,  tag, rev_name, balance, balanceDC, lst):
        balance += float(lst[2])
        creditEntry = NonOperatingRevenue(id= id, ledgerID = lst[0], nOprevName = rev_name, dateEarned = lst[1], tag = tag,
                                      related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, creditBalance = lst[2])
        return creditEntry
    
   
   

"""
--------------------------------------- Equity ----------------------------------------------------------
"""
class ShareholdersEquity(db.Model):
    __tablename__ = 'equity'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    ledgerID = db.Column(db.ForeignKey('genledger.ledgerID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    equityName = db.Column(db.String(100))
    date = db.Column(db.Date())
    tag = db.Column(db.String(50))
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

 
    genLedger = db.relationship('GeneralLedger')

    def ___init__(self, id, ledgerID, equityName, date, tag, related_entry, Balance, BalanceDC, debitBalance =0, creditBalance= 0): 
        self.id = id
        self.ledgerID =ledgerID 
        self.equityName =equityName
        self.date =date 
        self.tag = tag
        self.related_entry =related_entry
        self.debitBalance =debitBalance
        self.creditBalance =creditBalance
        self.Balance = Balance
        self.BalanceDC = BalanceDC
    
    def __repr__(self): 
        return "<Equity {}, {}>".format(self.id, self.equityName)
    
    def debit(id, related_entry,  tag, equity_name, balance, balanceDC, lst): 
        balance -= float(lst[2])
        debitEntry = ShareholdersEquity(id = id, ledgerID = lst[0], equityName = equity_name, date = lst[1], tag = tag,
                                        related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, debitBalance =lst[2])
        return debitEntry
    
    def credit(id, related_entry,  tag, equity_name, balance, balanceDC, lst): 
        balance += float(lst[2])
        creditEntry = ShareholdersEquity(id = id, ledgerID = lst[0], equityName = equity_name, date = lst[1], tag = tag,
                                        related_entry = related_entry, Balance = balance, BalanceDC = balanceDC, creditBalance =lst[2])
        return creditEntry
    
 



