import os, sys
import secrets
import hashlib, random
from functools import wraps
from datetime import datetime, timedelta
# from app import   db, login_manager, cors, csrf_, principal, admin_permission, \
#                             owner_permission, employee_permission, fin_manger_permission, jwt_token
# WTF Forms and SQLAlchemy Models
from app.forms import RegisterForm, LoginForm, NCAForm, websiteForm, orderForm, newProductForm
from app.model import  accounts, auth, sales, transactions
from app.model.sales import Product, ProductSaleItem
from app.schema.sales import products_schema

from app.model.financial_statement import Financialstmt, Financialstmtline, Financialstmtlineseq, Financialstmtlinealia,Financialstmtdesc 
from sqlalchemy import func, inspection, event
from flask import  request, jsonify, flash, session, _request_ctx_stack, g
from werkzeug.utils import secure_filename
from flask import  current_app as app
from werkzeug.security import generate_password_hash, check_password_hash

# Flask-Login imports for session management.
from flask_login import logout_user, current_user, login_required, login_user
from flask_principal import Principal, Permission, Identity, AnonymousIdentity
from flask_principal import RoleNeed, UserNeed, identity_changed, identity_loaded
import json


token =''

"""
--------------------------------------- Form Error Catcher ----------------------------------------------------------
"""
# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
                message = u"Error in the %s field - %s" % (
                        getattr(form, field).label.text,
                        error
                )
                error_messages.append(message)

    return error_messages



"""
--------------------------------------- DO NOT CREATE VIEW ROUTES BELOW HERE ----------------------------------------------------------
"""

###
# The functions below should be applicable to all Flask apps.
###

def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    # response.headers['Access-Control-Allow-Origin'] = '*'

    return response


if __name__ == '__main__':
    
    app.run(debug=True, host="0.0.0.0", port="8080")
    

