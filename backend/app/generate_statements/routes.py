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

