import os, sys
import secrets
import hashlib, random
from functools import wraps
from datetime import datetime, timedelta

# WTF Forms and SQLAlchemy Models
from app.forms import RegisterForm, LoginForm, NCAForm, websiteForm,orderForm, CLiabForm, LTLiabForm, CAForm,ExpForm, RevForm, EquityForm
from app.model import  accounts, auth, sales
from app.model.financial_statement import Financialstmt, Financialstmtline, Financialstmtlineseq, \
                                          Financialstmtlinealia,Financialstmtdesc 
from sqlalchemy import func, inspection, event
from sqlalchemy.inspection import inspect

from flask import request, jsonify, flash, session, _request_ctx_stack, g
from werkzeug.utils import secure_filename

from flask import Blueprint, current_app
from app import db, login_manager, principal, csrf_
from app.auth.routes import requires_auth
from app.views import form_errors

# Flask-Login imports for session management.
from flask_login import logout_user, current_user, login_required, login_user
from flask_principal import Principal, Permission, Identity, AnonymousIdentity
from flask_principal import RoleNeed, UserNeed, identity_changed, identity_loaded

# Blueprint Configuration
accounting= Blueprint('accounting', __name__)

"""
--------------------------------------- General Ledger Accounts Routes ----------------------------------------------------------
"""
natural_balances = {
                    "NonCurrentAsset": "Debit", 
                    "CurrentAsset": "Debit", 
                    "Currentliability" : "Credit",
                    "Longtermliability" : "Credit",
                    "OperatingExpense" : "Debit",
                    "NonOperatingExpense" : "Debit",
                    "OperatingRevenue" : "Credit",
                    "NonOperatingRevenue" : "Credit",
                    "ShareholdersEquity" : "Credit",
                   }
                   
def account_balances(ledgerID, *args,**accounts): 
    account_bal = []
    for key, value in accounts.items(): 
        balance = db.session.query(value).filter_by(ledgerID = ledgerID).order_by(value.id.desc()).first()
        balance = (float(balance.Balance) if balance is not None else 0)
        account_bal.append(balance)
    return account_bal

def get_last_id(ledgerID, *args,**accounts): 
    id_lst = []
    for key, value in accounts.items(): 
        last_id = db.session.query(value).filter_by(ledgerID = ledgerID).order_by(value.id.desc()).first()
        last_id = (int(last_id.id)+1 if last_id is not None else 1)
        id_lst.append(last_id)
    return id_lst

def bal_debit_cred(ledgerID, balance_label, amount, **balances): 
    debit_cred = []
    for key, value in balances.items():
        print(type(key)) 
        total_sum =  value.query.with_entities( value.ledgerID,
                                                func.coalesce(func.sum(value.debitBalance),0).label("totalDebit"),
                                                func.coalesce(func.sum(value.creditBalance),0).label("totalCredit")
                                              ).filter_by(ledgerID = ledgerID).first()
        if "Debit" in balance_label: 
            BalanceDC = ("Debit" if float(total_sum.totalDebit) + amount > float(total_sum.totalCredit) else "Credit")
        elif "Credit" in balance_label: 
            BalanceDC = ("Debit" if float(total_sum.totalDebit) > float(total_sum.totalCredit) + amount else "Credit")
        else: 
            BalanceDC = natural_balances[key]
        debit_cred.append(BalanceDC)
    return debit_cred 

def findLedger(busID, year): 
    ledger = db.session.query(accounts.GeneralLedger).filter_by(busID =busID, year = year).first()
    if ledger is None:
        newledger = accounts.GeneralLedger(ledgerID=None, busID=busID, year=year)

        try:
            db.session.add(newledger)
            db.session.commit()
        except Exception as e:
            error = str(e)
            print(error)
        newledger = db.session.query(accounts.GeneralLedger).filter_by(busID=busID, year=year).first()
        if newledger is not None: 
            return newledger.ledgerID
    else:
        return ledger.ledgerID
    
def prepAccounts(ledgerID, label, amount, *args, **kwargs):
    account_starter ={} 
    for  key, value in kwargs.items():
        account_store = []
        last_id = get_last_id(ledgerID, key=value)
        account_store.append(last_id)
        # Get the balances of Accounts 
        balances = account_balances(ledgerID, key=value)
        account_store.append(balances)

        BalanceDC = bal_debit_cred(ledgerID, "Debit", amount, key=value)
        account_store.append(BalanceDC)
        account_starter[key]=account_store
    return account_starter

    

@accounting.route('/api/transaction/<busID>/currentasset', methods = ["POST", "GET"])
@login_required
@requires_auth
def ca_transaction(busID):
    if request.method == "POST": 
    
        form = CAForm(request.form)
        asset_name = form.asset_name.data 
        transaction_date = form.transaction_date.data 
        asset_desc = form.asset_desc.data 
        amount = float(form.amount.data)
        account_affected = form.paid_using.data
        increase_decrease = form.increase_decrease.data
        loanPeriods = form.loan_period.data
        tag=form.tag.data
        ledgerID =findLedger(busID, 2021)
        # FIX HOW DATE IS ADDED__ CURRENTLY HARDCODED

        prep_acc = prepAccounts(ledgerID, "Debit", amount, CurrentAsset = accounts.CurrentAsset, Currentliability = accounts.Currentliability)
        last_ca, CA_Balance, CA_BalanceDC = prep_acc["CurrentAsset"][0][0], prep_acc["CurrentAsset"][1][0],prep_acc["CurrentAsset"][2][0]
        last_cl, CL_Balance, CL_BalanceDC = prep_acc["Currentliability"][0][0], prep_acc["Currentliability"][1][0],prep_acc["Currentliability"][2][0]
        # prep_accs = results in a dicitonary {'Non Current Assset': [id, balance, BalanceDC]}

        if "Increase" in  increase_decrease: 
            debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount,  "CA" + str(last_ca+1), tag, asset_name, CA_Balance, CA_BalanceDC)
            if account_affected == "Cash": 
                creditEntry = accounts.CurrentAsset.credit(last_ca+1,ledgerID, transaction_date, amount,"CA" + str(last_ca), "Cash",  "Cash", CA_Balance, CA_BalanceDC)

            elif account_affected == "Cheque": 
                creditEntry = accounts.CurrentAsset.credit(last_ca+1,ledgerID, transaction_date, amount,"CA" + str(last_ca),'Cash Equivalents', "Cash Equivalents", CA_Balance, CA_BalanceDC)
            else: 
                BalanceDC = bal_debit_cred(current_user.ledgerID, amount, Currentliability = accounts.Currentliability)
                CL_BalanceDC = BalanceDC[0]

                debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount,  "CLiab" + str(last_cl), tag, asset_name, CA_Balance, CA_BalanceDC)
                creditEntry = accounts.Currentliability.credit(last_cl, ledgerID, transaction_date, loanPeriods, amount, "CA" + str(last_ca), "Accounts Payable", "Accounts Payable", CL_Balance, CL_BalanceDC)
        
        else: 
            creditEntry = accounts.CurrentAsset.credit(last_ca+1,ledgerID, transaction_date, amount, "CA" + str(last_ca),tag, asset_name, CA_Balance, CA_BalanceDC)
            if account_affected == "Cash": 
                debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount,"CA" + str(last_ca+1), "Cash", "Cash", CA_Balance, CA_BalanceDC)
            elif account_affected == "Cheque": 
                debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount,  "CA" + str(last_ca+1), "Cash Equivalents", "Cash Equivalents", CA_Balance, CA_BalanceDC)
            else: 
                debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount,  "CA" + str(last_ca+1), "Accounts Receivable", "Accounts Receivable", CA_Balance, CA_BalanceDC)
        try:
            db.session.add(debitEntry)
            db.session.add(creditEntry)
            db.session.commit()
        except Exception as e:
                error = str(e)
                print(error)
        return jsonify({'message': 'Transaction sucessfully added.'})   
        
    else: 
        error_list = form_errors(form)
        return jsonify(errors= error_list)

# WHats left: Depreciation Amortization Intangible Tangible 
@accounting.route('/api/transaction/<busID>/noncurrentasset', methods = ["POST", "GET"])
@login_required
@requires_auth
def nca_transaction(busID):
    if request.method == "POST":
        if request.form['form_id'] == "AddNCAForm":
            form = NCAForm(request.form)
                # rEMEMEMEBER TO VALIDATE THE FORM 
            asset_name = form.asset_name.data 
            transaction_date = form.transaction_date.data 
            dep_type = form.dep_type.data
            asset_desc = form.asset_desc.data 
            amount = float(form.amount.data)
            account_affected = form.paid_using.data
            lifeSpan = int(form.asset_lifespan.data)
            dueDate = form.due_date.data 
            totalUnits = 1
            salvageVal = float(form.salvage_val.data )
            remainingLife = 1  #form.remainingLife.data  #calculate remaining life from lifeSpan
            bought_sold = form.bought_sold.data
            tag= form.tag.data
            ledgerID =findLedger(busID, 2021)
            """ How to deal with INTANGIBLE ASSETS """
            # CHANGE TRANSACTION DATE TO DUE DATE

            # Calculate Net Asset by subtracting Depreciation from Asset at Cost 
            assetCost = amount - accounts.NonCurrentAsset.calcDepExpense(dep_type, amount, lifeSpan, totalUnits, salvageVal, remainingLife)

            # Get Last Account ID, Balance, Label Balance
            prep_acc = prepAccounts(ledgerID, "Debit", amount, NonCurrentAsset = accounts.NonCurrentAsset, CurrentAsset = accounts.CurrentAsset,
                                                                Currentliability = accounts.Currentliability)
            last_ca, CA_Balance, CA_BalanceDC = prep_acc["CurrentAsset"][0][0], prep_acc["CurrentAsset"][1][0],prep_acc["CurrentAsset"][2][0]
            last_cl, CL_Balance, CL_BalanceDC = prep_acc["Currentliability"][0][0], prep_acc["Currentliability"][1][0],prep_acc["Currentliability"][2][0]
            last_nca, NCA_Balance, NCA_BalanceDC = prep_acc["NonCurrentAsset"][0][0], prep_acc["NonCurrentAsset"][1][0],prep_acc["NonCurrentAsset"][2][0]
            
            if "Bought" in  bought_sold: 
                debitEntry = accounts.NonCurrentAsset.debit(last_nca, ledgerID, transaction_date, assetCost,lifeSpan, dep_type, "CA" + str(last_ca), tag, asset_name, NCA_Balance, NCA_BalanceDC)
                if account_affected == "Cash": 
                    creditEntry = accounts.CurrentAsset.credit(last_ca, ledgerID, transaction_date, assetCost, "NCA" + str(last_nca), "Cash", "Cash", CA_Balance, CA_BalanceDC)

                elif account_affected == "Cheque": 
                    creditEntry = accounts.CurrentAsset.credit(last_ca,ledgerID, transaction_date, assetCost,"NCA" + str(last_nca), "Cash Equivalents","Cash Equivalents", CA_Balance, CA_BalanceDC)

                else: 

                    debitEntry = accounts.NonCurrentAsset.debit(last_nca, ledgerID, transaction_date, assetCost,lifeSpan, dep_type, "CLiab" + str(last_cl), tag, asset_name, NCA_Balance, NCA_BalanceDC)
                    creditEntry = accounts.Currentliability.credit(last_cl, ledgerID, transaction_date, loan_periods, amount,"NCA" + str(last_nca), "Accounts Payable" ,"Accounts Payable", CL_Balance, CL_BalanceDC)
            else: 
                creditEntry = accounts.NonCurrentAsset.credit(last_nca,ledgerID, transaction_date, assetCost,lifeSpan, dep_type,"CA" +str(last_ca),tag, asset_name, NCA_Balance, NCA_BalanceDC)
                if account_affected == "Cash": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, ledgerID, transaction_date, assetCost,  "NCA" + str(last_nca),"Cash","Cash", CA_Balance, CA_BalanceDC)
                    
                elif account_affected == "Cheque": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, assetCost,  "NCA" + str(last_nca), "Cash Equivalents","Cash Equivalents", CA_Balance, CA_BalanceDC) 
                else: 
                    debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, assetCost, "NCA" + str(last_nca),"Accounts Receivable", "Accounts Receivable", CA_Balance, CA_BalanceDC)
                    
            try:
                db.session.add(debitEntry)
                db.session.add(creditEntry)
                db.session.commit()
            except Exception as e:
                    error = str(e)
                    print(error)

            return jsonify({'message': 'Transaction sucessfully added.'})                   
        else: 
            jsonify({'message': 'Form does not match - Select Non Current Asset Form'})    
    else: 
        error_list = form_errors(form)
        return jsonify(errors= error_list)

        
@accounting.route('/api/transaction/<busID>/currentliability', methods = ["POST", "GET"])
@login_required
@requires_auth
def cl_transaction(busID):
    if request.method == "POST": 
        form = CLiabForm(request.form)
        liab_name = form.liab_name.data
        person_owed = form.person_owed.data 
        loan_rate = form.loan_rate.data 
        loan_periods = form.loan_periods.data 
        borrow_date = form.borrow_date.data 
        payment_start_date = form.payment_start_date.data 
        amount_borrowed = float(form.amount_borrowed.data )
        account_affected = form.account_affected.data
        increase_decrease = form.increase_decrease.data
        tag = form.tag.data
        ledgerID =findLedger(busID, 2021)
        # new year = datetime.strptime(borrow_date, "%Y-%m-%d").year + loan_periods

        # Get Last Account ID, Balance, Label Balance
        prep_acc = prepAccounts(ledgerID, "Credit", amount_borrowed, CurrentAsset = accounts.CurrentAsset, Currentliability = accounts.Currentliability)
        last_ca, CA_Balance, CA_BalanceDC = prep_acc["CurrentAsset"][0][0], prep_acc["CurrentAsset"][1][0],prep_acc["CurrentAsset"][2][0]
        last_cl, CL_Balance, CL_BalanceDC = prep_acc["Currentliability"][0][0], prep_acc["Currentliability"][1][0],prep_acc["Currentliability"][2][0]
    
                            
        if "Increase" in increase_decrease: 
            creditEntry = accounts.Currentliability.credit(last_cl, ledgerID, borrow_date, loan_periods, amount_borrowed, "CA" +str (last_ca), tag, liab_name, CL_Balance, CL_BalanceDC)
            if account_affected == "Cash": 
                debitEntry = accounts.CurrentAsset.debit(last_ca, ledgerID, borrow_date, amount_borrowed,  "CL" +str(last_cl), "Cash", "Cash", CA_Balance, CA_BalanceDC)
            else:
                debitEntry = accounts.CurrentAsset.debit(last_ca,  ledgerID, borrow_date, amount_borrowed,  "CL" +str(last_cl), "Cash Equivalents", "Cash Equivalents", CA_Balance, CA_BalanceDC)
                
        else: 
            debitEntry = accounts.Currentliability.debit(last_cl, ledgerID, borrow_date, loan_periods, amount_borrowed,  "CA" +str(last_ca), tag, liab_name, CL_Balance, CL_BalanceDC)
            if account_affected == "Cash": 
                creditEntry = accounts.CurrentAsset.credit(last_ca, ledgerID, borrow_date, amount_borrowed, "CL" +str(last_cl),"Cash", "Cash", CA_Balance, CA_BalanceDC)
            else:
                creditEntry = accounts.CurrentAsset.credit(last_ca, ledgerID, borrow_date, amount_borrowed, "CL" +str(last_cl), "Cash Equivalents", "Cash Equivalents", CA_Balance, CA_BalanceDC)
        try:
            db.session.add(debitEntry)
            db.session.add(creditEntry)
            db.session.commit()
        except Exception as e:
            error = str(e)
            print(error)
        return jsonify({'message': 'Transaction sucessfully added.'}) 
    else:
        error_list = form_errors(form)
        return jsonify(errors= error_list)   

@accounting.route('/api/transaction/<busID>/ltliability', methods = ["POST", "GET"])
@login_required
@requires_auth
def lt_transaction(busID):
    if request.method == "POST": 
        if request['form_id'] == "LTLiabForm":
            form = LTLiabForm(request.form)
            
            liab_name = form.liab_name.data
            person_owed = form.person_owed.data 
            loan_rate = form.loan_rate.data 
            loan_periods = form.loan_periods.data 
            borrow_date = form.borrow_date.data 
            payment_start_date = form.payment_start_date.data 
            amount_borrowed = float(form.amount_borrowed.data )
            account_affected = form.account_affected.data
            increase_decrease = form.increase_decrease.data
            tag = form.tag.data
            ledgerID =findLedger(busID, 2021) 

            # CHANGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE CABALCNE TO LTBALANCE
            
            # new year = datetime.strptime(borrow_date, "%Y-%m-%d").year + loan_periods
            # Get Last Account ID, Balance, Label Balance
            prep_acc = prepAccounts(ledgerID, "Credit", amount_borrowed, CurrentAsset = accounts.CurrentAsset, Currentliability = accounts.Currentliability)
            last_ca, CA_Balance, CA_BalanceDC = prep_acc["CurrentAsset"][0][0], prep_acc["CurrentAsset"][1][0],prep_acc["CurrentAsset"][2][0]
            last_cl, CL_Balance, CL_BalanceDC = prep_acc["Currentliability"][0][0], prep_acc["Currentliability"][1][0],prep_acc["Currentliability"][2][0]
             # prep_accs = results in a dicitonary {'Non Current Assset': [id, balance, BalanceDC]}
                                                        
            if "Increase" in increase_decrease: 
                creditEntry = accounts.Currentliability.credit(last_cl, ledgerID, borrow_date, loan_periods, amount_borrowed, "CA" +str (last_ca), tag, liab_name, CL_Balance, CL_BalanceDC)
                if account_affected == "Cash": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, ledgerID, borrow_date, amount_borrowed,  "CL" +str(last_cl), "Cash", "Cash", CA_Balance, CA_BalanceDC)
                else:
                    debitEntry = accounts.CurrentAsset.debit(last_ca,  ledgerID, borrow_date, amount_borrowed,  "CL" +str(last_cl), "Cash Equivalents", "Cash Equivalents", CA_Balance, CA_BalanceDC)
                    
            else: 
                debitEntry = accounts.Currentliability.debit(last_cl, ledgerID, borrow_date, loan_periods, amount_borrowed,  "CA" +str(last_ca), tag, liab_name, CL_Balance, CL_BalanceDC)
                if account_affected == "Cash": 
                    creditEntry = accounts.CurrentAsset.credit(last_ca, ledgerID, borrow_date, amount_borrowed, "CL" +str(last_cl),"Cash", "Cash", CA_Balance, CA_BalanceDC)
                else:
                    creditEntry = accounts.CurrentAsset.credit(last_ca, ledgerID, borrow_date, amount_borrowed, "CL" +str(last_cl), "Cash Equivalents", "Cash Equivalents", CA_Balance, CA_BalanceDC)
            try:
                db.session.add(debitEntry)
                db.session.add(creditEntry)
                db.session.commit()
            except Exception as e:
                error = str(e)
                print(error)
            return jsonify({'message': 'Transaction sucessfully added.'}) 
        else:
            error_list = form_errors(form)
            return jsonify(errors= error_list)   
            

@accounting.route('/api/transaction/<busID>/expense', methods = ["POST", "GET"])
@login_required
@requires_auth
def exp_transaction(busID):
    if request.method == "POST": 
        form = ExpForm(request.form)

        expense_name = form.expense_name.data
        transaction_date = form.transaction_date.data 
        expense_category = form.expense_type.data
        expense_desc = form.expense_desc.data 
        amount = float(form.amount.data)
        account_affected = form.paid_using.data
        increase_decrease = form.increase_decrease.data
        tag= form.tag.data
        ledgerID =findLedger(busID, 2021)
        
        # Get Last Account ID, Balance, Label Balance
        prep_acc = prepAccounts(ledgerID, "Credit", amount, CurrentAsset = accounts.CurrentAsset, OperatingExpense = accounts.OperatingExpense,
                                NonOperatingExpense = accounts.NonOperatingExpense)
        last_ca, CA_Balance, CA_BalanceDC = prep_acc["CurrentAsset"][0][0], prep_acc["CurrentAsset"][1][0],prep_acc["CurrentAsset"][2][0]
        last_opex,  OE_Balance, OE_BalanceDC = prep_acc["OperatingExpense"][0][0], prep_acc["OperatingExpense"][1][0],prep_acc["OperatingExpense"][2][0]
        last_nOpex, nOE_Balance, nOE_BalanceDC = prep_acc["NonOperatingExpense"][0][0], prep_acc["NonOperatingExpense"][1][0],prep_acc["NonOperatingExpense"][2][0]
    
        if "Operating" in  expense_category: 
            # use Operating classess.. 
            if "Increase" in increase_decrease: 
                debitEntry = accounts.OperatingExpense.debit(last_opex, ledgerID, transaction_date, expense_category, amount,  "CA" + str(last_ca), tag, expense_name, OE_Balance, OE_BalanceDC)
                if account_affected == "Cash": 
                    creditEntry = accounts.CurrentAsset.credit(last_ca, ledgerID, transaction_date, amount, "OE" + str(last_opex), tag,"Cash", CA_Balance, CA_BalanceDC)
                else: 
                    creditEntry = accounts.CurrentAsset.credit(last_ca,ledgerID, transaction_date, amount, "OE" + str(last_opex), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC)
            else: 
                creditEntry = accounts.OperatingExpense.credit(last_opex, ledgerID, transaction_date, expense_category, amount,   "CA" + str(last_ca), tag, expense_name, OE_Balance, OE_BalanceDC)
                if account_affected == "Cash": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount,  "OE" + str(last_opex),"Cash", "Cash", CA_Balance, CA_BalanceDC)
                else:                        
                    debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount,  "OE" + str(last_opex), "Cash Equivalents","Cash Equivalents", CA_Balance, CA_BalanceDC)
            try:
                db.session.add(debitEntry)
                db.session.add(creditEntry)
                db.session.commit()
            except Exception as e:
                error = str(e)
                print(error)
            return jsonify({'message': 'Transaction sucessfully added.'})  
        else: 
            # use non operating expense class 
            if "Increase" in increase_decrease: 
                debitEntry = accounts.NonOperatingExpense.debit(last_nOpex,ledgerID, transaction_date, amount,   "CA" + str(last_ca),tag, expense_name, nOE_Balance, nOE_BalanceDC)
                if account_affected == "Cash": 
                    creditEntry = accounts.CurrentAsset.credit(last_ca,ledgerID, transaction_date, amount, "NOE" + str(last_nOpex), "Cash", "Cash", CA_Balance, CA_BalanceDC)
                else: 
                    creditEntry = accounts.CurrentAsset.credit(last_ca,ledgerID, transaction_date, amount, "NOE" + str(last_nOpex), "Cash Equivalents","Cash Equivalents", CA_Balance, CA_BalanceDC) 
            else: 
                creditEntry = accounts.NonOperatingExpense.credit(last_nOpex, ledgerID, transaction_date, expense_category, amount,  "CA" + str(last_ca), tag, expense_name, nOE_Balance, nOE_BalanceDC)
                if account_affected == "Cash": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount, "NOE" + str(last_nOpex), "Cash","Cash", CA_Balance, CA_BalanceDC)
                else:
                    debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount, "NOE" + str(last_nOpex), "Cash Equivalents","Cash Equivalents", CA_Balance, CA_BalanceDC)
            try:
                db.session.add(debitEntry)
                db.session.add(creditEntry)
                db.session.commit()
            except Exception as e:
                error = str(e)
                print(error)
            return jsonify({'message': 'Transaction sucessfully added.'})  

    else: 
        error_list = form_errors(form)
        return jsonify(errors= error_list)

@accounting.route('/api/transaction/<busID>/revenue', methods = ["POST", "GET"])
@login_required
@requires_auth
def rev_transaction(busID):
    if request.method == "POST": 
        form = RevForm(request.form)
        revenue_name = form.revenue_name.data 
        revenue_type = form.revenue_type.data
        transaction_date = form.transaction_date.data
        revenue_desc = form.revenue_desc.data
        amount = float(form.amount.data )
        account_affected = form.paid_using.data   
        increase_decrease = form.increase_decrease.data    
        tag = form.tag.data
        ledgerID =findLedger(busID, 2021)

        # Get Last Account ID, Balance, Label Balance
        prep_acc = prepAccounts(ledgerID, "Credit", amount, CurrentAsset = accounts.CurrentAsset, OperatingRevenue = accounts.OperatingRevenue,
                                NonOperatingRevenue= accounts.NonOperatingRevenue)
        last_ca, CA_Balance, CA_BalanceDC = prep_acc["CurrentAsset"][0][0], prep_acc["CurrentAsset"][1][0],prep_acc["CurrentAsset"][2][0]
        last_opRevenueID,  OR_Balance, OE_BalanceDC = prep_acc["OperatingRevenue"][0][0], prep_acc["OperatingRevenue"][1][0],prep_acc["OperatingRevenue"][2][0]
        last_nopRevenueID, nOR_Balance, nOR_BalanceDC = prep_acc["NonOperatingRevenue"][0][0], prep_acc["NonOperatingRevenue"][1][0],prep_acc["NonOperatingRevenue"][2][0]
    
        if "Operating" in  revenue_type: 
            # use Operating classess.. 
            if "Increase" in increase_decrease: 
                # increase operating revenue
                creditEntry = accounts.OperatingRevenue.credit(last_opRevenueID, ledgerID, transaction_date,  amount, "CA" + str(last_ca), tag, revenue_name, OR_Balance, OR_BalanceDC)
                if account_affected == "Cash":                         
                    debitEntry = accounts.CurrentAsset.debit(last_ca, ledgerID, transaction_date,  amount,"OR" + str(last_opRevenueID), "Cash", "Cash", CA_Balance, CA_BalanceDC)
                else: 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, ledgerID, transaction_date,  amount,"OR" + str(last_opRevenueID), "Cash Equivalents","Cash Equivalents", CA_Balance, CA_BalanceDC)
            else: 
                # decrease operating revenue
                debitEntry = accounts.OperatingRevenue.debit(last_opRevenueID, ledgerID, transaction_date,  amount, "CA" + str(last_ca), tag,revenue_name, OR_Balance, OR_BalanceDC)
                if account_affected == "Cash": 
                    creditEntry = accounts.CurrentAsset.credit(last_ca, ledgerID, transaction_date,  amount,"OR" + str(last_opRevenueID),"Cash", "Cash", CA_Balance, CA_BalanceDC)
                else:
                    creditEntry = accounts.CurrentAsset.credit(last_ca, ledgerID, transaction_date,  amount, "OR" + str(last_opRevenueID), "Cash Equivalents","Cash Equivalents", CA_Balance, CA_BalanceDC)
        
            try:
                db.session.add(debitEntry)
                db.session.add(creditEntry)
                db.session.commit()
            except Exception as e:
                error = str(e)
                print(error)
            return jsonify({'message': 'Transaction sucessfully added.'})  
        else: 
            # use non operating revenue class 
            if "Increase" in increase_decrease: 
                creditEntry = accounts.NonOperatingRevenue.credit(last_nopRevenueID,"CA" + str(last_ca), tag, revenue_name , nOR_Balance, nOR_BalanceDC)
                if account_affected == "Cash": 
                    debitEntry =  accounts.CurrentAsset.debit(last_ca, ledgerID, transaction_date, amount,"NOR" + str(last_nopRevenueID), tag, "Cash", CA_Balance, CA_BalanceDC)
                else: 
                    debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount, "NOR" + str(last_nopRevenueID), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC)
            else: 
                # decrease non operating revenue
                debitEntry = accounts.NonOperatingRevenue.debit(last_nopRevenueID,"CA" + str(last_ca), tag, revenue_name, nOR_Balance, nOR_BalanceDC, transaction_inputs)
                if account_affected == "Cash": 
                    creditEntry = accounts.CurrentAsset.credit(last_ca, ledgerID, transaction_date, amount, lifeSpan,"NOR" + str(last_nopRevenueID),tag, "Cash", CA_Balance, CA_BalanceDC)
                else:                        
                    creditEntry = accounts.CurrentAsset.credit(last_ca, ledgerID, transaction_date, amount,"NOR" + str(last_nopRevenueID), tag, "Cash Equivalents", CA_Balance, CA_BalanceDC)
            
            try:
                db.session.add(debitEntry)
                db.session.add(creditEntry)
                db.session.commit()
            except Exception as e:
                error = str(e)
                print(error)
            return jsonify({'message': 'Transaction sucessfully added.'})  

    else: 
        error_list = form_errors(form)
        return jsonify(errors= error_list)
        
@accounting.route('/api/transaction/<busID>/equity', methods = ["POST", "GET"])
@login_required
@requires_auth
def equity_transaction(busID):
    if request.method == "POST":             
        form = EquityForm(request.form)
        equity_name= form.equity_name.data
        transaction_date =form.transaction_date.data
        equity_desc = form.equity_desc.data
        amount = float(form.amount.data)
        account_affected = form.paid_using.data
        increase_decrease = form.increase_decrease.data
        tag = form.tag.data
        ledgerID =findLedger(busID, 2021)

        # Get Last Account ID, Balance, Label Balance
        prep_acc = prepAccounts(ledgerID, "Credit", amount, CurrentAsset = accounts.CurrentAsset, ShareholdersEquity = accounts.ShareholdersEquity)
        last_ca, CA_Balance, CA_BalanceDC = prep_acc["CurrentAsset"][0][0], prep_acc["CurrentAsset"][1][0],prep_acc["CurrentAsset"][2][0]
        last_equityID,  SE_Balance, SE_BalanceDC = prep_acc["ShareholdersEquity"][0][0], prep_acc["ShareholdersEquity"][1][0],prep_acc["ShareholdersEquity"][2][0]
    
        if "Increase" in increase_decrease: 
            # Increase in Capital
            creditEntry = accounts.ShareholdersEquity.credit(last_equityID,ledgerID, transaction_date, amount, "CA" + str(last_ca), tag, equity_name, SE_Balance, SE_BalanceDC)
            if account_affected == "Cash": 
                debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount, "SE" + str(last_equityID), "Cash", "Cash", CA_Balance, CA_BalanceDC)
            else:
                debitEntry = accounts.CurrentAsset.debit(last_ca,ledgerID, transaction_date, amount,"SE" + str(last_equityID), "Cash Equivalents", "Cash Equivalents", CA_Balance, CA_BalanceDC)
        else: 
            # Decrease in Capital
            debitEntry = accounts.ShareholdersEquity.debit(last_equityID,ledgerID, transaction_date, amount,"CA" + str(last_ca), tag, equity_name, SE_Balance, SE_BalanceDC)
            if account_affected == "Cash":
                creditEntry = accounts.CurrentAsset.credit(last_ca,ledgerID, transaction_date, amount,"SE" + str(last_equityID), "Cash", "Cash", CA_Balance, CA_BalanceDC)            
            else: 
                creditEntry = accounts.CurrentAsset.credit(last_ca,ledgerID, transaction_date, amount,"SE" + str(last_equityID), "Cash Equivalents", "Cash Equivalents", CA_Balance, CA_BalanceDC)
                
        try:
            db.session.add(debitEntry)
            db.session.add(creditEntry)
            db.session.commit()
        except Exception as e:
            error = str(e)
            print(error)
        return jsonify({'message': 'Transaction sucessfully added.'}) 
    else: 
        error_list = form_errors(form)
        return jsonify(errors= error_list)
  

def list_accounts(ledgerID, *args, **kwargs): 
    output = {}
    for key, value in kwargs.items(): 
        all_accounts = db.session.query(value).filter_by(ledgerID =ledgerID).all()
        output[key] = all_accounts
    return output


@accounting.route('/api/transactions/<busID>/', methods = ["GET", "POST"])
def get_all_accounts(busID): 
    ledgerID =findLedger(busID, 2021)

    all_accounts = list_accounts(ledgerID, CurrentAsset = accounts.CurrentAsset, NonCurrentAsset = accounts.NonCurrentAsset, 
                 Currentliability = accounts.Currentliability, Longtermliability = accounts.Longtermliability, 
                 OperatingRevenue = accounts.OperatingRevenue, NonOperatingRevenue = accounts.NonOperatingRevenue, 
                 OperatingExpense = accounts.OperatingExpense, NonOperatingExpense = accounts.NonOperatingExpense,  
                 ShareholdersEquity = accounts.ShareholdersEquity)
    
    def load_Accounts(**account_entries):
        final_list = []
        for key,value in account_entries.items(): 
            if value is not None or value != []: 
                for entry in value: 
                    balance = (entry.debitBalance if entry.debitBalance is not None else entry.creditBalance)
                    if key == "NonCurrentAsset":
                        final_list.append({'date': entry.acquisDATE, 'transaction_id': 'NCA' + str(entry.id),
                                           'transaction_name': entry.assetName, 'related_entry': entry.related_entry, 'amount': balance,'actions': 'true' })
                    elif  key == "CurrentAsset":
                        final_list.append({'date': entry.acquisDATE, 'transaction_id': 'CA' + str(entry.id),'transaction_name': entry.assetName, 'related_entry': entry.related_entry, 'amount': balance,'actions': 'true' })
                    elif key == "Currentliability":
                        final_list.append({'date': entry.borwDATE, 'transaction_id': 'CL'+ str(entry.id), 'transaction_name': entry.liabName, 'related_entry':entry.related_entry,'amount': balance, 'actions': 'true'})
                    elif key == "Longtermliability":
                        final_list.append({'date': entry.borwDATE, 'transaction_id': 'LT'  +str(entry.id), 'transaction_name': entry.liabName, 'related_entry':entry.related_entry,'amount': balance, 'actions': 'true'})
                    elif key == "OperatingRevenue":
                        final_list.append({'date': entry.dateEarned, 'transaction_id': 'OR'+ str(entry.id), 'transaction_name':entry.oprevName, 'related_entry': entry.related_entry, 'amount':balance, 'actions': 'true'})
                    elif key == "NonOperatingRevenue":
                        final_list.append({'date': entry.dateEarned, 'transaction_id': 'NOR' +str(entry.id), 'transaction_name':entry.nOprevName, 'related_entry': entry.related_entry, 'amount':balance,'actions': 'true'})
                    elif key == "OperatingExpense":
                        final_list.append({'date': entry.dateIncurred, 'transaction_id': 'OE' + str(entry.id), 'transaction_name':entry.opexName, 'related_entry': entry.related_entry,'amount': balance,'actions': 'true'})
                    else:
                        final_list.append({'date': entry.dateIncurred, 'transaction_id': 'NOE' + str(entry.id), 'transaction_name':entry.nOpexName, 'related_entry': entry.related_entry, 'amount':balance,'actions': 'true'})
            else: 
                print(value)
        return final_list
                
    
    all_transactions = load_Accounts(CurrentAsset = all_accounts["CurrentAsset"], NonCurrentAsset = all_accounts["NonCurrentAsset"], Currentliability = all_accounts["Currentliability"], 
                    Longtermliability = all_accounts["Longtermliability"], OperatingRevenue = all_accounts["OperatingRevenue"], NonOperatingRevenue = all_accounts["NonOperatingRevenue"], 
                    OperatingExpense = all_accounts["OperatingExpense"], NonOperatingExpense = all_accounts["NonOperatingExpense"], ShareholdersEquity = all_accounts["ShareholdersEquity"])
    return jsonify({'transaction': all_transactions})
    
