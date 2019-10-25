from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'FAtchance'

from realestatecalc.core.views import core

app.register_blueprint(core)