import os, sys
import pandas as pd
import jwt
import secrets
import hashlib, random
from datetime import timedelta, datetime
from app.model.sales import Customer, Invoice, Order
from functools import wraps
from datetime import datetime
from app import app,  db, login_manager, cors, csrf_, principal, admin_permission, \
                            owner_permission, employee_permission, fin_manger_permission, jwt_token
# WTF Forms and SQLAlchemy Models
from app.forms import RegisterForm, LoginForm, NCAForm, websiteForm,
from app.model import  accounts, auth, sales, transactions
from app.model.sales import Product, ProductSaleItem

from app.model.financial_statement import Financialstmt, Financialstmtline, Financialstmtlineseq, Financialstmtlinealia,Financialstmtdesc 
from sqlalchemy.event import listens_for

from flask import render_template, request, jsonify, flash, session, \
                                _request_ctx_stack, g
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

# Flask-Login imports for session management.
from flask_login import logout_user, current_user, login_required, login_user
from flask_principal import Principal, Permission, Identity, AnonymousIdentity
from flask_principal import RoleNeed, UserNeed, identity_changed, identity_loaded


token =''

# def add_twoN(a,b): 
#     return a+b

"""
--------------------------------------- JWT Authorization Function and CSRF Handler----------------------------------------------------------
"""
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
    token = csrf_.generate_csrf(app.config['SECRET_KEY'])
    return jsonify(token)


"""
--------------------------------------- Financial Statement Routes ----------------------------------------------------------
"""

@app.route('/api/transaction', methods = ["POST", "GET"])
@login_required
@requires_auth
def manageTransactions():
    if request.method == "POST":
        if request.form['form_id'] == "AddNCAForm":
            form = NCAForm(request.form)
 
            # assign NCA form fields
            name = form.asset_name.data 
            transaction_date = form.transaction_date.data 
            dep_type = form.dep_type.data
            dep_rate = form.dep_rate.data
            asset_desc = form.asset_desc.data 
            amount = form.amount.data
            paid_using = form.paid_using.data
            lifeSpan = form.asset_lifespan.data
            bought_sold = form.bought_sold.data

            last_ncaID = db.session.query(accounts.NonCurrentAsset).order_by(accounts.NonCurrentAsset.ncaID.desc()).first()
            if last_ncaID is not None:
                last_id = int(last_ncaID.ncaID)
                last_id +=1
            else: 
                last_id= 1
            
            last_balance = db.session.query(accounts.NonCurrentAsset).order_by(accounts.NonCurrentAsset.ncaID.desc()).first()
            if last_balance is not None: 
                Balance = int(last_balance.Balance)
                Balance += amount 
                # Add Balance to form data 

            
            if "Bought" in  bought_sold: 
                form_data = [None, current_user.busID, lifeSpan, dep_type,  transaction_date, amount, ]
                entries =accounts.NonCurrentAsset.increase(paid_using, name, form_data )
                entry_debit = entries[0]
                entry_credit = entries[1]
                print( entry_debit, entry_credit)
                # business = auth.Busines(busID = current_user.busID)

                try:
                    # db.session.add(business)
                    db.session.add(entry_debit)
                    db.session.add(entry_credit)
                    db.session.commit()
                except Exception as e:
                     error = str(e)
                     print(error)
                
                return jsonify({'message': 'Success - Asset Bought'})   

            else: 
                form_data = ["ncaid", "busID", lifeSpan, dep_type,  transaction_date, amount]
                Entry1 =accounts.NonCurrentAsset.decrease(paid_using, name, form_data )[0]
                Entry2 =accounts.NonCurrentAsset.decrease(paid_using, name, form_data )[1]

                db.session.add()
                db.session.add(Entry2)

            
                return jsonify({'message': 'Success - Asset Sold'})                   
            
        elif request['form_id'] == "AddCAForm":
            form = CAForm(request.form)
            
        elif request['form_id'] == "LTLiabForm":
            form = LTLiabForm(request.form)

        elif request['form_id'] == "CLiabForm": 
            form = CLiabForm(request.form)

        elif request['form_id'] == "ExpForm": 
            form = ExpenseForm(request.form)
            
        elif request['form_id'] == "RevForm": 
            form = RevenueForm(request.form)
            
        elif request['form_id'] == "EquityForm": 
            form = EquityForm(request.form)
        
    else:
        return "request == GET"


@app.route('/api/printstmtdata', methods= ["GET"])
def stmt():
    resultstmt = []
    financialstmt = Financialstmt.query.all()
    for stmt in financialstmt:
        resultstmt.append({ 'id' :stmt.stmtID,'Statement Name': stmt.fs_name})


    return jsonify(response = [resultstmt])

"""
--------------------------------------- Testing Route (To be removed) ----------------------------------------------------------
"""
@app.route('/api/test', methods = ["GET", "POST"])
def home():
    data = [{'message': 'Data deh ya'}]
    # result = users.User.test('Checkingg')
    # res = sales.Customer.query.filter_by(fname='Bob').first()
    # big_name = res.fname

    if request.method =="POST":
        #  print(request.form['description'])
        return jsonify(data)

"""
--------------------------------------- User Authentication Routes ----------------------------------------------------------
"""

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Set th identity user object
    identity.user = current_user

    # Update identity with a list of role for the user
    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.role_name))


@app.route('/api/auth/login', methods=["POST", "GET"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit() and form.email.data:
        # Get the username and password values from the form.
        email = form.email.data
        passwordGiven = form.password.data

        #Check if email exists
        user = db.session.query(auth.UserCredential).filter_by(user_email=email).first()

        if user is not None:
            if check_password_hash(user.user_password, passwordGiven):
                # get user id, load into session
                login_user(user)
                print(user)
                # Flask-Principal, register user identity into the system
                identity_changed.send(app, identity = Identity(user.cid))

                payload = {'userid': user.userID}
                token = jwt.encode(payload, jwt_token, algorithm='HS256').decode('utf-8')
                return jsonify(success = [{"token": token,"userid": user.userID, "message": "User successfully logged in."}])
                
            else:
                return jsonify({'error msg': 'Login credentials failed: Please check email or password.'})
                
            return jsonify({'error msg': 'Account not found, try again or Sign up.',  })
        else: 
            return jsonify({'error msg': "No account exists with that email"})
    else:
        error_list = form_errors(form)
        form_e = form.errors
        return jsonify(errors = form_e)



@app.route('/api/auth/logout', methods = ["GET"])
@login_required
def logout():
    # Clears user from session
    logout_user()
    print(current_user)

    # Flask-Principal: Remove session keys
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    # Flask-Principal: set user to anonymous
    identity_changed.send(app, identity=AnonymousIdentity())
    
    return jsonify({'message': "You have been logged out successfully"})


@app.route('/api/users/register', methods=["POST"])
def register():
    # Wrap the request form in the flask wtf form to transfer validation etc
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate_on_submit():

        #  Add form fields
        # NEED TO SETUP SERIALIZATION LATER WITH MARSHMELLOW. 
        f_name = form.first_name.data
        l_name = form.last_name.data
        user_email = form.email.data
        user_password= form.password.data
        business_name = form.business_name.data
        # print(business_name)

        # Checks if another user has this email address
        existing_email = db.session.query(auth.UserCredential).filter_by(user_email=user_email).first()

        # Checks if business already exists
        existing_business = db.session.query(auth.Busines).filter_by(busName=business_name).first()

        # If unique email address and username provided then log new user
        if existing_business is None and existing_email is None:
            # Get the last BusID and UserID from db
            last_businessID = db.session.query(auth.Busines).order_by(auth.Busines.date_joined.desc()).first()
            last_userID = db.session.query(auth.User).order_by(auth.User.date_joined.desc()).first()

            if last_businessID is None:
                bus_int = 1
            else: 
                # Get the numeric part of the last business ID and increment by 1
                last_busID =last_businessID.busID                
                bus_int = int(last_busID[3:])
                bus_int += 1

            if last_userID is None: 
                user_int = 1
            else:
                
                # Get the numeric part of the last User ID and increment by 1
                last_uID = last_userID.userID
                user_int = int(last_uID[4:])
                user_int +=1
                
            newBusID = str(business_name[:3])+str(bus_int)
            newUserID = 'user' + str(user_int)
            bus_date = datetime.now()
            business = auth.Busines(busID = newBusID, busName = business_name, date_joined = bus_date)

            user = auth.User(userID = newUserID, fname = f_name, lname = l_name, 
                        user_address = None, phone = None)

            user_cred = auth.UserCredential(userID = newUserID, busID = newBusID, 
                                       user_email = user_email, user_password = user_password, 
                                       active = True)
            user_roles = auth.Role(role_name = "owner", userID = newUserID)
            user_cred.roles.append(user_roles)
            # print(user_cred.roles)
           
            db.session.add(business)
            db.session.add(user)
            db.session.add(user_cred)
            db.session.add(user_roles)
            db.session.commit()
            return jsonify(success =[{'message': 'Successfully registered'}])

        else: 
            # What to do if existing business is not none and email is not None
            if existing_business is not None: 
                return jsonify({'message': 'Business already exists, if you are an employee, request access from the business owner.'})
            if existing_email is not None: 
                return jsonify({'message': 'Email already exists within the system, try again.'})
    else:
        error_list = form_errors(form)
        return jsonify(errors = error_list)

@login_manager.user_loader
def load_user(id):
    user = auth.UserCredential.query.get(id)
    return user

"""
--------------------------------------- Onboarding Routes (To be added)----------------------------------------------------------
"""



"""
--------------------------------------- Report Generation Routes ----------------------------------------------------------
"""
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
    prod_numbers.sort(key= lambda x: x[1], reverse = True)

    return prod_numbers


@app.route('/website/placeorder', methods = ['POST'])
def place_order():
  #Display order based on rank
  if request.method == "POST":
    fname = request.form['fname']
    lname = request.form['lname']
    trn = request.form['trn']
    phone = request.form['phone']
    email = request.form['email']

    customer = Customer.query.filter_by(trn = trn)

    if customer.trn == None:
        # Add new customer
        new_customer = Customer(fname, lname, trn, email, phone)
        db.session.add(new_customer)
        db.session.commit()

    date_format = "%Y-%m-%d"
    status = "Pending"
    today = datetime.datetime.now()
    todayString = today.strftime(date_format)
    dateDue = (today + timedelta(days=7)).strftime(date_format)
    new_order = Order(2800, todayString, customer.custID, 'test_invoiceID','test_businessID', status, dateDue)
    db.session.add(new_order)
    db.session.commit()

    
""" 
Rank based on date order should be fulfilled
 
Click manage orders
1) Pull all orders which are pending
2) compare date due, with current date. Subtract and use the value to rank
3) Sort in ascending order based on that value.

from datetime import datetime

date_format = "%Y-%m-%d"
a = datetime.strptime('2021-04-14',date_format)
b = datetime.strptime('2021-04-22',date_format)
delta = b - a
print (delta.days)

"""
@app.route('/manage-orders')
def manageOrders():
    #Get all orders that are pending
    date_format = "%Y-%m-%d"
    allOrders = []
    ordersQuery = Order.query.filter_by(status="Pending").all()

    #Calculate days left for each record
    #Put record in tuple form and append to list
    for record in ordersQuery:
        orderID = record.orderID
        orderTotal = record.order_tot
        date = record.order_DATE
        custID = record.custID
        invoiceID = record.invoiceID
        busID = record.busIDo
        status = record.status
        dueDate = record.dueDate

        startDate = datetime.strptime(date, date_format)
        endDate = datetime.strptime(dueDate, date_format)

        daysLeft = endDate - startDate
        daysLeft = daysLeft.days()

        allOrders.append((orderID, orderTotal, date, custID, invoiceID,
        busID, status, dueDate, daysLeft))

    allOrders.sort(lambda x: x[8], reverse = False)

    #Need to print this list on the front end.
    return allOrders

#########################################################################################################

"""
--------------------------------------- Product/Services Routes ----------------------------------------------------------
"""
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

@app.route('/api/product/classify', methods = ['GET', 'POST'])

def product_classify():
    product_list = defaultdict(list)
    annual_consum_val = []
    total_consum_val = 0
    total_units_sold = 0
    product_sales = db.session.query(ProductSaleItem).all()

    for product in product_sales: 
        consum_val = product.quantitySold * product.unit_price
        annual_consum_val.append([product.psiID, consum_val])
        total_consum_val += consum_val
        total_units_sold += product.quantitySold

    # Find Percentage of Annual Units Sold 
    for product in product_sales: 
        desc_consum_val = sorted(annual_consum_val, reverse=True) # List of Annual Consumption Values (Descending Order)
        percent_units_sold = (product.quantitySold/total_units_sold)*100.0  # % of Annual Units Sold
        for val in desc_con_val: 
            percent_consum_val = (val/total_consum_val)*100.0  # % of Total Annual Consumption Value

            # Split Data ito 80/15/5
            # get length of product_list then divide by percentage
            # Assign Grades to products based on products in each percentile


    # Find Percentage of Annual Consumption Value

    return jsonify({'products': products})

"""
------------------------------------------------------------------------------------------------------------
"""
@app.route('/api/website-settings', methods = ['POST', 'GET'])
def websiteinfo():
  
  form = websiteForm()
  settings={}
  if request.method == 'POST':
    
      wel_head = request.form['wel_head']
      wel_mess = request.form['wel_mess']
      prod_mess = request.form['prod_mess']
      rec_head = request.form['rec_head']
      rec_mess = request.form['rec_mess']
      con_head = request.form['con_head']
      con_mess = request.form['con_mess']

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
------------------------------------------------------------------------------------------------------------
"""
@app.route('/api/items', methods = ['GET'])
def items():
    data = {}

    file_cont = open("/Users/User/Desktop/test_data_capstone.txt", "r")
    content = file_cont.readlines()

    data['content'] = content
    return jsonify(data)
    # return render_template("Products.vue", content=content)

"""
--------------------------------------- Orders ----------------------------------------------------------
"""
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

# To be edited
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return "error message"


if __name__ == '__main__':
    
    app.run(debug=True, host="0.0.0.0", port="8080")
    

