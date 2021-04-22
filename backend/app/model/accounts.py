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

class CurrentAsset(db.Model):
    __tablename__ = 'currentasset'

    caID= db.Column(db.Integer, primary_key=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    assetName = db.Column(db.String(100))
    acquisDATE = db.Column(db.Date)   
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

   
    busines = db.relationship('Busines')

    def ___init__(self, caID, busID,  assetName, acquisDATE, related_entry, debitBalance=0, creditBalance =0):
        self.busID = busID 
        self.caID = caID
        self.assetName = assetName 
        self.lifeSpan = lifeSpan
        self.acquisDATE = acquisDATE
        self.related_entry = related_entry
        self.debitBalance = debitBalance
        self.creditBalance = creditBalance
        # self.Balance = 
        # self.BalanceDC = BalanceDC       
    
    def __repr__(self): 
        return "<Current Asset {}, {}>".format(self.caID, self.assetName)
    
    def debit(lst,related_entry, asset_name): 

        debitEntry = CurrentAsset(caID = lst[0], busID = lst[1],  assetName = asset_name, 
                                            acquisDATE = lst[4], related_entry = related_entry, debitBalance = lst[5])
        return debitEntry 

    def credit(lst, related_entry, asset_name): 

        creditEntry =  CurrentAsset(caID = lst[0], busID = lst[1],  assetName = asset_name, 
                                    acquisDATE = lst[4], related_entry = related_entry, creditBalance = lst[5])
        return creditEntry

    def increase(account_affected, asset_name, lst):
        if account_affected == "cash": 
            # Debit the Asset Account 
            # Calculate Accum Depreciation - to be done 
            related_entry = "Cash" + str(lst[0])
            debitEntry = CurrentAsset.debit(related_entry, asset_name, lst)

            # Credit the Cash Class 
            #  Retrieve asset id from database and increment by 1
            # Get Previous Balance and add if new entry is debit and subtract otherwise 
            creditEntry = CurrentAsset.credit(related_entry, "Cash", lst)

            return debitEntry, creditEntry
        elif account_affected == "Cheque": 
            #Debit the NCA Asset Account
            related_entry = "Cheque" + str(lst[0])
            debitEntry = CurrentAsset.debit(lst, related_entry, asset_name)

            # Credit the Bank Account
            creditEntry = CurrentAsset.credit(lst, related_entry, "Bank")

            return debitEntry, creditEntry
        else: 
            # Debit the Asset Class 
            related_entry = "CL" + str(lst[0])
            debitEntry = CurrentAsset.debit(lst, related_entry, asset_name)

            # Credit the liability account
            creditEntry = Currentliability.credit(lst, related_entry, "Accounts Payable")

            return debitEntry, creditEntry
             
    def decrease(account_affected, lst): 
        # Identifying the second account in double entry 
        if account_affected == "cash": 
            
            # Debit the Cash Class 
            debitEntry = CurrentAsset.debit(lst, related_entry, "Cash")

            # Credit the Asset Class 
            NCA_related_entry = "Cash" +str(lst[0])
            creditEntry = CurrentAsset.credit(lst,NCA_related_entry, asset_name)


            return debitEntry, creditEntry

        elif account_affected == "Cheque": 
            
            #Debit the Asset Class
            debitEntry = CurrentAsset.debit(lst, related_entry, "Bank")

            #Credit the Asset Class 
            NCA_related_entry = "Cash" +str(lst[0])
            creditEntry = CurrentAsset.credit(lst,NCA_related_entry, asset_name)

            return debitEntry,creditEntry
        else: 
            #Debit the Accounts Receivable Account -Asset
            debitEntry = CurrentAsset.debit(lst, related_entry, "Accounts Receivable")

            #Credit the Asset Class 
            NCA_related_entry = "Cash" +str(lst[0])
            creditEntry = CurrentAsset.credit(lst,NCA_related_entry, asset_name)
            
            return debitEntry, creditEntry


class NonCurrentAsset(db.Model):
    __tablename__ = 'noncurrentasset'

    ncaID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)    
    assetName = db.Column(db.String(100))
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

    def __init__(self, ncaID, busID, assetName, lifeSpan, depType, acquisDATE, related_entry, accumDep = 0, disposalAmt =0,debitBalance =0, creditBalance=0):
        self.busID = busID 
        self.ncaID = ncaID
        self.assetName = assetName 
        self.lifeSpan = lifeSpan
        self.accumDep = accumDep
        self.disposalAmt = disposalAmt
        self.depType = depType
        self.acquisDATE = acquisDATE
        self.related_entry = related_entry
        self.debitBalance = debitBalance    
        self.creditBalance = creditBalance
        self.Balance = balance()
        # self.BalanceDC = BalanceDC       
    def balance():
        balance = db.session.query(NonCurrentAsset).all()
        print(balance)
        return 0
    def debit(lst, related_entry, asset_name): 

        debitEntry = NonCurrentAsset(ncaID= lst[0], busID = lst[1], assetName = asset_name, lifeSpan = lst[2],
                                     depType = lst[3], acquisDATE = lst[4], related_entry = related_entry, 
                                      debitBalance = lst[5])
        return debitEntry
    
    def credit(lst,related_entry, asset_name): 
        creditEntry = NonCurrentAsset(ncaID= lst[0], busID = lst[1], assetName = asset_name, lifeSpan = lst[2], 
                                      depType = lst[3], acquisDATE = lst[4], related_entry = related_entry, 
                                      creditBalance = lst[5])
        return creditEntry
    
    
    def increase(account_affected, asset_name, lst):
        if account_affected == "Cash": 
            # Debit the Asset Class 
            # Calculate Accum Depreciation
            related_entry = "Cash" + str(lst[0])
            debitEntry = NonCurrentAsset.debit(lst, related_entry, asset_name)

            # Credit the Cash Class 
            #  Retrieve asset id from database and increment by 1
            # Get Previous Balance and add if new entry is debit and subtract otherwise 
            creditEntry = CurrentAsset.credit(lst, related_entry, asset_name)

            return debitEntry, creditEntry
        elif account_affected == "Cheque": 
            #Debit the Asset Class 
            related_entry = "Cheque" + str(lst[0])
            debitEntry = NonCurrentAsset.debit(lst, related_entry, asset_name)

            creditEntry = CurrentAsset.credit(lst, related_entry, asset_name)

            return debitEntry, creditEntry
        else: 
            #Debit the Asset Class 
            related_entry = "CL" + str(lst[0])
            debitEntry = NonCurrentAsset.debit(lst, related_entry, asset_name)

            #Credit the liability account
            creditEntry = Currentliability.credit(lst, related_entry, "Accounts Payable")
            return debitEntry, creditEntry
             
    def decrease(account_affected, asset_name, lst): 
        # Identifying the second account in double entry 
        if account_affected == "cash": 
            # Credit the Asset Class 
            NCA_related_entry = "Cash" +str(lst[0])
            creditEntry = NonCurrentAsset.credit(lst,NCA_related_entry, asset_name)

            # Debit the Cash Class 
            debitEntry = CurrentAsset.debit(lst, related_entry, "Cash")

            return debitEntry, creditEntry

        elif account_affected == "Cheque": 
            #Debit the Asset Class
            debitEntry = CurrentAsset.debit(lst, related_entry, "Cheque")

            #Credit the Asset Class 
            NCA_related_entry = "Cash" +str(lst[0])
            creditEntry = NonCurrentAsset.credit(lst,NCA_related_entry, asset_name)


            return debitEntry,creditEntry
        else: 
            #Debit the Accounts Receivable Account -Asset
            debitEntry = CurrentAsset.debit(lst, related_entry, "Accounts Receivable")

            #Credit the Asset Class 
            NCA_related_entry = "Cash" +str(lst[0])
            creditEntry = NonCurrentAsset.credit(lst,NCA_related_entry, asset_name)
            
            return debitEntry, creditEntry


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
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   
    
    busines = db.relationship('Busines')
    
    def __init__(self, cliabID, busID, liabName, borwDATE, dueDATE, related_entry, debitBalance = 0, creditBalance =0): 
        self.cliabID = cliabID 
        self.busID = busID 
        self.liabName = liabName
        self.borwDATE = borwDATE
        self.dueDATE = dueDATE
        self.related_entry = related_entry
        self.debitBalance = debitBalance
        self.creditBalance = creditBalance
        # self.Balance = Balance 
        # self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Current Liability {}, {}>".format(self.cliabID, self.liabName)

    def debit(lst, related_entry, liab_name): 
        debitEntry= Currentliability(cliabID = lst[9], busID =lst[1], liabName = liab_name,
                                     borwDATE = lst[5], dueDATE = "", related_entry = related_entry,
                                     debitBalance = lst[7])
        return debitEntry
    
    def credit(lst,related_entry, liab_name): 

        creditEntry = Currentliability(cliabID = lst[0], busID =lst[1], liabName = liab_name,
                                       borwDATE = lst[4], dueDATE = "", related_entry = related_entry,
                                       creditBalance = lst[3])
        return creditEntry
    def increase(account_affected, liab_name, lst): 
        
        if account_affected == "Cash": 
            debitEntry = CurrentAsset.debit(lst,related_entry, "Cash")
            creditEntry = Currentliability.credit(lst, related, liab_name)

            return debitEntry, creditEntry
            
        else:
            debitEntry = CurrentAsset.debit(lst,related_entry, "Bank")
            creditEntry = Currentliability.credit(lst,related, liab_name)
        
            return debitEntry, creditEntry 

    def decrease(account_affected, liab_name, lst): 
        
        if account_affected == "Cash": 
            debitEntry = CurrentAsset.debit(lst,related_entry, "Cash")
            creditEntry = Currentliability.credit(lst,related_entry, liab_name)

            return debitEntry, creditEntry
            
        else:
            debitEntry = CurrentAsset.debit(lst,related_entry, "Bank")
            creditEntry = Currentliability.credit(lst,related_entry, liab_name)
        
            return debitEntry, creditEntry 


class Longtermliability(db.Model):
    __tablename__ = 'longtermliability'

    LtliabID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    liabName = db.Column(db.String(100))
    borwDATE = db.Column(db.Date)
    dueDATE  = db.Column(db.Date)
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))
   
    
    busines = db.relationship('Busines')

    def __init__(self, LtliabID, busID, liabName, borwDATE, dueDATE, related_entry, debitBalance =0, creditBalance =0): 
        self.cliabID = cliabID 
        self.busID = busID 
        self.liabName = liabName
        self.borwDATE = borwDATE
        self.dueDATE = dueDATE
        self.related_entry = related_entry
        self.debitBalance = debitBalance
        self.creditBalance = creditBalance
        # self.Balance = Balance 
        # self.BalanceDC = BalanceDC

    def __repr__(self): 
        return "<Long Term Liability {}, {}>".format(self.LtliabID, self.liabName)
    
    def debit(lst,related_entry, liab_name): 
        debitEntry= Longtermliability(LtliabID = lst[9], busID =lst[1], liabName = liab_name,
                                     borwDATE = lst[5], dueDATE = "", related_entry = related_entry,
                                     debitBalance = lst[7])
        return debitEntry
    
    def credit(lst,related_entry, liab_name): 

        creditEntry = Longtermliability(LtliabID = lst[9], busID =lst[1], liabName = liab_name,
                                       borwDATE = lst[5], dueDATE = "", related_entry = related_entry,
                                       creditBalance = lst[7])
        return creditEntry
    
    def increase(account_affected, liab_name, lst): 
        
        if account_affected == "Cash": 
            debitEntry = CurrentAsset.debit(lst,related_entry, "Cash")
            creditEntry = Longtermliability.credit(lst,related, liab_name)

            return debitEntry, creditEntry
            
        else:
            debitEntry = CurrentAsset.debit(lst,related_entry, "Bank")
            creditEntry = Longtermliability.credit(lst,related, liab_name)
        
            return debitEntry, creditEntry 

    def decrease(account_affected, liab_name, lst): 
        
        if account_affected == "Cash": 
            debitEntry = CurrentAsset.debit(lst, related_entry, "Cash")
            creditEntry = Longtermliability.credit(lst,related, liab_name)

            return debitEntry, creditEntry
            
        else:
            debitEntry = CurrentAsset.debit(lst,related_entry, "Bank")
            creditEntry = Longtermliability.credit(lst,related, liab_name)
        
            return debitEntry, creditEntry 



   
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
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    
    busines = db.relationship('Busines')

    def __init__(self, opexID, busID, opexName, dateIncurred, expenseCategory, related_entry, debitBalance =0, creditBalance =0): 
        self.opexID =opexID 
        self.busID = busID 
        self.opexName = opexName 
        self.dateIncurred = dateIncurred
        self.expenseCategory = expenseCategory
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        # self.Balance = Balance 
        # self.BalanceDC

    def __repr__(self): 
        return "<Operating Expense {},{}".format(self.opexID, self.opexName)
    
    def debit(lst,related_entry, exp_name): 
        debitEntry = OperatingExpense(opexID= lst[0], busID =lst[1], opexName = exp_name, dateIncurred = lst[4],
                                      expenseCategory =lst[3], related_entry =related_entry, debitBalance =lst[5])
        return debitEntry
    
    def credit(lst,related_entry, exp_name): 
        creditEntry = OperatingExpense(opexID= lst[0], busID =lst[1], opexName = exp_name, dateIncurred = lst[4],
                                      expenseCategory =lst[3], related_entry =related_entry, creditBalance =lst[5])
        return debitEntry
    
    def increase(): 
        pass
    
    def decrease(): 
        pass
   

class NonOperatingExpense(db.Model):
    __tablename__ = 'nonopex'

    nOpexID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    nOpexName = db.Column(db.String(100))
    dateIncurred = db.Column(db.Date())
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    busines = db.relationship('Busines')

    def __init__(self, nOpexID, busID, nOpexName, dateIncurred, related_entry, debitBalance, creditBalance): 
        self.nOpexID = nOpexID 
        self.busID = busID 
        self.nOpexName = nOpexName 
        self.dateIncurred = dateIncurred
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        # self.Balance = Balance 
        # self.BalanceDC

    def __repr__(self): 
        return "<Non Operating Expense {},{}".format(self.nOpexID, self.nOpexName)
    
    def debit(): 
        pass
    
    def credit(): 
        pass
    
    def increase(): 
        pass
    
    def decrease(): 
        pass
   
"""
--------------------------------------- Revenues ----------------------------------------------------------
"""
class OperatingRevenue(db.Model):
    __tablename__ = 'oprev'

    opRevenueID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    oprevName = db.Column(db.String(100))
    dateEarned = db.Column(db.Date())
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    
    busines = db.relationship('Busines')

    def __init__(self, opRevenueID, busID, oprevName, dateEarned, related_entry, debitBalance, creditBalance): 
        self.opRevenueID = opRevenueID
        self.busID = busID 
        self.oprevName = oprevName
        self.dateEarned = dateEarned
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        # self.Balance = Balance 
        # self.BalanceDC

    def __repr__(self): 
        return "<Operating Revenue{},{}".format(self.opRevenueID, self.oprevName)
    
    def debit(): 
        pass
    
    def credit(): 
        pass
    
    def increase(): 
        pass
    
    def decrease(): 
        pass
   
class NonOperatingRevenue(db.Model):
    __tablename__ = 'nonoprev'

    nopRevenueID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    nOprevName = db.Column(db.String(100))
    dateEarned = db.Column(db.Date())
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    
    busines = db.relationship('Busines')

    def __init__(self, nopRevenueID, busID, nOprevName, dateEarned, related_entry, debitBalance, creditBalance): 
        self.nopRevenueID = nopRevenueID
        self.busID = busID 
        self.nOprevName = nOprevName
        self.dateEarned = dateEarned
        self.related_entry =related_entry
        self.debitBalance = debitBalance 
        self.creditBalance = creditBalance 
        # self.Balance = Balance 
        # self.BalanceDC

    def __repr__(self): 
        return "<Non Operating Revenue{},{}".format(self.nopRevenueID, self.nOprevName)
    
    def debit(): 
        pass
    
    def credit(): 
        pass
    
    def increase(): 
        pass
    
    def decrease(): 
        pass
   

"""
--------------------------------------- Equity ----------------------------------------------------------
"""
class ShareholdersEquity(db.Model):
    __tablename__ = 'equity'

    equityID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    equityName = db.Column(db.String(100))
    date = db.Column(db.Date())
    related_entry = db.Column(db.String(50))
    debitBalance = db.Column(db.DECIMAL(10,0))
    creditBalance = db.Column(db.DECIMAL(10,0))
    Balance = db.Column(db.DECIMAL(10, 0))
    BalanceDC = db.Column(db.Enum("Debit", "Credit"))

    busines = db.relationship('Busines')

    def ___init__(self, equityID, busID, equityName, date, related_entry, debitBalance, creditBalance): 
        self.equityID = equityID
        self.busID =busID 
        self.equityName =equityName
        self.date =date 
        self.related_entry =related_entry
        self.debitBalance =debitBalance
        self.creditBalance =creditBalance
    
    def __repr__(self): 
        return "<Equity {}, {}>".format(self.equityID, self.equityName)
    
    def debit(): 
        pass
    
    def credit(): 
        pass
    
    def increase(): 
        pass
    
    def decrease(): 
        pass


   
#     @property
#     def balance(self): 
#         return self.Balance

#     @balance.setter
#     def balance(self):
#         debitBal = self.debitBalance
#         creditBal = self.creditBalance
#         self.Balance = debitBal - creditBal
#         if self.Balance < 0: 
#             self.BalanceDC = "Credit"
#         else: 
#             self.BalanceDC = "Debit"

#     def account_affected(self, methodOfPayment): 
#         if methodOfPayment == "Cash": 
#             pass 
#         elif methodOfPayment == "Cheque": 
#             pass
#         else: 
#             pass 





