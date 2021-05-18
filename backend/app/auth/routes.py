import os, sys
import jwt
import secrets
import hashlib, random
from functools import wraps
from datetime import datetime
from app import  db, login_manager,  csrf_, principal, admin_permission, \
                            owner_permission, employee_permission, fin_manger_permission
from app.forms import RegisterForm, LoginForm
from app.model import  accounts, auth, sales
from app.schema.role import role_schema, roles_schema, users_schema
from flask import  Blueprint, current_app,  request, jsonify, flash, session, _request_ctx_stack, g
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

# Flask-Login imports for session management.
from flask_login import logout_user, current_user, login_required, login_user
from flask_principal import Principal, Permission, Identity, AnonymousIdentity
from flask_principal import RoleNeed, UserNeed, identity_changed, identity_loaded

authorize= Blueprint('authorize', __name__)

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
                payload = jwt.decode(token, current_app.config['TOKEN_KEY'])

        except jwt.ExpiredSignature:
                return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
        except jwt.DecodeError:
                return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

        g.current_user = user = payload
        return f(*args, **kwargs)

    return decorated


@authorize.route('/api/csrf', methods = ["GET"])
def token():
    token = csrf_.generate_csrf(current_app.config['SECRET_KEY'])
    return jsonify(token)



"""
--------------------------------------- User Authentication Routes ----------------------------------------------------------
"""
@authorize.route('/api/auth/<userid>', methods = ["GET"])
def userDetails(userid):
    #userid = current_user.userID
    result=[]
    user = db.session.query(auth.User).filter_by(userID=userid).all()
    output = users_schema.dump(user)
    for item in output:
        fname = item['fname']
        lname = item['lname']
    return jsonify(fname=fname, lname=lname)

@authorize.route('/api/business', methods = ["GET"])
def busDetails(busID):
    busid = current_user.busID
    if busID == busid:
        business = db.session.query(auth.Business).filter_by(busID=busID).all()
        #output = sales.invoices_schema.dump(user)
    return jsonify(business)

@identity_loaded.connect_via(authorize)
def on_identity_loaded(sender, identity):
    # Set th identity user object
    identity.user = current_user

    # Update identity with a list of role for the user
    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.role_name))


@authorize.route('/api/auth/login', methods=["POST", "GET"])
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

                # Flask-Principal, register user identity into the system
                identity_changed.send(auth, identity = Identity(user.cid))
         
                user_roles = db.session.query(auth.Role).filter_by(userID = user.userID).all()
                user_roles = roles_schema.dump(user_roles)
                
                payload = {'userid': user.userID}
                token = jwt.encode(payload, current_app.config['TOKEN_KEY'], algorithm='HS256').decode('utf-8')
                return jsonify(success = [{
                                           "token": token, 
                                           "userid": user.userID, 
                                           "user_role": user_roles, 
                                           "busID": current_user.busID,
                                           "message": "User successfully logged in."
                                         }])
                
            else:
                return jsonify({'error msg': 'Login credentials failed: Please check email or password.'})
                
            return jsonify({'error msg': 'Account not found, try again or Sign up.',  })
    else:
        error_list = form_errors(form)
        form_e = form.errors
        return jsonify(errors = form_e)



@authorize.route('/api/auth/logout', methods = ["GET"])
@login_required
def logout():
    # Clears user from session
    
    if current_user.is_authenticated == True: 
        logout_user()
        
        # Flask-Principal: Remove session keys
        for key in ('identity.name', 'identity.auth_type'):
            session.pop(key, None)

        # Flask-Principal: set user to anonymous
        identity_changed.send(auth, identity=AnonymousIdentity())

        return jsonify({'message': "You have been logged out successfully"})

    else:
        return jsonify({'message': "You are not logged in."})


    
    


@authorize.route('/api/users/register', methods=["POST"])
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
            return jsonify({'message': 'Successfully registered'})

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
