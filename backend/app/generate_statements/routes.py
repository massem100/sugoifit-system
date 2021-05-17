import os, sys
import secrets
import hashlib, random
from functools import wraps
from datetime import datetime, timedelta
import pandas as pd

# WTF Forms and SQLAlchemy Models
from app.forms import RegisterForm, LoginForm, NCAForm, websiteForm,orderForm, LTLiabForm, CAForm,ExpForm, RevForm
from app.model import  accounts, auth, sales
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
Things not yet accounted for 

Inventory 
Sales 
Purchases 
How to calculate stuff that cant be directly entered? 
"""
# Create Inventory Tables
# def calcTotalOpex(*args, **kwargs): 
#     balance = db.session.query(value).order_by(value.id.desc()).first()
#     balance = (str(balance.Balance) if balance is not None else 0)
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
        grossSales = (str(grossSales.totalSales) if grossSales is not None else 0)

        # Get balance from sale reductions table
        saleReductions = db.session.query(SaleReductions).filter_by(SaleType = "Product").order_by(SaleReductions.id.desc()).first()
        saleReductions = (str(saleReductions.Balance) if  saleReductions is not None else 0)
        
        return grossSales-saleReductions
    elif prod_service== "Service": 
        # total number of goods x average price per good sold
        # average price per services sold x number of service 
        grossSales = ServiceSaleItem.query.with_entities(func.coalesce(func.sum(ServiceSaleItem.saleAmtPaid), 0).label("totalSales")).first()
        grossSales = (str(grossSales.totalSales) if grossSales is not None else 0)

        # Get balance from sale reductions table
        saleReductions = db.session.query(SaleReductions).filter_by(SaleType = "Service").order_by(SaleReductions.id.desc()).first()
        saleReductions = (str(saleReductions.Balance) if  saleReductions is not None else 0)
           
        return grossSales-saleReductions
    else: 
        productSales = ProductSaleItem.query.with_entities(func.coalesce(func.sum(ProductSaleItem.saleAmtPaid), 0).label("totalSales")).first()
        productSales = (str(productSales.totalSales) if productSales is not None else 0)

        serviceSales = ServiceSaleItem.query.with_entities(func.coalesce(func.sum(ServiceSaleItem.saleAmtPaid), 0).label("totalSales")).first()
        serviceSales = (str(serviceSales.totalSales) if serviceSales is not None else 0)


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


def opex_list_items(ledgerID): 
    selling_admin = 0 
    dist_bal =0 
    bad_debt_bal =0 
    dep_bal = 0 
    gen_expense = 0 
    other_opex = 0

    opex_line_items = db.session.query(accounts.OperatingExpense, 
                                                accounts.OperatingExpense.tag,
                                                func.coalesce(func.sum(accounts.OperatingExpense.debitBalance), 0).label("totalDebit"),
                                                func.coalesce(func.sum(accounts.OperatingExpense.creditBalance), 0).label("totalCredit")
                                            ).filter_by(ledgerID= ledgerID).group_by(accounts.OperatingExpense.tag).all()
    if opex_line_items is not None: 
        for expense in opex_line_items: 
            if expense.tag == 'Selling & Administration Expenses':
                selling_admin += expense.totalDebit - expense.totalCredit
            elif expense.tag == 'Distribution Expense':
                dist_bal += expense.totalDebit - expense.totalCredit  
            elif expense.tag == 'General Expense':
                gen_expense += expense.totalDebit - expense.totalCredit
            elif expense.tag == 'Depreciation Expense':
                dep_bal += expense.totalDebit - expense.totalCredit
            elif expense.tag == 'Bad Debt Expense':
                bad_debt_bal += expense.totalDebit - expense.totalCredit
            else: 
                other_opex += expense.totalDebit - expense.totalCredit

        operating_expense_lst = {
                                'Selling & Administration Expenses': str(selling_admin), 
                                'Distribution Expenses': str(dist_bal), 
                                'General Expenses': str(gen_expense), 
                                'Depreciation Expense': str(dep_bal),
                                'Bad Debt Expense': str(bad_debt_bal), 
                                'Other Operating Expense': str(other_opex), 
                               
                            }
    return operating_expense_lst    
                
            


def nopex_list_items(ledgerID): 
    interest_exp = 0 
    loss_disposals = 0 
    other_nopex = 0

    nopex_line_items = db.session.query(accounts.NonOperatingExpense, 
                                                accounts.NonOperatingExpense.tag,
                                                func.coalesce(func.sum(accounts.NonOperatingExpense.debitBalance), 0).label("totalDebit"),
                                                func.coalesce(func.sum(accounts.NonOperatingExpense.creditBalance), 0).label("totalCredit")
                                            ).filter_by(ledgerID= ledgerID).group_by(accounts.NonOperatingExpense.tag).all()
    if nopex_line_items is not None: 
        for expense in nopex_line_items: 
            if expense.tag == 'Interest Expense':
                interest_exp += expense.totalDebit - expense.totalCredit
            elif expense.tag == 'Loss on Disposal':
                loss_disposals += expense.totalDebit - expense.totalCredit  
            else: 
                other_nopex += expense.totalDebit - expense.totalCredit

        nonoperating_expense_lst = {
                                'Interest Expense': str(interest_exp), 
                                'Loss on Disposal': str(loss_disposals), 
                                'Other Non Operating Expense': str(other_nopex), 
                               
                            }
    return nonoperating_expense_lst    


@statement.route('/api/financialstmt/incomestatement/<busID>/<year>')
def generate_income_statement(busID, year =str(datetime.today().strftime('%Y'))):

    GeneralLedger = db.session.query(accounts.GeneralLedger).filter_by(busID = busID, year = year).first()
    if GeneralLedger is not None: 
        id = GeneralLedger.ledgerID 
        
        return jsonify({
            'Operating Expenses': opex_list_items(id), 
            'Non Operating Expenses': nopex_list_items(id),
            # 'Operating Revenue': opex_list_items(id), 
            # 'Non Operating Revenue': nopex_list_items(id),
            'Sales': str(1), 
            'Cost of Goods Sold': str(1), 
            'Gross Profit': str(1), 

        })
    else: 
        return jsonify({'message': 'No general ledger'})


            

"""
------------------------------------------------------ Generate Balance Statement -------------------------------------------------------------------------
"""

def calcTotalAssets(ledgerID): 
    # get the balance from NCA and CA accounts and sum  
    # if inventory is separate from current asset add that in
    balance = account_balances(ledgerID, NonCurrentAsset=accounts.NonCurrentAsset, CurrentAsset = accounts.CurrentAsset)
    NCA_Total,CA_Total  = balance[0], balance[1]
    
    return NCA_Total + CA_Total

def getBSTotals(ledgerID): 
    balance = account_balances(ledgerID, CurrentAsset = accounts.CurrentAsset, NonCurrentAsset = accounts.NonCurrentAsset, 
                                        CurrentLiability = accounts.Currentliability, LongTermLiability = accounts.Longtermliability)
    return [balance[0], balance[1],balance[2], balance[3]]


def calcTotalLiabilities(ledgerID): 
    # get the Balance from LTLiab and CLiab and sum it
    balance = account_balances(ledgerID,CurrentLiability = accounts.Currentliability, Longtermliability= accounts.Longtermliability)
    CLiab_Total, LTLiab_Total  = balance[0], balance[1]
    return CLiab_Total + LTLiab_Total


def calcCapital(id): 
    # Either have one function to calculate capital based on sole trader, partnership or company or have separate functions. 
    return calcTotalAssets(id) - calcTotalLiabilities(id)


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

    ca_line_items = db.session.query(accounts.CurrentAsset, 
                                                accounts.CurrentAsset.tag,
                                                func.coalesce(func.sum(accounts.CurrentAsset.debitBalance), 0).label("totalDebit"),
                                                func.coalesce(func.sum(accounts.CurrentAsset.creditBalance), 0).label("totalCredit")
                                            ).filter_by(ledgerID= ledgerID).group_by(accounts.CurrentAsset.tag).all()
    if ca_line_items is not None: 
        for asset in ca_line_items: 
            if asset.tag == 'Inventory':
                inventory_bal += asset.totalDebit - asset.totalCredit
            elif asset.tag == 'Accounts Receivable': 
                receivable_bal += asset.totalDebit - asset.totalCredit
            elif asset.tag =='Cash': 
                cash_bal += asset.totalDebit - asset.totalCredit
            elif asset.tag == 'Cash Equivalents': 
                bank_bal += asset.totalDebit - asset.totalCredit
            elif asset.tag == 'Prepaid Expenses': 
                prepaid_exp_bal += asset.totalDebit - asset.totalCredit
            elif asset.tag == 'Marketable Securities': 
                market_sec_bal += asset.totalDebit - asset.totalCredit
            else: 
                other_assets_bal += asset.totalDebit - asset.totalCredit
    
        
        current_asset_lst = {
                                'Inventory': str(inventory_bal), 
                                'Accounts Receivable': str(receivable_bal), 
                                'Cash': str(cash_bal), 
                                'Cash Equivalents': str(bank_bal),
                                'Prepaid Expense': str(prepaid_exp_bal), 
                                'Marketable Securities':str(market_sec_bal),
                                'Other Liquid Assets': str(other_assets_bal),
                                'Total Current Assets': str(getBSTotals(ledgerID)[0])
                            }
    return current_asset_lst

def nca_list_items(ledgerID):
    ppe_bal = 0 
    other_nca_assets = 0 
    intan_bal = 0 
    investments_bal = 0 

    nca_line_items = db.session.query(accounts.NonCurrentAsset, 
                                                accounts.NonCurrentAsset.tag,
                                                func.coalesce(func.sum(accounts.NonCurrentAsset.debitBalance), 0).label("totalDebit"),
                                                func.coalesce(func.sum(accounts.NonCurrentAsset.creditBalance), 0).label("totalCredit")
                                            ).filter_by(ledgerID= ledgerID).group_by(accounts.NonCurrentAsset.tag).all()

    if nca_line_items is not None: 
        for asset in nca_line_items: 
            if asset.tag == 'Property, Plant and Equipment':
                ppe_bal += asset.totalDebit - asset.totalCredit
            elif asset.tag == 'Long Term Investment': 
                investments_bal += asset.totalDebit - asset.totalCredit
            elif  asset.tag == 'Intangible Asset': 
                intan_bal += asset.totalDebit - asset.totalCredit
            else:  
                other_nca_assets += asset.totalDebit - asset.totalCredit
            
        
        noncurrent_asset_lst = {
                                'Property, Plant & Equipment': str(ppe_bal), 
                                'Long Term Investment': str(investments_bal),
                                'Intangible Asset': (intan_bal), 
                                'Other Non Current Asset': str(other_nca_assets), 
                                'Total Non Current Assets': str(getBSTotals(ledgerID)[1])
                                
                            }
    return noncurrent_asset_lst

def cl_list_items(ledgerID):
    payables_bal = 0 
    cportion_loan_bal = 0 
    accrued_exp_bal = 0 
    other_cliab_bal = 0
    tax_payable = 0 
    unearned_revenue = 0 
    st_loans_bal = 0 

    cl_line_items = db.session.query(accounts.Currentliability,                          
                                                accounts.Currentliability.tag,            
                                                func.coalesce(func.sum(accounts.Currentliability.debitBalance), 0).label("totalDebit"),
                                                func.coalesce(func.sum(accounts.Currentliability.creditBalance), 0).label("totalCredit")
                                            ).filter_by(ledgerID= ledgerID).group_by(accounts.Currentliability.tag).all()
    
    if cl_line_items is not None:
        for liab in cl_line_items: 
            if liab.tag == 'Accounts Payable':
                payables_bal += liab.totalDebit - liab.totalCredit
            elif 'portion' in liab.tag: 
                cportion_loan_bal += liab.totalDebit - liab.totalCredit
            elif liab.tag == 'Accrued Expense': 
                accrued_exp_bal += liab.totalDebit - liab.totalCredit
            elif liab.tag == 'Other Current Liabilities': 
                other_cliab_bal += liab.totalDebit - liab.totalCredit
            elif liab.tag == 'Tax Payable': 
                tax_payable += liab.totalDebit - liab.totalCredit
            elif liab.tag == 'Unearned Revenue': 
                unearned_revenue += liab.totalDebit - liab.totalCredit
            else: 
                st_loans_bal += liab.totalDebit - liab.totalCredit

        current_liab_items= [
                            {'Accounts Payable': str(payables_bal), 
                            'Short Term Loans': str(st_loans_bal), 
                            'Tax Payable': str(tax_payable),
                            'Accrued Expenses': str(accrued_exp_bal), 
                            'Current Portion of Long Term Loans': str(cportion_loan_bal), 
                            'Unearned Revenue': str(unearned_revenue),
                            'Other Current Liabilities': str(other_cliab_bal),
                            'Total Current Liabilities':str(getBSTotals(ledgerID)[2])

        }]
    return current_liab_items

def lt_list_items(ledgerID):
    lt_loan_bal = 0 
    def_tax_bal = 0 
    mortgage_bal = 0 
    other_ltliab_bal = 0
    debentures = 0 
    bonds_bal = 0 
    
    lt_line_items = db.session.query(accounts.Longtermliability, 
                                                accounts.Longtermliability.tag,
                                                func.coalesce(func.sum(accounts.Longtermliability.debitBalance), 0).label("totalDebit"),
                                                func.coalesce(func.sum(accounts.Longtermliability.creditBalance), 0).label("totalCredit")
                                            ).filter_by(ledgerID= ledgerID).group_by(accounts.Longtermliability.tag).all()

    if lt_line_items is not None: 
        for liab in lt_line_items: 
            if liab.tag == 'Long Term Loan':
                lt_loan_bal += liab.totalDebit - liab.totalCredit
            elif liab.tag == 'Deferred Taxation': 
                def_tax_bal += liab.totalDebit - liab.totalCredit
            elif liab.tag == 'Mortgage': 
                mortgage_bal += liab.totalDebit - liab.totalCredit
            elif 'Other' in liab.tag: 
                other_ltliab_bal += liab.totalDebit - liab.totalCredit
            elif liab.tag == 'Debentures': 
                debentures += liab.totalDebit - liab.totalCredit
            else:  
                bonds_bal += liab.totalDebit - liab.totalCredit

        long_term_liab_items= [
                            {'Long Term Loan': str(lt_loan_bal), 
                            'Deferred Taxation': str(def_tax_bal), 
                            'Mortgage': str(mortgage_bal),
                            'Bonds Payable': str(bonds_bal), 
                            'Debentures': str(debentures), 
                            'Other Long Term Liabilities': str(other_ltliab_bal),
                            'Total Long Term Liabilities': str(getBSTotals(ledgerID)[3])

                            }]
    return long_term_liab_items

# Find some of Capital 
        

@statement.route('/api/financialstmt/balancesheet/<busID>/<year>')
def generate_balance_sheet(busID, year =str(datetime.today().strftime('%Y'))):

    GeneralLedger = db.session.query(accounts.GeneralLedger).filter_by(busID = busID, year = year).first()
    if GeneralLedger is not None: 
        id = GeneralLedger.ledgerID 
        
        
        return jsonify({
            'currentAsset': ca_list_items(id), 
            'Non Current Asset': nca_list_items(id),
            'Current Liabilities': cl_list_items(id),
            'Long Term Liability': lt_list_items(id),
            'Capital': str(calcCapital(id))
        })
    else: 
        return jsonify({'message': 'No general ledger'})







