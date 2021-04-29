import os, sys
import secrets
import hashlib, random
from functools import wraps
from datetime import datetime, timedelta
from app import db, login_manager, csrf_, principal, admin_permission, \
                            owner_permission, employee_permission, fin_manger_permission
# WTF Forms and SQLAlchemy Models
from app.forms import websiteForm,orderForm
from app.model import  accounts, auth, sales, transactions
from flask import Blueprint, request, jsonify, flash, session, _request_ctx_stack, g
from werkzeug.utils import secure_filename

website= Blueprint('website', __name__)


"""
--------------------------------------- Website Routes ----------------------------------------------------------
"""
@website.route('/api/checkout-products', methods = ['GET'])
def checkoutproducts():
    message = {}
    data = {}
    tprice = 0
    deliver = 500

    transaction_inputs = [
            {
                'id': 1,
                'img': "https://5.imimg.com/data5/RU/WI/MY-46283651/school-skirts-500x500.jpg",
                'name': 'skirt',
                'quantity': '1',
                'size': 'L',
                'colour': 'black',
                'price': "500"
            },
            {
                'id': 2,
                'img': "https://slimages.macysassets.com/is/image/MCY/products/2/optimized/17864922_fpx.tif?$browse$&wid=170&fmt=jpeg",
                'name': 'pants',
                'quantity': '1',
                'size': 'medium',
                'colour': 'white',
                'price': '1000'
            },
            {
                'id': 3,
                'img': "https://di2ponv0v5otw.cloudfront.net/posts/2018/03/24/5ab6a736077b9758675a91e5/m_5ab6c769c9fcdfbadf53cd14.jpeg",
                'name': 'top',
                'quantity': '1',
                'size': 'medium',
                'colour': 'white',
                'price': '800'
            }
        ]

    for card in transaction_inputs:
        tprice = tprice + int(card['price'])

    tcost = tprice + deliver
    data["lst"] = lst
    data["total_price"] = tprice
    data["delivery_price"] = deliver
    data["total_cost"] = tcost

    return jsonify(data)



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

  