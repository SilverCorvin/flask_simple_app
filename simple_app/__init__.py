from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simple_app/simple_app.db'

db = SQLAlchemy(app)


import simple_app.views
from simple_app.models import UserProfile
