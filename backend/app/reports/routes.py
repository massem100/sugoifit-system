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
