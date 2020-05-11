from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_jsglue import JSGlue



app = Flask(__name__) 
# app = Flask(__name__, static_url_path='/templates')
app.config['SECRET_KEY'] = '8c5963ea5bf3d00e8e44e3a366639d15'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jsglue = JSGlue(app)
login_manager = LoginManager(app)
login_manager.login_view = 'hello_login'
login_manager.login_message_category = 'info'

from flaskblog import routes


