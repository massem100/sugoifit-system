import os, sys
import pandas as pd
import jwt, secrets
import hashlib, random
from app import app,  db, login_manager, cors, csrf_, principal, admin_permission, \
                            owner_permission, employee_permission, fin_manger_permission
# WTF Forms and SQLAlchemy Models
from app.forms import RegisterForm, LoginForm, NCAForm
from app.model import  accounts, auth, sales, transactions
from app.model.financial_statement import Financialstmt, Financialstmtlineseq, Financialstmtlinealia,\
                                                                                Financialstmtdesc, Financialstmtline
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
    # print(token)
    return jsonify(token)


"""
--------------------------------------- Financial Statement Routes ----------------------------------------------------------
"""

@app.route('/api/transaction', methods = ["POST", "GET"])
def manageTransactions():
    if request.method == "POST":
        if request['form_id'] == "AddNCAForm":
            form = NCAForm(request.form)

            # assign NCA form fields
            
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
def on_identity_loaded (sender, identity):
    # Set th identity user object
    identity.user = current_user

    # Update identity with a list of role for the user
    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.name))


@app.route('/api/auth/login', methods=["POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit() and form.email.data:
        # Get the username and password values from the form.
        email = form.email.data
        passwordGiven = form.password.data
        print({email, passwordGiven})

        #Check if email exists
        user_email = auth.Credential.user_email
        user_credential = User.query.filter_by(user_email=email).first()
        # user = db.session.query(auth.Credential).filter(auth.Credential.user_email = email).first()

        if user is not None:
            user_password = user_credential.user_password
            if check_password_hash(user_password, passwordGiven):
                # get user id, load into session
                login_user(user_credential)
                # Flask-Principal, register user identity into the system
                identity_changed.send(app, identity = Identity(auth.Credential.userID))
                role = user.role

                #Redirect to employee dashboard
                with employee_permission.require():
                    return jsonify({'access': 'employee', 'message': 'Login Successful, Entering Employee Dashboard'})
                #Redirect to owner dashboard
                with owner_permission.require():
                    return jsonify({'access': 'owner','message': 'Login Successful' })

                #Redirect to Fmanager dashboard
                with fin_manager_permission.require():
                    return jsonify({'access': 'financialmanager', 'message': 'Login Successful, Entering Financial Dashboard'})
            else:
                return jsonify({'error msg': 'Login credentials failed: Please check email or password.'})
                
            return jsonify({'error msg': 'Account not found, try again or Sign up.',  })
    else:
        error_list = form_errors(form)
        form_e = form.errors
        return jsonify(errors = form_e)



@app.route('/api/auth/logout', methods = ['GET'])
def logout():
    logout_user()

    # Flask-Prinicpal send identity_changed to anonymous
    # Attach requires_auth decorator
    return jsonify(message = [{'message': "You have been logged out successfully"}])


@app.route('/api/users/register', methods=["POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate_on_submit():

        #  Add form fields
        f_name = form.first_name.data
        l_name = form.last_name.data
        user_email = form.email.data
        user_password= form.password.data
        business_name = form.business_name.data


        # Checks if another user has this email address
        existing_email = db.session.query(UserCredential).filter_by(user_email=user_email).first()

        # Checks if business already exists
        existing_business = db.session.query(Busines).filter_by(busName=business_name).first()

        # If unique email address and username provided then log new user
        if existing_business is None and existing_email is None:
            # user = User(username=username

            db.session.add(user)
            db.session.commit()

            return jsonify(success =[{'message': 'Successfully registered'}])
    else:
        error_list = form_errors(form)
        return jsonify(errors = error_list)

@login_manager.user_loader
def load_user(id):
    user = User.query.get(userID)
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
    prod_numbers.sort(key= lambda x: x[1], reverse=True)

    return prod_numbers




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

    data['cards'] = lst
    data['tprice'] = tprice
    data['tcost'] = tcost
    data['deliver'] = deliver
    return jsonify(data)

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


