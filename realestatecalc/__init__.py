import os
from flask import Flask
from pymongo import MongoClient
from flask_login import LoginManager

app = Flask(__name__)


app.config['SECRET_KEY'] = 'FAtchance'

client = MongoClient()
db = client.realestatecalc

login = LoginManager(app)

from realestatecalc.core.views import core

app.register_blueprint(core)