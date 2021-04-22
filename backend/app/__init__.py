from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_wtf import csrf
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
from flask_principal import Principal, Permission, Identity, AnonymousIdentity
from flask_principal import RoleNeed, UserNeed

UPLOAD_FOLDER = './static/uploads'

username = 'root'
#password = 'SQLpass'
password = ''
server = 'localhost'

app = Flask(__name__, template_folder = None)
app.config['SECRET_KEY'] = b'\xbc\x86HN\x82\x12p\xceQV\x1f\x06eP\x16i\xc8=P\xb1\xc6^\xf0x'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{}:{}@{}/sugoifit".format(username, password, server)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

#Marshmallow
ma = Marshmallow(app)

# Flask migrate
migrate = Migrate(app, db)

# CSRF Attack Protection
csrf_ = csrf
csrf_wrap = csrf_.CSRFProtect(app)

# Cross Site Resource Sharing Protection
cors = CORS(app, support_credentials=True, resources = {r"/api/*": {"origins": "http://localhost:3000"}})

# JWT Authorization Setup
jwt = JWTManager(app)
jwt_token = app.config['TOKEN_KEY'] = "3cc8464f0b2eef61bf0872ebf640505db394175ed8d314ab9f2d9e6eb27552ce"

# Flask_Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Flask-Principal Setup
principal = Principal(app)
principal.init_app(app)


# Admin has access to admin interface to manage all businesses.
admin_permission = Permission(RoleNeed('admin'))

# Owner can access all areas of the system 
owner_permission= Permission (RoleNeed('owner'))

# Employee should not have access to financial information 
# Employee should not be able to delete transactions. 
employee_permission= Permission (RoleNeed('employee'))

# Financial Manager should only be able to see invoices and Accounting statements.
fin_manger_permission= Permission (RoleNeed('manager'))


app.config.from_object(__name__)
from app import views
