from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import csrf
# from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
from flask_security import Security


app = Flask(__name__, template_folder = None)
app.config['SECRET_KEY'] = b'\xbc\x86HN\x82\x12p\xceQV\x1f\x06eP\x16i\xc8=P\xb1\xc6^\xf0x'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:SQLpass@localhost/sugoifit'
username = 'root'
password = 'SQLpass'
server = 'localhost'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{}:{}@{}/sugoifit".format(username, password, server)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Statements below allow us to initialize the MYSQL database
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'SQLpass'
# app.config['MYSQL_PORT'] = 3306
# app.config['MYSQL_DB'] = 'sugoifit'

# Initializing the SQL connection to our app.
# mysql = MySQL(app)
# mysql = MySQL()
# mysql.init_app(app)


db = SQLAlchemy(app)
csrf_wrap = csrf.CSRFProtect(app)
cors = CORS(app, support_credentials=True, resources = {r"/api/*": {"origins": "http://localhost:3000"}})
# cors = CORS(app, support_credentials=True, )
jwt = JWTManager(app)

jwt_token = app.config['TOKEN_KEY'] = "3cc8464f0b2eef61bf0872ebf640505db394175ed8d314ab9f2d9e6eb27552ce"

# Flask_Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


app.config.from_object(__name__)
from app import views
