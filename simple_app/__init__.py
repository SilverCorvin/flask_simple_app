import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = False
app.config['TESTING'] = False
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'secret-key'
db_name = '{}.db'.format(__name__)
db_path = os.path.join(os.path.dirname(__file__), db_name)
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)


import simple_app.views
# from simple_app.models import UserProfile
