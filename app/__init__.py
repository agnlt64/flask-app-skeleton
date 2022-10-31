# This directory is a Python package because of this file
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database config stuff
# You can modify the name here, but make sure to do it everywhere
db = SQLAlchemy()
DB_NAME = "database.db"  

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "<add a secret key here>"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    # Add a custom prefix
    app.register_blueprint(views)
    app.register_blueprint(auth)
    
    # Your application initialization code goes here
    
    return app