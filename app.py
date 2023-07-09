# 🤪  setUp Imports

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from models import db, Production

# 🤪  Intialize the App
app = Flask(__name__)

# 🤪  setUp database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🤪  setUp migration and initialize instance with 'db.init)app(app)
migrate = Migrate(app, db)
db.init_app(app)
