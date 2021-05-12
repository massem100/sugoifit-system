import os, sys
import secrets
import hashlib, random
from functools import wraps
from datetime import datetime, timedelta

# WTF Forms and SQLAlchemy Models
from app.forms import RegisterForm, LoginForm, NCAForm, websiteForm,orderForm, LTLiabForm, CAForm,ExpForm, RevForm, EquityForm
from app.model import  accounts, auth, sales, transactions
from app.model.financial_statement import Financialstmt, Financialstmtline, Financialstmtlineseq, \
                                          Financialstmtlinealia,Financialstmtdesc 
from sqlalchemy import func, inspection, event
from sqlalchemy.inspection import inspect

from flask import request, jsonify, flash, session, _request_ctx_stack, g
from werkzeug.utils import secure_filename

from flask import Blueprint, current_app
from app import db, login_manager, principal, csrf_
from app.auth.routes import requires_auth

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
                   
def account_balances(busID, *args,**accounts): 
    account_bal = []
    for key, value in accounts.items(): 
        balance = db.session.query(value).filter_by(busID = busID).order_by(value.id.desc()).first()
        balance = (float(balance.Balance) if balance is not None else 0)
        account_bal.append(balance)
    return account_bal

def get_last_id(busID, *args,**accounts): 
    id_lst = []
    for key, value in accounts.items(): 
        last_id = db.session.query(value).filter_by(busID = busID).order_by(value.id.desc()).first()
        last_id = (int(last_id.id)+1 if last_id is not None else 1)
        id_lst.append(last_id)
    return id_lst


def bal_debit_cred(busID, amount, label, *args, **balances): 
    debit_cred = []
    for key, value in balances.items(): 
        total_sum =  value.query.with_entities(
                                                func.coalesce(func.sum(value.debitBalance),0).label("totalDebit"),
                                                func.coalesce(func.sum(value.creditBalance),0).label("totalCredit")
                                              ).filter_by(busID= busID).first()
        if label == "Debit": 
            BalanceDC = ("Debit" if float(total_sum.totalDebit) + amount > float(total_sum.totalCredit) else "Credit")
        elif label == "Credit": 
            BalanceDC = ("Debit" if float(total_sum.totalDebit) > float(total_sum.totalCredit) + amount else "Credit")
        else: 
            BalanceDC = natural_balances[key]
        debit_cred.append(BalanceDC)
    return debit_cred 


@accounting.route('/api/transaction/currentasset', methods = ["POST", "GET"])
@login_required
@requires_auth
def ca_transaction():
    if request.method == "POST": 
        if request['form_id'] == "AddCAForm":
            form = CAForm(request.form)
            asset_name = form.asset_name.data 
            transaction_date = form.transaction_date.data 
            asset_desc = form.asset_desc.data 
            amount = float(form.amount.data)
            account_affected = form.paid_using.data
            increase_decrease = form.increase_decrease.data
            
            transaction_inputs = [current_user.busID, lifeSpan, dep_type, transaction_date, amount]
            tag="tag"

            # Get IDs for related_entry
            last_id = get_last_id(CurrentAsset = accounts.CurrentAsset, Currentliability = accounts.currentliability)
            last_ca, last_cl = last_id[0], last_id[1]

            # Get the balances of Accounts 
            balances = account_balances(NonCurrentAsset =  accounts.NonCurrentAsset, CurrentAsset = accounts.CurrentAsset,
                                        Currentliability =accounts.Currentliability)
            NCA_Balance, CA_Balance, CL_Balance = balances[0], balances[1], balances[2]

            BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)
            CA_BalanceDC = BalanceDC[0]

            if "Increase" in  increase_decrease: 
                if account_affected == "Cash": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), tag, asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca+1,"CA" + str(last_ca), tag,  "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)

                elif account_affected == "Cheque": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), '', asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca+1,"CA" + str(last_ca),'cashequivalents', "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                else: 
                    BalanceDC = bal_debit_cred(amount, Currentliability = accounts.Currentliability)
                    CL_BalanceDC = BalanceDC[0]

                    debitEntry = accounts.CurrentAsset.debit(last_ca, "CLiab" + str(last_cl), tag, asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.Currentliability.credit(last_cl, "CA" + str(last_ca), tag, "Accounts Payable", CL_Balance, CL_BalanceDC, liability_inputs)
            
                try:
                    db.session.add(debitEntry)
                    db.session.add(creditEntry)
                    db.session.commit()
                except Exception as e:
                     error = str(e)
                     print(error)
                return jsonify({'message': 'Transaction sucessfully added.'})   
            else: 
                if account_affected == "Cash": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca+1,"CA" + str(last_ca),tag, asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                
                elif account_affected == "Cheque": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), tag, "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca+1,"CA" + str(last_ca), tag, asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                else: 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), tag, "Accounts Receivable", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca+1, "CA" + str(last_ca),tag,  asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                    
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

# WHats left: Depreciation Amortization Intangible Tangible 
@accounting.route('/api/transaction/noncurrentasset', methods = ["POST", "GET"])
@login_required
@requires_auth
def nca_transaction():
    if request.method == "POST":
        if request.form['form_id'] == "AddNCAForm":
            form = NCAForm(request.form)
                # rEMEMEMEBER TO VALIDATE THE FORM 
            asset_name = form.asset_name.data 
            transaction_date = form.transaction_date.data 
            dep_type = form.dep_type.data
            dep_rate = form.dep_rate.data
            asset_desc = form.asset_desc.data 
            amount = float(form.amount.data)
            account_affected = form.paid_using.data
            lifeSpan = form.asset_lifespan.data
            bought_sold = form.bought_sold.data
            # CHANGE TRANSACTION DATE TO DUE DATE
            transaction_inputs = [current_user.busID, lifeSpan, dep_type, transaction_date, amount]
            liability_inputs = [current_user.busID, transaction_date, transaction_date, amount]
            tag="tag"
         
            last_id = get_last_id(NonCurrentAsset = accounts.NonCurrentAsset, CurrentAsset = accounts.CurrentAsset,
                                    Currentliability = accounts.currentliability)
            last_nca, last_ca, last_cl = last_id[0], last_id[1], last_id[2]

            # Get the balances of Accounts 
            balances = account_balances(NonCurrentAsset = accounts.NonCurrentAsset, CurrentAsset = accounts.CurrentAsset,
                                        Currentliability = accounts.Currentliability)
            NCA_Balance, CA_Balance, CL_Balance = balances[0], balances[1], balances[2]

            BalanceDC = bal_debit_cred(amount, NonCurrentAsset = accounts.NonCurrentAsset, CurrentAsset = accounts.CurrentAsset)
            NCA_BalanceDC, CA_BalanceDC = BalanceDC[0], BalanceDC[1]
                                
            
            if "Bought" in  bought_sold: 
                if account_affected == "Cash": 
                    debitEntry = accounts.NonCurrentAsset.debit(last_nca,"CA" + str(last_ca), tag, asset_name, NCA_Balance, NCA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca,"NCA" + str(last_nca), tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)

                elif account_affected == "Cheque": 
                    debitEntry = accounts.NonCurrentAsset.debit(last_nca,"CA" + str(last_ca),tag, asset_name, CA_Balance, NCA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca,"NCA" + str(last_nca), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)

                else: 
                    BalanceDC = bal_debit_cred(amount, Currentliability = accounts.Currentliability)
                    CL_BalanceDC = BalanceDC[0]

                    debitEntry = accounts.NonCurrentAsset.debit(last_nca, "CLiab" + str(last_cl), tag, asset_name, NCA_Balance, NCA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.Currentliability.credit(last_cl, "NCA" + str(last_nca), tag,"Accounts Payable", CL_Balance, CL_BalanceDC, liability_inputs)

                try:
                    db.session.add(debitEntry)
                    db.session.add(creditEntry)
                    db.session.commit()
                except Exception as e:
                     error = str(e)
                     print(error)
                
                return jsonify({'message': 'Transaction sucessfully added.'})   

            else: 
                if account_affected == "Cash": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "NCA" + str(last_nca), tag,"Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.NonCurrentAsset.credit(last_nca,"CA" +str(last_ca),tag, asset_name, NCA_Balance, NCA_BalanceDC, transaction_inputs)

                elif account_affected == "Cheque": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "NCA" + str(last_nca), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.NonCurrentAsset.credit(last_nca,"CA" +str(last_ca),tag, asset_name, NCA_Balance, NCA_BalanceDC, transaction_inputs)

                else: 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "NCA" + str(last_nca),tag, "Accounts Receivable", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.NonCurrentAsset.credit(last_nca, "CA" + str(last_ca), tag,asset_name, NCA_Balance, NCA_BalanceDC, transaction_inputs)
                    
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

        
@accounting.route('/api/transaction/currentliability', methods = ["POST", "GET"])
@login_required
@requires_auth
def cl_transaction():
    if request.method == "POST": 
        form = CLiabForm(request.form)
        liab_name = form.liab_name.data
        person_owed = form.person_owed.data 
        loan_rate = form.loan_rate.data 
        loan_periods = form.loan_periods.data 
        borrow_date = form.borrow_date.data 
        payment_start_date = form.payment_start_date.data 
        amount_borrowed = form.amount_borrowed.data 
        account_affected = form.account_affected.data
        increase_decrease = form.increase_decrease.data
        
        transaction_inputs = [current_user.busID, transaction_date, transaction_date, amount]
        tag="tag"
        
        last_id = get_last_id(CurrentAsset = accounts.CurrentAsset, Currentliability = accounts.currentliability)
        last_ca, last_cl = last_id[0], last_id[1]

        # Get the balances of Accounts 
        balances = account_balances(CurrentAsset = accounts.CurrentAsset, Currentliability = accounts.Currentliability)
        CA_Balance, CL_Balance = balances[0], balances[1]

        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset,Currentliability = accounts.Currentliability)
        CA_BalanceDC, CL_BalanceDC = BalanceDC[0], BalanceDC[1]
                            
        if "Increase" in increase_decrease: 
            if account_affected == "Cash": 
                debitEntry = accounts.CurrentAsset.debit(last_ca, "CL" +str(last_cl), tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                creditEntry = accounts.Currentliability.credit(last_cl, "CA" +str (last_ca), tag, liab_name, CL_Balance, CL_BalanceDC, transaction_inputs)
            else:
                debitEntry = accounts.CurrentAsset.debit(last_ca, "CL" +str(last_cl), tag, "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                creditEntry = accounts.Currentliability.credit(last_cl, "CA" +str (last_ca), tag, liab_name, CL_Balance, CL_BalanceDC, transaction_inputs)
            try:
                db.session.add(debitEntry)
                db.session.add(creditEntry)
                db.session.commit()
            except Exception as e:
                error = str(e)
                print(error)
            return jsonify({'message': 'Transaction sucessfully added.'}) 
        else: 
            if account_affected == "Cash": 
                debitEntry = accounts.Currentliability.debit(last_cl, "CA" +str(last_ca), tag, liab_name, CL_Balance, CL_BalanceDC, transaction_inputs)
                creditEntry = accounts.CurrentAsset.credit(last_ca, "CL" +str(last_cl), tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
            else:
                debitEntry = accounts.Currentliability.debit(last_cl, "CA" +str(last_ca), tag, liab_name, CL_Balance, CL_BalanceDC, transaction_inputs)
                creditEntry = accounts.CurrentAsset.credit(last_ca, "CL" +str(last_cl), tag, "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
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

@accounting.route('/api/transaction/ltliability', methods = ["POST", "GET"])
@login_required
@requires_auth
def lt_transaction():
    if request.method == "POST": 
        if request['form_id'] == "LTLiabForm":
            form = LTLiabForm(request.form)
            liab_name = form.liab_name.data
            person_owed = form.person_owed.data 
            loan_rate = form.loan_rate.data 
            loan_periods = form.loan_periods.data 
            borrow_date = form.borrow_date.data 
            payment_start_date = form.payment_start_date.data 
            amount_borrowed = form.amount_borrowed.data 
             # I need to calculate interest on long term loan 
            # How to handle the current portion of long term loan that should be paid out
            return 1
        

@accounting.route('/api/transaction/expense', methods = ["POST", "GET"])
@login_required
@requires_auth
def exp_transaction():
    if request.method == "POST": 
        form = ExpenseForm(request.form)

        expense_name = form.expense_name.data
        transaction_date = form.transaction_date.data 
        expense_type = form.expense_type.data
        expense_desc = form.expense_desc.data 
        amount = float(form.amount.data)
        account_affected = form.paid_using.data
        increase_decrease = form.increase_decrease.data

        tag ="tag"

        last_id = get_last_id(CurrentAsset = accounts.CurrentAsset, OperatingExpense = accounts.OperatingExpense,
                                NonOperatingExpense = accounts.NonOperatingExpense)
        last_ca, last_opex, last_nOpex = last_id[0], last_id[1], last_id[2]

        # Get the balances of Accounts 
        balances = account_balances(CurrentAsset = accounts.CurrentAsset, OperatingExpense = accounts.OperatingExpense,
                                    NonOperatingExpense=accounts.NonOperatingExpense)
        CA_Balance, OE_Balance, nOE_Balance = balances[0], balances[1], balances[2]

        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, OperatingExpense = accounts.OperatingExpense,
                                    NonOperatingExpense=accounts.NonOperatingExpense)
        CA_BalanceDC, OE_BalanceDC, nOE_BalanceDC = BalanceDC[0], BalanceDC[1], BalanceDC[2]

        if "Operating" in  expense_type: 
            # use Operating classess.. 
            if "Increase" in increase_decrease: 
                # increase operating expense
                if account_affected == "Cash": 
                    debitEntry = accounts.OperatingExpense.debit(last_opex, "CA" + str(last_ca), tag, expense_name, OE_Balance, OE_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca,"OE" + str(last_opex), tag,"Cash", CA_Balance, CA_BalanceDC, transaction_inputs)

                else: 
                    debitEntry = accounts.OperatingExpense.debit(last_opex, "CA" + str(last_ca),tag, expense_name, OE_Balance, OE_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca,"OE" + str(last_opex), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)

                # Add to db...
                try:
                    db.session.add(debitEntry)
                    db.session.add(creditEntry)
                    db.session.commit()
                except Exception as e:
                    error = str(e)
                    print(error)
                return jsonify({'message': 'Transaction sucessfully added.'}) 
            else: 
                # decrease operating expense
                if account_affected == "Cash": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca,"OE" + str(last_opex),tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.OperatingExpense.credit(last_opex, "CA" + str(last_ca), tag,expense_name, OE_Balance, OE_BalanceDC, transaction_inputs)
                
                else:                        
                    debitEntry = accounts.CurrentAsset.debit(last_ca,"OE" + str(last_opex), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.OperatingExpense.credit(last_opex, "CA" + str(last_ca),tag, expense_name, OE_Balance, OE_BalanceDC, transaction_inputs)
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
                # increase operating expense
                if account_affected == "Cash": 
                    debitEntry = accounts.NonOperatingExpense.debit(last_nOpex, "CA" + str(last_ca),tag, expense_name, nOE_Balance, nOE_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca,"NOE" + str(last_nOpex), tag,"Cash", CA_Balance, CA_BalanceDC, transaction_inputs)

                else: 
                    debitEntry = accounts.NonOperatingExpense.debit(last_nOpex, "CA" + str(last_ca), tag, expense_name, nOE_Balance, nOE_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca,"NOE" + str(last_nOpex), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)

                try:
                    db.session.add(debitEntry)
                    db.session.add(creditEntry)
                    db.session.commit()
                except Exception as e:
                    error = str(e)
                    print(error)
                return jsonify({'message': 'Transaction sucessfully added.'}) 
            else: 
                # decrease operating expense
                if account_affected == "Cash": 
                    debitEntry = accounts.CurrentAsset.debit(last_ca,"NOE" + str(last_nOpex), tag,"Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.NonOperatingExpense.credit(last_nOpex, "CA" + str(last_ca), tag, expense_name, nOE_Balance, nOE_BalanceDC, transaction_inputs)
                else:
                    debitEntry = accounts.CurrentAsset.debit(last_ca,"NOE" + str(last_nOpex), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.NonOperatingExpense.credit(last_nOpex, "CA" + str(last_ca), tag, expense_name, nOE_Balance, nOE_BalanceDC, transaction_inputs)
                
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

@accounting.route('/api/transaction/revenue', methods = ["POST", "GET"])
@login_required
@requires_auth
def rev_transaction():
    if request.method == "POST": 
        form = RevenueForm(request.form)
        revenue_name = form.revenue_name.data 
        revenue_type = form.revenue_type.data
        transaction_date = form.transaction_date.data
        revenue_desc = form.revenue_desc.data
        amount = form.amount.data 
        account_affected = form.paid_using.data   
        increase_decrease = form.increase_decrease.data    
        
        
        last_id = get_last_id(CurrentAsset = accounts.CurrentAsset, OperatingRevenue = accounts.OperatingRevenue,
                                NonOperatingRevenue= accounts.NonOperatingRevenue)
        last_ca, last_opRevenueID, last_nopRevenueID = last_id[0], last_id[1], last_id[2]

        # Get the balances of Accounts 
        balances = account_balances(CurrentAsset = accounts.CurrentAsset, OperatingRevenue= accounts.OperatingRevenue,
                                    NonOperatingRevenue=accounts.NonOperatingRevenue)
        CA_Balance, OR_Balance, nOR_Balance = balances[0], balances[1], balances[2]

        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, OperatingRevenue = accounts.OperatingRevenue,
                                    NonOperatingRevenue=accounts.NonOperatingRevenue)
        CA_BalanceDC, OR_BalanceDC, nOR_BalanceDC = BalanceDC[0], BalanceDC[1], BalanceDC[2]

        if "Operating" in  revenue_type: 
            # use Operating classess.. 
            if "Increase" in increase_decrease: 
                # increase operating revenue
                if account_affected == "Cash":                         
                    debitEntry = accounts.CurrentAsset.debit(last_ca,"OR" + str(last_opRevenueID), tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.OperatingRevenue.credit(last_opRevenueID, "CA" + str(last_ca), tag, revenue_name, OR_Balance, OR_BalanceDC, transaction_inputs)

                else: 
                    debitEntry = accounts.CurrentAsset.debit(last_ca,"OR" + str(last_opRevenueID), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.OperatingRevenue.credit(last_opRevenueID, "CA" + str(last_ca), tag, revenue_name, OR_Balance, OR_BalanceDC, transaction_inputs)
                try:
                    db.session.add(debitEntry)
                    db.session.add(creditEntry)
                    db.session.commit()
                except Exception as e:
                    error = str(e)
                    print(error)
                return jsonify({'message': 'Transaction sucessfully added.'}) 

            else: 
                # decrease operating revenue
                if account_affected == "Cash": 
                    
                    debitEntry = accounts.OperatingRevenue.debit(last_opRevenueID,"CA" + str(last_ca), tag,revenue_name, OR_Balance, OR_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca, "OR" + str(last_opRevenueID),tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                else:
                    debitEntry = accounts.OperatingRevenue.debit(last_opRevenueID,"CA" + str(last_ca), tag,revenue_name, OR_Balance, OR_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca, "OR" + str(last_opRevenueID), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
        
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
                # increase operating expense
                if account_affected == "Cash": 
                    debitEntry =  accounts.CurrentAsset.debit(last_ca, "NOR" + str(last_nopRevenueID), tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.NonOperatingRevenue.credit(last_nopRevenueID,"CA" + str(last_ca), tag, revenue_name , nOR_Balance, nOR_BalanceDC, transaction_inputs)

                else: 
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "NOR" + str(last_nopRevenueID), tag,"Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.NonOperatingRevenue.credit(last_nopRevenueID,"CA" + str(last_ca), tag, revenue_name, nOR_Balance, nOR_BalanceDC, transaction_inputs)

                try:
                    db.session.add(debitEntry)
                    db.session.add(creditEntry)
                    db.session.commit()
                except Exception as e:
                    error = str(e)
                    print(error)
                return jsonify({'message': 'Transaction sucessfully added.'}) 
            else: 
                # decrease non operating revenue
                if account_affected == "Cash": 
                    debitEntry = accounts.NonOperatingRevenue.debit(last_nopRevenueID,"CA" + str(last_ca), tag, revenue_name, nOR_Balance, nOR_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca, "NOR" + str(last_nopRevenueID),tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                else:                        
                    debitEntry = accounts.NonOperatingRevenue.debit(last_nopRevenueID, "CA" + str(last_ca), tag, revenue_name, nOR_Balance, nOR_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca, "NOR" + str(last_nopRevenueID), tag, "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
            
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
        
@accounting.route('/api/transaction/equity', methods = ["POST", "GET"])
@login_required
@requires_auth
def equity_transaction():
    if request.method == "POST":             
        form = EquityForm(request.form)
        equity_name= form_data.equity_name.data
        transaction_date =form_data.transaction_date.data
        equity_desc = form_data.equity_desc.data
        amount = float(form.amount.data)
        account_affected = form.paid_using.data
        increase_decrease = form.increase_decrease.data

        
        last_id = get_last_id(CurrentAsset = accounts.CurrentAsset, ShareholdersEquity = accounts.ShareholdersEquity)
        last_ca, last_equityID = last_id[0], last_id[1]

        # Get the balances of Accounts 
        balances = account_balances(CurrentAsset = accounts.CurrentAsset, ShareholdersEquity = accounts.ShareholdersEquity)
        CA_Balance, SE_Balance = balances[0], balances[1]

        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, ShareholdersEquity = accounts.ShareholdersEquity)
        CA_BalanceDC, SE_BalanceDC= BalanceDC[0], BalanceDC[1]

        if "Increase" in increase_decrease: 
            # Increase in Capital
            if account_affected == "Cash": 
                debitEntry = accounts.CurrentAsset.debit(last_ca,"SE" + str(last_equityID), tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                creditEntry = accounts.ShareholdersEquity.credit(last_equityID, "CA" + str(last_ca), tag, equity_name, SE_Balance, SE_BalanceDC, transaction_inputs)
 
            else:
                debitEntry = accounts.CurrentAsset.debit(last_ca,"SE" + str(last_equityID), tag, "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                creditEntry = accounts.ShareholdersEquity.credit(last_equityID, "CA" + str(last_ca), tag, equity_name, SE_Balance, SE_BalanceDC, transaction_inputs)
            try:
                db.session.add(debitEntry)
                db.session.add(creditEntry)
                db.session.commit()
            except Exception as e:
                error = str(e)
                print(error)
            return jsonify({'message': 'Transaction sucessfully added.'}) 

        else: 
            # Decrease in Capital
            if account_affected == "Cash": 
                debitEntry = accounts.ShareholdersEquity.debit(last_equityID, "CA" + str(last_ca), tag, equity_name, SE_Balance, SE_BalanceDC, transaction_inputs)
                creditEntry = accounts.CurrentAsset.credit(last_ca,"SE" + str(last_equityID), tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                
            else: 
                debitEntry = accounts.ShareholdersEquity.debit(last_equityID, "CA" + str(last_ca), tag, equity_name, SE_Balance, SE_BalanceDC, transaction_inputs)
                creditEntry = accounts.CurrentAsset.credit(last_ca,"SE" + str(last_equityID), tag, "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                
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


    
@accounting.route('/api/printstmtdata', methods= ["GET"])
def stmt():
    resultstmt = []
    financiatransaction_inputsmt = Financiatransaction_inputsmt.query.all()
    for stmt in financiatransaction_inputsmt:
        resultstmt.append({ 'id' :stmt.stmtID,'Statement Name': stmt.fs_name})

    return jsonify(response = [resultstmt])

