import os, sys
import secrets
import hashlib, random
from functools import wraps
from datetime import datetime, timedelta

# WTF Forms and SQLAlchemy Models
from app.forms import RegisterForm, LoginForm, NCAForm, websiteForm,orderForm, LTLiabForm, CAForm,ExpForm, RevForm
from app.model import  accounts, auth, sales, transactions
from app.model.financial_statement import Financialstmt, Financialstmtline, Financialstmtlineseq, \
                                          Financialstmtlinealia,Financialstmtdesc 
from sqlalchemy import func, inspection, event

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

def check(): 
    return "working"

"""
--------------------------------------- Financial Statement Routes ----------------------------------------------------------
"""

def account_balances(*args,**accounts): 
    account_bal = []
    for key, value in accounts.items(): 
        balance = db.session.query(value[0]).order_by(value[1].desc()).first()
        balance = (float(balance.Balance) if balance is not None else 0)
        account_bal.append(balance)
    return account_bal

# def get_last_id(*args,**accounts): 
#     ids = []
#     for key, value in accounts.items(): 
#         last_id = db.session.query(value[0]).order_by(value[1].desc()).first()
#         last_id = (float(balance.Balance) if balance is not None else 0)
#         account_bal.append(balance)
#     return ids
#     last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
#             last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)


def bal_debit_cred(amount, *args, **balances): 
    debit_cred = []
    for key, value in balances.items(): 
        debitSum =  value.query.with_entities(func.coalesce(func.sum(value.debitBalance), 0).label("totalDebit")).first()
        creditSum = value.query.with_entities(func.coalesce(func.sum(value.creditBalance), 0).label("totalCredit")).first()
        BalanceDC = ("Debit" if float(debitSum.totalDebit) > float(creditSum.totalCredit) else "Credit")
        debit_cred.append(BalanceDC)
    return debit_cred 

# WHats left: Depreciation Amortization Intangible Tangible 
@accounting.route('/api/transaction/currentasset', methods = ["POST", "GET"])
@login_required
@requires_auth
def ca_transaction():
    if request.method == "POST": 
        if request['form_id'] == "AddCAForm":
            form = CAForm(request.form)
            
            # Add form data
            asset_name = form.asset_name.data 
            transaction_date = form.transaction_date.data 
            asset_desc = form.asset_desc.data 
            amount = float(form.amount.data)
            account_affected = form.paid_using.data
            increase_decrease = form.increase_decrease.data
            
            transaction_inputs = [current_user.busID, lifeSpan, dep_type, transaction_date, amount]

            tag="tag"
            # Get ID of Non Current Asset to increment 
            last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
            last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

            # last_cl
            # Get ID of Non Current Asset to increment 
            last_clID = db.session.query(accounts.Currentliability).order_by(accounts.Currentliability.cliabID.desc()).first()
            last_cl = (int(last_clID.cliabID)+1 if last_clID is not None else 1)

            # Get the balances of Accounts 
            balances = account_balances(NonCurrentAsset =  [accounts.NonCurrentAsset, accounts.NonCurrentAsset.ncaID], 
                                        CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                        Currentliability =[accounts.Currentliability, accounts.Currentliability.cliabID])
            NCA_Balance, CA_Balance, CL_Balance = balances[0], balances[1], balances[2]
            if "Increase" in  increase_decrease: 
                if account_affected == "Cash": 

                    BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)
                    CA_BalanceDC = BalanceDC[0]
                    # credit entry is cASH

                    debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), tag, asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca+1,"CA" + str(last_ca), tag,  "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)

                elif account_affected == "Cheque": 
                    BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)
                    CA_BalanceDC = BalanceDC[0]
                    # credit entry is cheque
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), tag, asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca+1,"CA" + str(last_ca),tag, "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                else: 

                    BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, 
                                                       Currentliability = accounts.Currentliability)
                    CA_BalanceDC, CL_BalanceDC = BalanceDC[0], BalanceDC[1]

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
                    BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)             
                    CA_BalanceDC = BalanceDC[0]

                    debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), tag, "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca+1,"CA" + str(last_ca),tag, asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                elif account_affected == "Cheque": 
                    BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)             
                    CA_BalanceDC = BalanceDC[0]

                    debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), tag, "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca+1,"CA" + str(last_ca), tag, asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                else: 
                    BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)
                    CA_BalanceDC = BalanceDC[0]
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
            
            # Get ID of Non Current Asset to increment 
            last_ncaID = db.session.query(accounts.NonCurrentAsset).order_by(accounts.NonCurrentAsset.ncaID.desc()).first()
            last_nca = (int(last_ncaID.ncaID)+1 if last_ncaID is not None else 1)

            # Get ID of Non Current Asset to increment 
            last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
            last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

            # last_cl
            # Get ID of Non Current Asset to increment 
            last_clID = db.session.query(accounts.Currentliability).order_by(accounts.Currentliability.cliabID.desc()).first()
            last_cl = (int(last_clID.cliabID)+1 if last_clID is not None else 1)

            # Get the balances of Accounts 
            balances = account_balances(NonCurrentAsset =  [accounts.NonCurrentAsset, accounts.NonCurrentAsset.ncaID], 
                                        CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                        Currentliability =[accounts.Currentliability, accounts.Currentliability.cliabID])
            NCA_Balance, CA_Balance, CL_Balance = balances[0], balances[1], balances[2]
                                
            
            if "Bought" in  bought_sold: 
                if account_affected == "Cash": 
                    BalanceDC = bal_debit_cred(amount, NonCurrentAsset = accounts.NonCurrentAsset, 
                                                       CurrentAsset = accounts.CurrentAsset)
                    NCA_BalanceDC, CA_BalanceDC = BalanceDC[0], BalanceDC[1]
                    
                    debitEntry = accounts.NonCurrentAsset.debit(last_nca,"CA" + str(last_ca), asset_name, NCA_Balance, NCA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca,"NCA" + str(last_nca), "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)

                elif account_affected == "Cheque": 
                    BalanceDC = bal_debit_cred(amount, NonCurrentAsset = accounts.NonCurrentAsset, 
                                                       CurrentAsset = accounts.CurrentAsset)
                    NCA_BalanceDC, CA_BalanceDC = BalanceDC[0], BalanceDC[1]

                    debitEntry = accounts.NonCurrentAsset.debit(last_nca,"CA" + str(last_ca), asset_name, CA_Balance, NCA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.CurrentAsset.credit(last_ca,"NCA" + str(last_nca), "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)

                else: 
                    BalanceDC = bal_debit_cred(amount, NonCurrentAsset = accounts.NonCurrentAsset, 
                                                       Currentliability = accounts.Currentliability)
                    NCA_BalanceDC, CL_BalanceDC = BalanceDC[0], BalanceDC[1]

                    debitEntry = accounts.NonCurrentAsset.debit(last_nca, "CLiab" + str(last_cl), asset_name, NCA_Balance, NCA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.Currentliability.credit(last_cl, "NCA" + str(last_nca), "Accounts Payable", CL_Balance, CL_BalanceDC, liability_inputs)

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

                    BalanceDC = bal_debit_cred(amount, NonCurrentAsset = accounts.NonCurrentAsset, 
                                                       CurrentAsset = accounts.CurrentAsset)
                    NCA_BalanceDC, CA_BalanceDC = BalanceDC[0], BalanceDC[1]

                    debitEntry = accounts.CurrentAsset.debit(last_ca, "NCA" + str(last_nca), "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.NonCurrentAsset.credit(last_nca,"CA" +str(last_ca), asset_name, NCA_Balance, NCA_BalanceDC, transaction_inputs)

                elif account_affected == "Cheque": 
                    NCA_related_entry = "Cash" +str(transaction_inputs[0])
                    BalanceDC = bal_debit_cred(amount, NonCurrentAsset = accounts.NonCurrentAsset, 
                                                       CurrentAsset = accounts.CurrentAsset)
                    NCA_BalanceDC, CA_BalanceDC = BalanceDC[0], BalanceDC[1]
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "NCA" + str(last_nca), "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.NonCurrentAsset.credit(last_nca,"CA" +str(last_ca), asset_name, NCA_Balance, NCA_BalanceDC, transaction_inputs)

                else: 
                    BalanceDC = bal_debit_cred(amount, NonCurrentAsset = accounts.NonCurrentAsset, 
                                                       CurrentAsset = accounts.CurrentAsset)
                    NCA_BalanceDC, CA_BalanceDC = BalanceDC[0], BalanceDC[1]
                    debitEntry = accounts.CurrentAsset.debit(last_ca, "NCA" + str(last_nca), "Accounts Receivable", CA_Balance, CA_BalanceDC, transaction_inputs)
                    creditEntry = accounts.NonCurrentAsset.credit(last_nca, "CA" + str(last_ca), asset_name, NCA_Balance, NCA_BalanceDC, transaction_inputs)
                    
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
        if request['form_id'] == "CLiabForm": 
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
            # I need to calculate interest on long term loan 
            # How to handle the current portion of long term loan that should be paid out
            return 1 
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
            return 1
        

@accounting.route('/api/transaction/expense', methods = ["POST", "GET"])
@login_required
@requires_auth
def exp_transaction():
    if request.method == "POST": 
        if request['form_id'] == "ExpForm": 
            form = ExpenseForm(request.form)

            expense_name = form.expense_name.data
            transaction_date = form.transaction_date.data 
            expense_type = form.expense_type.data
            expense_desc = form.expense_desc.data 
            amount = float(form.amount.data)
            account_affected = form.paid_using.data
            increase_decrease = form.increase_decrease.data

            if "Operating" in  expense_type: 
                # use Operating classess.. 
                if "Increase" in increase_decrease: 
                    # increase operating expense
                    if account_affected == "Cash": 
                        # Paid using Cash 
                         # Get ID of Non Current Asset to increment 
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_opexID = db.session.query(accounts.OperatingExpense).order_by(accounts.OperatingExpense.opexID.desc()).first()
                        last_opex = (int(last_opexID.opexID)+1 if last_opexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    OperatingExpense =[accounts.OperatingExpense, accounts.OperatingExpense.opexID])
                        CA_Balance, OE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, OperatingExpense = accounts.OperatingExpense)
                        CA_BalanceDC, OE_BalanceDC = BalanceDC[0], BalanceDC[1]
                        # credit entry is cASH
                        debitEntry = accounts.OperatingExpense.debit(last_opex, "CA" + str(last_ca), asset_name, OE_Balance, OE_BalanceDC, transaction_inputs)
                        creditEntry = accounts.CurrentAsset.credit(last_ca,"OE" + str(last_opex), "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)

                    else: 
                        # paid using cheque 
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_opexID = db.session.query(accounts.OperatingExpense).order_by(accounts.OperatingExpense.opexID.desc()).first()
                        last_opex = (int(last_opexID.opexID)+1 if last_opexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    OperatingExpense =[accounts.OperatingExpense, accounts.OperatingExpense.opexID])
                        CA_Balance, OE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, OperatingExpense = accounts.OperatingExpense)
                        CA_BalanceDC, OE_BalanceDC = BalanceDC[0], BalanceDC[1]
                        # credit entry is cASH
                        debitEntry = accounts.OperatingExpense.debit(last_opex, "CA" + str(last_ca), asset_name, OE_Balance, OE_BalanceDC, transaction_inputs)
                        creditEntry = accounts.CurrentAsset.credit(last_ca,"OE" + str(last_opex), "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)

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
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_opexID = db.session.query(accounts.OperatingExpense).order_by(accounts.OperatingExpense.opexID.desc()).first()
                        last_opex = (int(last_opexID.opexID)+1 if last_opexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    OperatingExpense =[accounts.OperatingExpense, accounts.OperatingExpense.opexID])
                        CA_Balance, OE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, OperatingExpense= accounts.OperatingExpense)
                        CA_BalanceDC, OE_BalanceDC = BalanceDC[0], BalanceDC[1]
                        
                        debitEntry = accounts.CurrentAsset.debit(last_ca,"OE" + str(last_opex), "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.OperatingExpense.credit(last_opex, "CA" + str(last_ca), asset_name, OE_Balance, OE_BalanceDC, transaction_inputs)
                    
                    else:
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_opexID = db.session.query(accounts.OperatingExpense).order_by(accounts.OperatingExpense.opexID.desc()).first()
                        last_opex = (int(last_opexID.opexID)+1 if last_opexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    OperatingExpense =[accounts.OperatingExpense, accounts.OperatingExpense.opexID])
                        CA_Balance, OE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, OperatingExpense = accounts.OperatingExpense)
                        CA_BalanceDC, OE_BalanceDC = BalanceDC[0], BalanceDC[1]
                        
                        debitEntry = accounts.CurrentAsset.debit(last_ca,"OE" + str(last_opex), "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.OperatingExpense.credit(last_opex, "CA" + str(last_ca), asset_name, OE_Balance, OE_BalanceDC, transaction_inputs)
                        
                        
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
                # use non operating expense class 
                if "Increase" in increase_decrease: 
                    # increase operating expense
                    if account_affected == "Cash": 
                        # Paid using Cash 
                         # Get ID of Non Current Asset to increment 
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_nOpexID = db.session.query(accounts.NonOperatingExpense).order_by(accounts.NonOperatingExpense.nOpexID.desc()).first()
                        last_nOpex = (int(last_nOpexID.nOpexID)+1 if last_nOpexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    NonOperatingExpense =[accounts.NonOperatingExpense, accounts.NonOperatingExpense.opexID])
                        CA_Balance, nOE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, NonOperatingExpense = accounts.NonOperatingExpense)
                        CA_BalanceDC, nOE_BalanceDC = BalanceDC[0], BalanceDC[1]
                        # credit entry is cASH
                        debitEntry = accounts.NonOperatingExpense.debit(last_nOpex, "CA" + str(last_ca), asset_name, nOE_Balance, nOE_BalanceDC, transaction_inputs)
                        creditEntry = accounts.CurrentAsset.credit(last_ca,"NOE" + str(last_nOpex), "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)

                    else: 
                        # paid using cheque 
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_nOpexID = db.session.query(accounts.NonOperatingExpense).order_by(accounts.NonOperatingExpense.nOpexID.desc()).first()
                        last_nOpex = (int(last_nOpexID.nOpexID)+1 if last_nOpexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    NonOperatingExpense =[accounts.NonOperatingExpense, accounts.NonOperatingExpense.opexID])
                        CA_Balance, nOE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, NonOperatingExpense = accounts.NonOperatingExpense)
                        CA_BalanceDC, nOE_BalanceDC = BalanceDC[0], BalanceDC[1]
                        # credit entry is cASH
                        debitEntry = accounts.NonOperatingExpense.debit(last_nOpex, "CA" + str(last_ca), asset_name, nOE_Balance, nOE_BalanceDC, transaction_inputs)
                        creditEntry = accounts.CurrentAsset.credit(last_ca,"NOE" + str(last_nOpex), "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)

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
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_nOpexID = db.session.query(accounts.NonOperatingExpense).order_by(accounts.NonOperatingExpense.opexID.desc()).first()
                        last_nOpex = (int(last_nOpexID.nOpexID)+1 if last_nOpexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    NonOperatingExpense =[accounts.NonOperatingExpense, accounts.NonOperatingExpense.nOpexID])
                        CA_Balance, nOE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, NonOperatingExpense =accounts.NonOperatingExpense)
                        CA_BalanceDC, nOE_BalanceDC = BalanceDC[0], BalanceDC[1]
                        
                        debitEntry = accounts.CurrentAsset.debit(last_ca,"NOE" + str(last_nOpex), "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.NonOperatingExpense.credit(last_nOpex, "CA" + str(last_ca), asset_name, nOE_Balance, nOE_BalanceDC, transaction_inputs)
                    else:
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_nOpexID = db.session.query(accounts.NonOperatingExpense).order_by(accounts.NonOperatingExpense.nOpexID.desc()).first()
                        last_nOpex = (int(last_nOpexID.nOpexID)+1 if last_nOpexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    OperatingExpense =[accounts.NonOperatingExpense, accounts.NonOperatingExpense.nOpexID])
                        CA_Balance, nOE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, NonOperatingExpense =accounts.NonOperatingExpense)
                        CA_BalanceDC, nOE_BalanceDC = BalanceDC[0], BalanceDC[1]
                        
                        debitEntry = accounts.CurrentAsset.debit(last_ca,"NOE" + str(last_nOpex), "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.NonOperatingExpense.credit(last_nOpex, "CA" + str(last_ca), asset_name, nOE_Balance, nOE_BalanceDC, transaction_inputs)
                        
                        
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
            jsonify({'message': 'Form does not match - Select Non Current Asset Form'})    
    else: 
        error_list = form_errors(form)
        return jsonify(errors= error_list)

@accounting.route('/api/transaction/revenue', methods = ["POST", "GET"])
@login_required
@requires_auth
def rev_transaction():
    if request.method == "POST": 
        if request['form_id'] == "RevForm": 
            form = RevenueForm(request.form)
            revenue_name = form.revenue_name.data 
            revenue_type = form.revenue_type.data
            transaction_date = form.transaction_date.data
            revenue_desc = form.revenue_desc.data
            amount = form.amount.data 
            account_affected = form.paid_using.data   
            increase_decrease = form.increase_decrease.data    
            

            if "Operating" in  revenue_type: 
                # use Operating classess.. 
                if "Increase" in increase_decrease: 
                    # increase operating expense
                    if account_affected == "Cash": 
                        # Paid using Cash 
                         # Get ID of Non Current Asset to increment 
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_opRevenueID = db.session.query(accounts.OperatingRevenue).order_by(accounts.OperatingRevenue.opRevenueID.desc()).first()
                        last_opRevenueID = (int(last_opRevenueID.opRevenueID)+1 if last_opRevenueID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    OperatingRevenue =[accounts.OperatingRevenue, accounts.OperatingRevenue.opRevenueID])
                        CA_Balance, OR_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, OperatingRevenue = accounts.OperatingRevenue)
                        CA_BalanceDC, OR_BalanceDC = BalanceDC[0], BalanceDC[1]

                        # credit entry is cASH
                       
                        debitEntry = accounts.CurrentAsset.debit(last_ca,"OR" + str(last_opRevenueID), "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.OperatingRevenue.credit(last_opRevenueID, "CA" + str(last_ca), revenue_name, OR_Balance, OR_BalanceDC, transaction_inputs)

                    else: 
                        # Paid using Cheque
                         # Get ID of Non Current Asset to increment 
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_opRevenueID = db.session.query(accounts.OperatingRevenue).order_by(accounts.OperatingRevenue.opRevenueID.desc()).first()
                        last_opRevenueID = (int(last_opRevenueID.opRevenueID)+1 if last_opRevenueID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    OperatingRevenue =[accounts.OperatingRevenue, accounts.OperatingRevenue.opRevenueID])
                        CA_Balance, OR_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, OperatingRevenue = accounts.OperatingRevenue)
                        CA_BalanceDC, OR_BalanceDC = BalanceDC[0], BalanceDC[1]

                        # credit entry is cASH
                        
                        debitEntry = accounts.CurrentAsset.debit(last_ca,"OR" + str(last_opRevenueID), "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.OperatingRevenue.credit(last_opRevenueID, "CA" + str(last_ca), revenue_name, OR_Balance, OR_BalanceDC, transaction_inputs)
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
                    # decrease operating revenue
                    if account_affected == "Cash": 
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_opRevenueID = db.session.query(accounts.OperatingRevenue).order_by(accounts.OperatingRevenue.opRevenueID.desc()).first()
                        last_opRevenueID = (int(last_opRevenueID.opRevenueID)+1 if last_opRevenueID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    OperatingRevenue =[accounts.OperatingRevenue, accounts.OperatingRevenue.opRevenueID])
                        CA_Balance, OR_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset, OperatingRevenue =accounts.OperatingRevenue)
                        CA_BalanceDC, OR_BalanceDC = BalanceDC[0], BalanceDC[1]
                        
                        debitEntry = accounts.OperatingRevenue.debit(last_ca,"CA" + str(last_ca+1), "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.CurrentAsset.credit(last_ca+1, "CA" + str(last_ca), asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                    else:
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_opexID = db.session.query(accounts.OperatingExpense).order_by(accounts.OperatingExpense.opexID.desc()).first()
                        last_opex = (int(last_opexID.opexID)+1 if last_opexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    OperatingExpense =[accounts.OperatingExpense, accounts.OperatingExpense.opexID])
                        CA_Balance, OE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)
                        CA_BalanceDC = BalanceDC[0]
                        
                        debitEntry = accounts.CurrentAsset.debit(last_ca,"CA" + str(last_ca+1), "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.CurrentAsset.credit(last_ca+1, "CA" + str(last_ca), asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                        
                        
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
                # use non operating expense class 
                if "Increase" in increase_decrease: 
                    # increase operating expense
                    if account_affected == "Cash": 
                        # Paid using Cash 
                         # Get ID of Non Current Asset to increment 
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_nOpexID = db.session.query(accounts.NonOperatingExpense).order_by(accounts.NonOperatingExpense.nOpexID.desc()).first()
                        last_nOpex = (int(last_nOpexID.nOpexID)+1 if last_nOpexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    NonOperatingExpense =[accounts.NonOperatingExpense, accounts.NonOperatingExpense.opexID])
                        CA_Balance, OE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)
                        CA_BalanceDC = BalanceDC[0]
                        # credit entry is cASH
                        debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.CurrentAsset.credit(last_ca+1,"CA" + str(last_ca), "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)

                    else: 
                        # paid using cheque 
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_nOpexID = db.session.query(accounts.NonOperatingExpense).order_by(accounts.NonOperatingExpense.nOpexID.desc()).first()
                        last_nOpex = (int(last_nOpexID.nOpexID)+1 if last_nOpexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    NonOperatingExpense =[accounts.NonOperatingExpense, accounts.NonOperatingExpense.opexID])
                        CA_Balance, OE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)
                        CA_BalanceDC = BalanceDC[0]
                        # credit entry is cASH
                        debitEntry = accounts.CurrentAsset.debit(last_ca, "CA" + str(last_ca+1), asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.CurrentAsset.credit(last_ca+1,"CA" + str(last_ca), "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)

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
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_nOpexID = db.session.query(accounts.NonOperatingExpense).order_by(accounts.NonOperatingExpense.opexID.desc()).first()
                        last_nOpex = (int(last_nOpexID.nOpexID)+1 if last_nOpexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    NonOperatingExpense =[accounts.NonOperatingExpense, accounts.NonOperatingExpense.nOpexID])
                        CA_Balance, OE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)
                        CA_BalanceDC = BalanceDC[0]
                        
                        debitEntry = accounts.CurrentAsset.debit(last_ca,"CA" + str(last_ca+1), "Cash", CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.CurrentAsset.credit(last_ca+1, "CA" + str(last_ca), asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                    else:
                        last_caID = db.session.query(accounts.CurrentAsset).order_by(accounts.CurrentAsset.caID.desc()).first()
                        last_ca = (int(last_caID.caID)+1 if last_caID is not None else 1)

                        last_nOpexID = db.session.query(accounts.NonOperatingExpense).order_by(accounts.NonOperatingExpense.nOpexID.desc()).first()
                        last_nOpex = (int(last_nOpexID.nOpexID)+1 if last_nOpexID is not None else 1)

                         # Get the balances of Accounts 
                        balances = account_balances(CurrentAsset = [accounts.CurrentAsset, accounts.CurrentAsset.caID],
                                                    OperatingExpense =[accounts.NonOperatingExpense, accounts.NonOperatingExpense.nOpexID])
                        CA_Balance, OE_Balance = balances[0], balances[1]


                        BalanceDC = bal_debit_cred(amount, CurrentAsset = accounts.CurrentAsset)
                        CA_BalanceDC = BalanceDC[0]
                        
                        debitEntry = accounts.CurrentAsset.debit(last_ca,"CA" + str(last_ca+1), "Cash Equivalents", CA_Balance, CA_BalanceDC, transaction_inputs)
                        creditEntry = accounts.CurrentAsset.credit(last_ca+1, "CA" + str(last_ca), asset_name, CA_Balance, CA_BalanceDC, transaction_inputs)
                        
                        
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
            jsonify({'message': 'Form does not match - Select Non Current Asset Form'})    
    else: 
        error_list = form_errors(form)
        return jsonify(errors= error_list)
        
@accounting.route('/api/transaction/equity', methods = ["POST", "GET"])
@login_required
@requires_auth
def equity_transaction():
    if request.method == "POST":             
        if request['form_id'] == "EquityForm": 
            form = EquityForm(request.form)
            return 1

    
@accounting.route('/api/printstmtdata', methods= ["GET"])
def stmt():
    resultstmt = []
    financiatransaction_inputsmt = Financiatransaction_inputsmt.query.all()
    for stmt in financiatransaction_inputsmt:
        resultstmt.append({ 'id' :stmt.stmtID,'Statement Name': stmt.fs_name})

    return jsonify(response = [resultstmt])
