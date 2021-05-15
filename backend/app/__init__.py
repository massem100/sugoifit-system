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
from flask import Blueprint
from flask import current_app
from werkzeug.utils import import_string
from flask_marshmallow import Marshmallow
from flask_mail import Mail 

db = SQLAlchemy()
principal = Principal()
login_manager = LoginManager()
csrf_ = csrf
# JWT Authorization Setup
jwt = JWTManager()
ma = Marshmallow

mail = Mail()



def init_app(): 
    app = Flask(__name__, instance_relative_config=False, template_folder = None)
    app.config.from_object('config.Config')

    username, password, server = 'root', 'SQLpass','localhost'
    # username, password, server = 'root', '', 'localhost'
    app.config['SECRET_KEY'] = b'\xbc\x86HN\x82\x12p\xceQV\x1f\x06eP\x16i\xc8=P\xb1\xc6^\xf0x'
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{}:{}@{}/sugoifit".format(username, password, server)
    app.config["SQLALCHEMY_BINDS"] ={
                                        'sugoifit': "mysql+mysqlconnector://{}:{}@{}/sugoifit".format(username, password, server)                                  
                                    }
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # from app.model import db
    db.init_app(app)

    # Flask-Principal Setup
    principal.init_app(app)

    # Flask_Login login manager
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # Flask migrate
    migrate = Migrate(app, db)

    # Flask Mail 
    app.config['SECRET_KEY'] = 'Peter rabit bakes'
    app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
    app.config['MAIL_PORT'] = '465' # (or try 2525)
    app.config['MAIL_USERNAME'] = 'massem100@outlook.com'
    app.config['MAIL_PASSWORD'] = 'rabits'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)


    with app.app_context():      

        # CSRF Attack Protection
        csrf_wrap = csrf_.CSRFProtect(app)

        
            
        # Cross Site Resource Sharing Protection
        cors = CORS(app, support_credentials=True, resources = {r"/api/*": {"origins": "http://localhost:3000"}})
        app.config['TOKEN_KEY'] = "3cc8464f0b2eef61bf0872ebf640505db394175ed8d314ab9f2d9e6eb27552ce"
        jwt.init_app(app)
        
        # Blueprints
        from .accounting.routes import accounting 
        app.register_blueprint(accounting)

        from .sales.routes import sales
        app.register_blueprint(sales)

        from .website.routes import website
        app.register_blueprint(website)

        from .products.routes import product
        app.register_blueprint(product)

        from .auth.routes import authorize
        app.register_blueprint(authorize)  

        from .generate_statements.routes import statement
        app.register_blueprint(statement)   

       
        #    Include View routes
        from app import views
        
         # from . import model
        # from .model import auth, accounts, financial_statement, sales
        # db.create_all()
    return app 


# Admin has access to admin interface to manage all businesses.
admin_permission = Permission(RoleNeed('admin'))

# Owner can access all areas of the system 
owner_permission= Permission (RoleNeed('owner'))

# Employee should not have access to financial information 
# Employee should not be able to delete transactions. 
employee_permission= Permission (RoleNeed('employee'))

# Financial Manager should only be able to see invoices and Accounting statements.
fin_manger_permission= Permission (RoleNeed('manager'))

