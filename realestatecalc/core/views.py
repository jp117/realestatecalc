from flask import render_template, Blueprint
from datetime import datetime

core = Blueprint('core', __name__)

@core.context_processor
def inject_now():
    return {'now':datetime.utcnow()}

@core.route('/')
def index():
    return render_template('mainSite/index.html')