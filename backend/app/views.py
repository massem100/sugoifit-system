import os
from . import app,  db, login_manager, cors
from flask import render_template, request, jsonify, flash, session, _request_ctx_stack, g
from flask_cors import cross_origin, CORS
from flask_wtf import csrf
from .forms import RegisterForm, LoginForm, websiteForm
from .model import  asset_liability, auth, financial_statement, sales, transactions
from .model.financial_statement import Financialstmt, Financialstmtlineseq, Financialstmtlinealia, Financialstmtdesc, Financialstmtline
from .model.sales import Websitedrag, Websitedetails
from sqlalchemy.event import listens_for
from flask_login import logout_user
import pandas as pd
import enum
import secrets
import jwt
import hashlib, random

token =''

# Create a JWT @requires_auth decorator
# This decorator can be used to denote that a specific route should check
# for a valid JWT token before displaying the contents of that route.
def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None)
    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
        payload = jwt.decode(token, jwt_token)

    except jwt.ExpiredSignature:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated     


@app.route('/api/csrf', methods = ["GET"])
def token(): 
  token = csrf.generate_csrf(app.config['SECRET_KEY'])
  print(token)
  return jsonify(token)


################## PRINT FINANCIAL STATEMENTS ############################
@app.route('/api/printstmtdata', methods= ["GET"])
def stmt(): 
    resultstmt = []
    financialstmt = Financialstmt.query.all()
    for stmt in financialstmt: 
        resultstmt.append({ 'id' :stmt.stmtID, 
                            'Statement Name': stmt.fs_name})


    return jsonify(response = [resultstmt])

#########################################################################################################
@app.route('/api/test', methods = ["GET", "POST"])
def home():
    data = [{'message': 'Data deh ya'}]
    # result = users.User.test('Checkingg')
    # res = sales.Customer.query.filter_by(fname='Bob').first()
    
    # big_name = res.fname
    return jsonify(data)

################## LOGIN ############################
@app.route('/api/auth/login', methods=["POST"])
def login(): 
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit() and form.username.data:
        # Get the username and password values from the form.
        email = form.username.data
        passwordGiven = form.password.data

        #Check if email exists
        user = session.query(Credentials).filter(Credentials.email == email)

        if not user:
          flash("Sorry, Account not found")
          return redirect('/api/auth/login')
        else:
          user_password = user.user_password
          pass_salt = user.pass_salt
          #Combine password and salt
          passwordGiven = passwordGiven + pass_salt
          #Generate the hash
          passwordGiven = hashlib.sha256(passwordGiven.encode('utf-8')).hexdigest()
          if user_password == passwordGiven:
              role = user.role

              if role =="Employee":
                #Redirect to employee dashboard
                pass
              elif role =="Owner":
                  #Redirect to owner dashboard
                  pass
              else:
                #Redirect to Fmanager dashboard
                return jsonify([{'message': "Login successful", "token": "{{CSRF_token()}}"}])
          else:
                # Not using flash messages so for errors also return jsonify tag as error and handle in client.
              flash("Incorrect password given")
              return redirect('/api/auth/login')


@app.route('/add-user', methods = ["POST"])
def addUser():
  #Write code to add user to database
  #Remember to sanitize data before putting in database
  #Code to generate random salt below:
  ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  chars=[]
  for i in range(16):
    chars.append(random.choice(ALPHABET))
  salt = "".join(chars)
  

@app.route('/view-reports/view-performance')
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
  prod_numbers.sort(key= lambda x: x[1], reverse=True)

  return prod_numbers



@app.route('/api/auth/logout', methods = ['GET'])
def logout():
    logout_user()
    return jsonify(message = [{'message': "You have been logged out successfully"}])

#########################################################################################################
@app.route('/api/products', methods = ['GET'])
def products():
  message = {}
  data = {}
  tprice = 0
  deliver = 500

  lst = [
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

  for card in lst:
    tprice = tprice + int(card['price'])
  
  tcost = tprice + deliver

  data['cards'] = lst
  data['tprice'] = tprice
  data['tcost'] = tcost
  data['deliver'] = deliver
  return jsonify(data)

#########################################################################################################
@app.route('/api/website-settings', methods = ['POST', 'GET'])
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
####################################################
@app.route('/api/testdrop')
def testdrop():
  data = []
  sections = Websitedrag.query.all()
  for section in sections: 
    data.append({ 'position': section.positionID,
                  'name': section.sectionName,})
  
  return jsonify(response = [data])

#########################################################################################################
@app.route('/api/items', methods = ['GET'])
def items():
  data = {}
  
  file_cont = open("/Users/User/Desktop/test_data_capstone.txt", "r") 
  content = file_cont.readlines()
  
  data['content'] = content
  return jsonify(data)

  return render_template("Products.vue", content=content) 

#########################################################################################################
@app.route('/api/order', methods = ['POST', 'GET'])
def custOrder():
  customer = {}
  '''
  form = orderForm()
  if form.validate_on_submit():
    if request.method == 'POST': 

      # Get info.
      fname = request.form['fname']
      lname = request.form['lname']
      trn = request.form['trn']
      address = request.form['address']
      phone_num = request.form['phone_num']
      email = request.form['email']

      customer['first_name'] = fname
      customer['last_name'] = lname
      customer['TRN'] = trn
      customer['address'] = address
      customer['telephone'] = phone_num
      customer['emaile'] = email
            '''
  return jsonify(
      [
        {'message': "Data saved successfully"}, 
        {'token': csrf }
      ])



# @login_manager.user_loader
# def load_user(id):
#     user = User.query.get(int(id))
#     return user

# # Please create all new routes and view functions above this route.
# # This route is now our catch all route for our VueJS single page
# # application.
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def index(path):
#     """
#     Because we use HTML5 history mode in vue-router we need to configure our
#     web server to redirect all routes to index.html. Hence the additional route
#     "/<path:path".

#     Also we will render the initial webpage and then let VueJS take control.
#     """
#     return render_template('index.html')

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

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
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


# @app.errorhandler(404)
# def page_not_found(error):
#     """Custom 404 page."""
#     return render_template('404.html'), 404


if __name__ == '__main__':
    # insert_initial_values()
    app.run(debug=True, host="0.0.0.0", port="8080")
    

