import os, sys
import secrets
import hashlib, random
from functools import wraps
from datetime import datetime, timedelta
import pandas as pd

# WTF Forms and SQLAlchemy Models
from app.forms import RegisterForm, LoginForm, NCAForm, websiteForm,orderForm, LTLiabForm, CAForm,ExpForm, RevForm
from app.model import  accounts, auth, sales, transactions
from app.model.financial_statement import Financialstmt, Financialstmtline, Financialstmtlineseq, \
                                          Financialstmtlinealia,Financialstmtdesc 
from app.accounting.routes import account_balances
from sqlalchemy import func, inspection, event

from flask import request, jsonify, flash, session, _request_ctx_stack, g
from werkzeug.utils import secure_filename

from flask import Blueprint, current_app
from app import db, login_manager, principal, csrf_
from app.auth.routes import requires_auth

# Flask-Login imports for db.session management.
from flask_login import logout_user, current_user, login_required, login_user
from flask_principal import Principal, Permission, Identity, AnonymousIdentity
from flask_principal import RoleNeed, UserNeed, identity_changed, identity_loaded

# Blueprint Configuration
statement= Blueprint('statement', __name__)


"""
select * from financialstmtline join financialstmtlineseq on lineID = fsStmtLineID where fsStmtID = 1 order by sequence asc;

Get data from each account  - asset table 
find the total of each account by grouping by name then subtracting sum(debit )- sum(credit) 
events - how to ensure that the table is created before. db.event.listens_for
^^^^ this will be used to find the category total 
for the sub categories or items - we can just list them out 


SELECT financial_statement_line.name FROM financial_statement_line
JOIN financial_statement_line_sequence
ON financial_statement_line.id = financial_statement_line_sequence.financial_statement_line_id
JOIN financial_statement
ON financial_statement.id = financial_statement_line_sequence.financial_statement_id
WHERE financial_statement.name = 'Commercial Income Statement'
ORDER BY financial_statement_line_sequence.sequence;
"""



commercial_income_statement = Financialstmt(fs_name='Commercial Income Statement')
commercial_balance_sheet = Financialstmt(fs_name='Commercial Balance Sheet Statement')
commercial_cash_flow_statement = Financialstmt(fs_name='Commercial Cash Flow Statement')

financial_income_statement = Financialstmt(fs_name='Financial Income Statement')
financial_balance_sheet = Financialstmt(fs_name='Financial Balance Sheet Statement')
financial_cash_flow_statement = Financialstmt(fs_name='Financial Cash Flow Statement')


@event.listens_for(Financialstmt.__table__, "after_create")
def insert_initial_values(*args, **kwargs):
    print ("working")
    db.session.add(commercial_income_statement)
    db.session.add(commercial_balance_sheet)
    db.session.add(commercial_cash_flow_statement)
    db.session.add(financial_income_statement)
    db.session.add(financial_balance_sheet)
    db.session.add(financial_cash_flow_statement)
    db.session.commit()

@event.listens_for(Financialstmtline.__table__, "after_create")
def insert_initial_values(*args, **kwargs):
    
    financial_statement_lines = pd.read_csv(r"C:\Users\Masse\Desktop\Files\sugoifit-system\backend\app\financial_statements_lines.csv")
    print (financial_statement_lines)       
    for index, line in financial_statement_lines.iterrows():
        db.session.add(Financialstmtline( tag=line['tag'], line_name=line['name']))
    db.session.commit()   

@event.listens_for(Financialstmtlineseq.__table__, "after_create")
def insert_initial_values(*args, **kwargs):
    print("reach")
    financial_statement_lines = pd.read_csv(r"C:\Users\Masse\Desktop\Files\sugoifit-system\backend\app\financial_statements_lines.csv")
    statement_types = ['commercial', 'financial']
    statement_codes = ['income_statement', 'balance_sheet_statement', 'cash_flow_statement']

    for statement_type in statement_types:
        for statement_code in statement_codes:
            statement_name = (statement_type + ' ' + statement_code.replace('_',' ')).title()
            statement = db.session.query(Financialstmt) \
                .filter(Financialstmt.fs_name == statement_name).first()
            financial_statement_sequence = financial_statement_lines[
                (financial_statement_lines['statement_type'] == statement_type) & \
                (financial_statement_lines['statement_code'] == statement_code)]
            
            for index, row in financial_statement_sequence.iterrows():
                line = db.session.query(Financialstmtline) \
                    .filter(Financialstmtline.tag == row['tag']).first()
                db.session.add(Financialstmtlineseq(sequence=row['sequence'],
                                                        fsStmtID =statement.stmtID,
                                                        fsStmtLineID=line.lineID))
        db.session.commit()

"""
Things not yet accounted for 

Inventory 
Sales 
Purchases 
How to calculate stuff that cant be directly entered? 
"""
# Create Inventory Tables
# def calcTotalOpex(*args, **kwargs): 
#     balance = db.session.query(value).order_by(value.id.desc()).first()
#     balance = (float(balance.Balance) if balance is not None else 0)
#     return balance
"""
------------------------------------------------------ Generate Income Statement -------------------------------------------------------------------------
"""
def calcNetSales(prod_service, *args, **kwargs):
    # get balance of service sale item and product sale item
    if prod_service == "Product": 
        # total number of goods x average price per good sold
        # average price per services sold x number of service 
        # grossSales = db.session.query(ProductSaleItem).order_by(ProductSaleItem.id.desc()).first()
        # filter_by Year
        grossSales = ProductSaleItem.query.with_entities(func.coalesce(func.sum(ProductSaleItem.saleAmtPaid), 0).label("totalSales")).first()
        grossSales = (float(grossSales.totalSales) if grossSales is not None else 0)

        # Get balance from sale reductions table
        saleReductions = db.session.query(SaleReductions).filter_by(SaleType = "Product").order_by(SaleReductions.id.desc()).first()
        saleReductions = (float(saleReductions.Balance) if  saleReductions is not None else 0)
        
        return grossSales-saleReductions
    elif prod_service== "Service": 
        # total number of goods x average price per good sold
        # average price per services sold x number of service 
        grossSales = ServiceSaleItem.query.with_entities(func.coalesce(func.sum(ServiceSaleItem.saleAmtPaid), 0).label("totalSales")).first()
        grossSales = (float(grossSales.totalSales) if grossSales is not None else 0)

        # Get balance from sale reductions table
        saleReductions = db.session.query(SaleReductions).filter_by(SaleType = "Service").order_by(SaleReductions.id.desc()).first()
        saleReductions = (float(saleReductions.Balance) if  saleReductions is not None else 0)
           
        return grossSales-saleReductions
    else: 
        productSales = ProductSaleItem.query.with_entities(func.coalesce(func.sum(ProductSaleItem.saleAmtPaid), 0).label("totalSales")).first()
        productSales = (float(productSales.totalSales) if productSales is not None else 0)

        serviceSales = ServiceSaleItem.query.with_entities(func.coalesce(func.sum(ServiceSaleItem.saleAmtPaid), 0).label("totalSales")).first()
        serviceSales = (float(serviceSales.totalSales) if serviceSales is not None else 0)







def calculateNetProfit(grossProfit, expenses): 
    return grossProfit - expenses

def calculateCOGS(beg_inv, end_inv, purchases, year): 


    return beg_inv + purchases - end_inv

def calcTotalExpenses(): 
    pass


def calcOperatingRevenue(): 
    pass

def calcTaxation(): 
    pass

"""
------------------------------------------------------ Generate Balance Statement -------------------------------------------------------------------------
"""

def calcTotalAssets(): 
    # get the balance from NCA and CA accounts and sum  
    # if inventory is separate from current asset add that in
    account_balances(NonCurrentAsset=accounts.NonCurrentAsset, CurrentAsset = accounts.CurrentAsset)
    NCA_Total,CA_Total  = account_balances[0], account_balances[1]
    
    return NCA_Total + CA_Total

def calcTotalLiabilities(): 
    # get the Balance from LTLiab and CLiab and sum it
    account_balances(CurrentLiability = accounts.Currentliability, Longtermliability= accounts.Longtermliability)
    CLiab_Total, LTLiab_Total  = account_balances[0], account_balances[1]
    return CLiab_Total + LTLiab_Total


def calcCapital(): 
    # Either have one function to calculate capital based on sole trader, partnership or company or have separate functions. 
    pass


def isBalSheetBalance(): 
    # Total Assets = Total Liabilities + Total Capital
    liab_cap = calcCapital() + calcTotalLiabilities()
    return calcTotalAssets == liab_cap

def ca_list_items(ledgerID):
    inventory_bal = 0 
    receivable_bal = 0
    cash_bal = 0 
    bank_bal = 0 
    prepaid_exp_bal = 0 
    market_sec_bal = 0 
    other_assets_bal = 0 

    ca_line_items = accounts.CurrentAsset.query.with_entities(
                                                accounts.CurrentAsset.tag,
                                                func.coalesce(func.sum(accounts.CurrentAsset.debitBalance), 0).label("totalDebit"),
                                                func.coalesce(func.sum(accounts.CurrentAsset.creditBalance), 0).label("totalCredit")
                                            ).filter_by(ledgerID= ledgerID).group_by(accounts.CurrentAsset.tag).all()
    for asset in ca_line_items(): 
        if asset.tag == 'inventory':
            inventory_bal += asset.debitBalance - asset.creditBalance
        elif 'receivable' in asset.tag: 
            receivable_bal += asset.debitBalance - asset.creditBalance
        elif asset.tag =='cash': 
            cash_bal += asset.debitBalance - asset.creditBalance
        elif asset.tag == 'cashequivalents': 
            bank_bal += asset.debitBalance - asset.creditBalance
        elif asset.tag == 'prepaidexpense': 
            prepaid_exp_bal += asset.debitBalance - asset.creditBalance
        elif asset.tag == 'marketablesecurities': 
            market_sec_bal += asset.debitBalance - asset.creditBalance
        else: 
            other_assets_bal += asset.debitBalance - asset.creditBalance
   
    
    current_asset_lst = {
                            'Inventory': inventory_bal, 
                            'Accounts Receivable': receivable_bal, 
                            'Cash': cash_bal, 
                            'Cash Equivalents': bank_bal,
                            'Prepaid Expense': prepaid_exp_bal, 
                            'Marketable Securities': market_sec_bal,
                            'Other Liquid Assets': other_assets_bal
                        }
    return current_asset_lst

def cl_list_items(ledgerID):
    payables_bal = 0 
    cportion_loan_bal = 0 
    accrued_exp_bal = 0 
    other_cliab_bal = 0
    tax_payable = 0 
    unearned_revenue = 0 
    st_loans_bal = 0 

    cl_line_items = acccounts.Currentliability.query.with_entities(
                                                accounts.Currentliability.tag,
                                                func.coalesce(func.sum(accounts.Currentliability.debitBalance), 0).label("totalDebit"),
                                                func.coalesce(func.sum(accounts.Currentliability.creditBalance), 0).label("totalCredit")
                                            ).filter_by(ledgerID= ledgerID).group_by(accounts.Currentliability.tag).all()
    # for asset in cl_line_items(): 
    #     if asset.tag == 'accountspayables':
    #         inventory_bal += asset.debitBalance - asset.creditBalance
    #     elif 'portion' in asset.tag: 



        

@statement.route('/api/financialstmt/balancesheet/<busID>/<year>')
def generate_balance_sheet(busID, year=datetime.now().year):

    GeneralLedger = db.session.query(accounts.GeneralLedger).filter_by(busID = busID, YEAR = year)
    id = GeneralLedger.ledgerID 
    # ca_list_items(id)
    # nca_line_items = db.session.query(accounts.NonCurrentAsset.filter_by(ledgerID=id)).all()
    # cl_line_items = db.session.query(accounts.Currentliability.filter_by(ledgerID=id)).all()
    # ltl_line_items = db.session.query(accounts.Longtermliability.filter_by(ledgerID=id)).all()
    # cap_line_items = db.session.query(accounts.ShareholdersEquity.filter_by(ledgerID=id)).all()
    return jsonify({'currentAsset': ca_list_items(id)})






