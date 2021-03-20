import os
from app import app, db, csrf, cors
from flask import jsonify, flash
from app.forms import RegisterForm, LoginForm
from app.model import  asset_liability, auth, financial_statement, sales, transactions
from flask_cors import cross_origin




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


@app.route('/api/test', methods = ["GET"])
@cross_origin(supports_credentials=True)
def home():
    data = [{'message': 'Data deh ya'}]
    # result = users.User.test('Checkingg')
    res = sales.Customer.query.filter_by(fname='Bob').first()
    
    big_name = res.fname
    return jsonify(data,big_name)

    return jsonify(data)

@app.route('/api/auth/login', methods=["POST"])
def login(): 
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit() and form.username.data:
            # Get the username and password values from the form.
        email = form.username.data
        password = form.password.data

        if email == "johndoe@gmail.com" and password == "pass":
            
            return jsonify([{'message': "Login successful", "token": "{{CSRF_token()}}"}])
           
@app.route('/api/auth/logout', methods = ['GET'])
def logout():
    logout_user()
    return jsonify(message = [{'message': "You have been logged out successfully"}])

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
    return response


# @app.errorhandler(404)
# def page_not_found(error):
#     """Custom 404 page."""
#     return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

