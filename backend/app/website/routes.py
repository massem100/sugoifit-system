import os, sys
import secrets
import hashlib, random
from functools import wraps
from datetime import datetime, timedelta
from app import db, mail,  login_manager, csrf_, principal, admin_permission, \
                            owner_permission, employee_permission, fin_manger_permission

# WTF Forms and SQLAlchemy Models
from app.forms import websiteForm, orderForm,ProofOfPaymentForm, ContactForm
from app.model import auth
from app.model.sales import CustomerPayment, Customer, Order, Orderdetail
from app.views import form_errors
from flask import Blueprint, current_app, request, jsonify, flash, session, _request_ctx_stack, g
from flask_login import current_user
from werkzeug.utils import secure_filename
from flask_mail import Message 

website= Blueprint('website', __name__)


"""
--------------------------------------- Website Routes ----------------------------------------------------------
"""

"""
----------------------------------------SETTINGS------------------------------------------------------
"""
@website.route('/api/website-settings', methods = ['POST', 'GET'])
def websiteinfo():
  
  form = websiteForm(request.form)
  settings={}
  if request.method == 'POST':
    
      wel_head = form.wel_head.data
      wel_mess = form.wel_mess.data
      prod_mess = form.prod_mess.data
      rec_head = form.rec_head.data
      rec_mess = form.rec_mess.data
      con_head = form.con_head.data
      con_mess = form.con_mess.data

      settings['welcome_head'] = wel_head
      settings['welcome_mess'] = wel_mess
      settings['product_mess'] = prod_mess
      settings['receipt_head'] = rec_head
      settings['receipt_mess'] = rec_mess
      settings['contact_head'] = con_head
      settings['contact_mess'] = con_mess

      #welcome = Websitedetails( section_detail='wel' sec_header=wel_head, sec_message=wel_mess)
      #product = Websitedetails( section_detail='prod' sec_message=prod_mess)
      #receipt = Websitedetails( section_detail='rec' sec_header=rec_head, sec_message=rec_mess)
      #contact = Websitedetails( section_detail='con' sec_header=con_head, sec_message=con_mess)
      #db.session.add(welcome)
      #db.session.add(product)
      #db.session.add(receipt)
      #db.session.add(contact)
      #db.session.commit()
      '''
      return jsonify(settings)

  elif request.method == 'GET':
    website = sales.Websitedrag
    sections = website.query.filter_by().all()
    return jsonify(sections.sectionName)
'''
  return jsonify({'message':"Success"}, settings)

  
  
"""
---------------------------------------- WEBSITE FORMS ------------------------------------------------------
"""

@website.route('/api/proof-payment', methods = ['POST'])
def proof_payment(): 
    form = ProofOfPaymentForm(request.form)
    if request.method == 'POST' and form.validate_on_submit(): 

        order_no = form.order_no.data 
        customer_name = form.cust_name.data 
        receipt = request.files["image"]
        
        if receipt is not None:
            secure_file = secure_filename(receipt.filename)
            receipt.save(os.path.join(current_app.config['UPLOAD_FOLDER'], secure_file))

        fname, lname = customer_name.split() 

        custID = db.session.query(Customer).filter_by(fname = fname, lname = lname).first()
        order_num = db.session.query(Order).filter_by(orderID = order_no).first()

        if custID is None or order_num is None: 
            jsonify({'message': 'No Order exists with that order number or customer name.' })
        else: 
            new_payment = CustomerPayment(custID, order_no, receipt)
            db.session.add(new_payment)
            db.session.commit()
            return jsonify({'message': 'Proof of Payment successfully added. An email will be sent when order is updated.'})
    else: 
        error_list = form_errors(form)
        return jsonify(errors= error_list)
            
# ----------------------- NEED TO BE TESTED -----------------------------------------
@website.route('/api/website/place-order', methods=['POST', 'GET'])
def web_place_order(): 
    cust_form = orderForm(request.form)
    if request.method == 'POST' and request.form.validate_on_submit(): 
        # CHANGE ALL TO GET DIRECTLY FROM REQUEST - let frontend handle validation using vee-validate
        fname = cust_form.fname.data 
        lname = cust_form.lname.data
        trn = cust_form.trn.data 
        address = cust_form.address.data 
        phone_num = cust_form.phone_num.data 
        email = cust_form.email.data 


        order_date = datetime.now() 
        order_tot = cust_form.order_tot.data 
        custID = 1
        invoiceID = 1
        # order_total = form.o
        new_customer = Customer(custID=None, 
                                fname = fname, 
                                lname = lname, 
                                trn = trn,
                                email = email, 
                                address = address)
        last_orderID = db.session.query(Order).filter_by(busID = current_user.busID).order_by(Order.orderID.desc()).first()
        orderID = (int(last_orderID.orderID)+1 if last_orderID is not None else 1)

        new_order = Order(  orderID=None, 
                            order_tot=order_tot,
                            order_DATE= order_date, 
                            custID=custID,
                            invoiceID=invoiceID,
                            busID=current_user.busID,
                            status='Pending Payment')
        # Orderdetail(orderID = orderID, detailsID, prodID, serviceID, quantity, order_tot)
    else: 
        error_list = form_errors(cust_form)
        return jsonify({'Order Number': orderID, 'errors': error_list})
            



@website.route('/api/website/contact', methods=['POST', 'GET'])
def contact_form(): 
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate_on_submit(): 
        
        customer_name = form.name.data  
        subject = form.subject.data 
        email = form.email.data 
        phone_num = form.phone_num.data 
        message = form.message.data 

        msg = Message(subject, sender=(customer_name, email), recipients=[email])
        msg.body = message
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully!'})

    else: 
        error_list = form_errors(form)
        return jsonify(errors= error_list)
            
