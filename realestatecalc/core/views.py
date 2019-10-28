from flask import render_template, Blueprint, request, session, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
import bcrypt
from realestatecalc.core.forms import LogInForm, RegistrationForm, RentalPropertyForm
from realestatecalc import db
from realestatecalc.core.models import User

core = Blueprint('core', __name__)

@core.context_processor
def inject_now():
    return {'now':datetime.utcnow()}

@core.route('/')
def index():
    return render_template('mainSite/index.html')

@core.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))

@core.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    error = 'Invalid username / password'
    if form.validate_on_submit():
        user = db.users.find_one({'email': form.email.data})
        if user:
            if bcrypt.hashpw(form.password.data.encode('utf-8'), user['password']) == user['password']:
                user_obj = User(email=user['email'])
                login_user(user_obj)
                next = request.args.get('next')
                if next is None or next[0] == '/':
                    next = 'core.index'
                return redirect(url_for(next))
        return render_template('mainSite/login.html', form=form, error=error)
    return render_template('mainSite/login.html', form=form)


@core.route('/analyzeproperty')
@login_required
def analyze():
    form = RentalPropertyForm()
    return render_template('mainSite/analyzeproperty.html', form=form)

@core.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        users = db.users
        existing_user = users.find_one({'email': form.email.data})
        error = 'that username already exists'

        if existing_user is None:
            hashpass = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            db.users.insert({
                'email': form.email.data, 
                'password': hashpass
            })
            return redirect(url_for('core.login'))
        return render_template('mainSite/register.html', form=form, error=error)

    return render_template('mainSite/register.html', form=form)
