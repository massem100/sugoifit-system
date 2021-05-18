import os, sys
import secrets
import hashlib, random
from functools import wraps
from datetime import datetime, timedelta
from app import  db, login_manager, cors, csrf_, principal, admin_permission, \
                            owner_permission, employee_permission, fin_manger_permission, jwt_token
# WTF Forms and SQLAlchemy Models
from app.model import  accounts, sales
from app.model.sales import Product, ProductSaleItem, Customer, Invoice, Order
from app.generate_statements import getBSTotals

from app.model.financial_statement import Financialstmt, Financialstmtline, Financialstmtlineseq, Financialstmtlinealia,Financialstmtdesc 
from sqlalchemy import func, inspection, event
from flask import  Blueprint, request, jsonify, flash, session, _request_ctx_stack, g
from werkzeug.utils import secure_filename

reports = Blueprint('reports', __name__)



"""
--------------------------------------- Report Generation Routes ----------------------------------------------------------
"""
@reports.route('/view-reports/view-performance')
def sucessful_prods():
    #Remember to use busID as filter for products
    #Find a way to get business ID here
    #Get all products for the busID

    busID = "Test123"
    result = session.query(Product).filter(Product.busID == busID)
    prod_numbers = []

    for product in result:
        #Add to list as tuple with product name and amount sold
        #Other fields required can be added
        prod_numbers.append([product.prodName, product.amtSold])

    #Item with highest number of sales would be at the top
    prod_numbers.sort(key= lambda x: x[1], reverse = True)

    return prod_numbers

"""
Ratio Analysis
CashFlow Revenue 
Group by Tag then print out values for expenses 

"""
@reports('/api/<busID>/ratios', methods=["GET"])
def generateRatios():
    total_cash_equiv = 0
    total_inventories = 0
    total_current_liab = getBSTotals()[0]
    total_current_asssets = getBSTotals()[2]
    net_sales = calcNetSales(current_user.busID)
    cost_of_goods_sold = calcCOGS
    total_assets = getBSTotals[0] + getBSTotals[1]
    total_liab = getBSTotals[2] + getBSTotals[3]
    operating_income = calcIncomeStmtTotals(busID, ledgerID)["Operating Income"]

   current_ratio = currentRatio(total_current_asssets, total_current_liab ) 
   cash_ratio = cashRatio(total_cash_equiv, total_current_liab s)
   acid_test_ratio = acidTestRatio(total_current_asssets, inventories, total_current_liab )
   invent_turn = inventoryTurnoverRatio(cost_of_goods_sold, avgInventory)
   asset_turn = assetTurnoverRatio(net_sales, avgTotalAssets)
   debt_ratio =  debtRatio(total_liab, total_assets)
   

    return jsonify({
                    'Current Ratio': current_ratio, 
                    'Acid Test Ratio': acid_test_ratio, 
                    'Cash Ratio': cash_ratio, 
                    'Debt Ratio': debt_ratio, 
                    'Asset Turnover': asset_turn, 
                    'Inventory Turnover': invent_turn, 
                     
    })
'''
 # interest expense
    # avgAccountsReceivable
    # avgInventory
    # avgTotalAssets
    # operating_cashflow 
'''

# Liquidity Ratios
def currentRatio(currentAsset,cLiabilities): 
    calc = currentAsset/cLiabilities
    return calc

def acidTestRatio(currentAsset, inventories, cLiabilities): 
    return (currentAsset-inventories )/ cLiabilities
    
def cashRatio(cashequiv,cLiabilities): 
    calc = cashequiv/cLiabilities
    return calc

def opcashFlowRatio(opcashflow ,cLiabilities): 
    calc = opcashflow /cLiabilities
    return calc

# Leverage Financial Ratios

def debtRatio(totalLiabilities, totalAssets):
    calc = totalLiabilities/totalAssets
    return calc

def debtEquityRatio(totalLiabilities,shareEquity):
    calc = totalLiabilities/ shareEquity
    return calc

def interestCoverageRatio(opIncome, interestExpense): 
    calc = opIncome/interestExpense
    return calc

# Efficiency Ratios 
def assetTurnoverRatio(netSales, avgTotalAssets):
    calc = netSales/avgTotalAssets
    return calc

def inventoryTurnoverRatio(costOfGoodsSold, avgInventory):
    calcc = costOfGoodsSold/avgInventory
    return calc 

# def receivablesTurnoverRatio(netCreditSales, avgAccountsReceivable):
#     calc = netCreditSales/avgAccountsReceivable
#     return calc

def daysInventoryRatio(inventoryTurnoverRatio):
    calcc = 365/inventoryTurnoverRatio
    return calc


def prof_margin(sales, expenses):
    """ The percentage of sales revenue that is
        profit."""      
    return ((sales - expenses) / sales ) * 100

def op_margin(sales, op_expenses):
    """ The percentage of profit a company produces 
        from its operations """
    return ((sales - op_expenses) / sales ) * 100

def break_even(fixed_cost, unit_price, var_cost):
    """ The point at which there is neither profit nor loss /
        where income and expenditure are equal"""

    #The value is the minimum units you need to avoid profit loss
    return (fixed_cost / (unit_price - var_cost))
