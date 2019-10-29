from flask import render_template, Blueprint, request, session, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from realestatecalc.analyzeProperty.forms import RentalPropertyForm
from realestatecalc import db

analyzeProp = Blueprint('analyzeProp', __name__)

@analyzeProp.route('/analyzeproperty', methods=['GET', 'POST'])
@login_required
def analyze():
    print(current_user.get_id())
    form = RentalPropertyForm()

    return render_template('mainSite/analyzeproperty.html', form=form)