from flask import render_template, Blueprint, request, session, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from realestatecalc.analyzeProperty.forms import RentalPropertyForm
from realestatecalc import db
from realestatecalc.core.models import User

analyzeProp = Blueprint('analyzeProp', __name__)

@analyzeProp.route('/analyzeproperty', methods=['GET', 'POST'])
@login_required
def analyze():
    form = RentalPropertyForm()
    if form.validate_on_submit():
        db.rentalProperty.insert({
            'user': current_user.get_id(),
            'title': form.title.data,
            'street': form.street.data,
            'city': form.city.data,
            'state': form.state.data,
            'zipcode': form.zipcode.data,
            'purchasePrice': form.purchasePrice.data,
            'improvementCosts': form.improvementCosts.data,
            'closingCosts': form.closingCosts.data,
            'miscCosts': form.miscCosts.data,
            'afterRapairValue': form.afterRepairValue.data,
            'cashPurchase': form.cashPurchase.data,
            'downPayment': form.downPayment.data,
            'interestRate': form.interestRate.data,
            'feesAndPoints': form.feesAndPoints.data,
            'payFees': form.payFees.data,
            'interestOnly': form.interestOnly.data,
            'rent': form.rent.data,
            'otherIncome': form.otherIncome.data,
            'electricity': form.electricity.data,
            'waterAndSewer': form.waterAndSewer.data,
            'pmi': form.pmi.data,
            'garbage': form.garbage.data,
            'hoa': form.hoa.data,
            'insurance': form.insurance.data,
            'propertyTax': form.propertyTax.data,
            'otherExpenses': form.otherExpenses.data,
            'vacancy': form.vacancy.data,
            'repairsAndMaint': form.repairsAndMaint.data,
            'capex': form.capex.data,
            'managementFees': form.managementFees.data,
            'incomeGrowth': form.incomeGrowth.data,
            'appreciation': form.appreciation.data,
            'expenseGrowth': form.expenseGrowth.data,
            'salesExpenses': form.salesExpenses.data
        })
        return 'submitted'
    return render_template('mainSite/analyzeproperty.html', form=form)