from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# from app import app  # we import the app object from the app module

from app import db
from app import init_app

app = init_app()

with app.app_context(): 

    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    @app.before_first_request
    def create_tables():
        db.create_all()

if __name__ == '__main__':
    manager.run()
