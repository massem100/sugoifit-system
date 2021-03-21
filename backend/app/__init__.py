from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token


app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xbc\x86HN\x82\x12p\xceQV\x1f\x06eP\x16i\xc8=P\xb1\xc6^\xf0x'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:SQLpass@localhost/sugoifit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
cors = CORS(app, support_credentials=True)
jwt = JWTManager(app)

jwt_token = app.config['TOKEN_KEY'] = "3cc8464f0b2eef61bf0872ebf640505db394175ed8d314ab9f2d9e6eb27552ce"

# Flask_Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
