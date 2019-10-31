from flask import render_template, Blueprint, request, session, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from realestatecalc.analyzeProperty.forms import RentalPropertyForm
from realestatecalc import db
from realestatecalc.core.models import User
from bson.objectid import ObjectId
from decimal import Decimal
from realestatecalc.analyzeProperty.rentalPropAnalysis import capRate, noi, freeCashFlow, monthlyLoanPayment, monthlyLoanPaymentInterestOnly

analyzeProp = Blueprint('analyzeProp', __name__)

@analyzeProp.route('/analyzeproperty', methods=['GET', 'POST'])
@login_required
def analyze():
    form = RentalPropertyForm()
    if form.validate_on_submit():
        x = db.rentalProperty.insert({
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
            'interestRate': str(form.interestRate.data),
            'amortizationPeriod': form.amortizationPeriod.data,
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
            'vacancy': str(form.vacancy.data),
            'repairsAndMaint': str(form.repairsAndMaint.data),
            'capex': str(form.capex.data),
            'managementFees': str(form.managementFees.data),
            'incomeGrowth': str(form.incomeGrowth.data),
            'appreciation': str(form.appreciation.data),
            'expenseGrowth': str(form.expenseGrowth.data),
            'salesExpenses': str(form.salesExpenses.data)
        })
        return redirect(url_for('analyzeProp.analyzedReport', analyzepropertyform_id=x))
    return render_template('analysis/analyzepropertyform.html', form=form)

@analyzeProp.route('/<analyzepropertyform_id>', methods=['GET', 'POST'])
@login_required
def analyzedReport(analyzepropertyform_id):
    prop = list(db.rentalProperty.find({'_id': ObjectId(analyzepropertyform_id)}))
    prop = prop[0]
    title = prop['title']
    address = "{0}, {1}, {2} {3}".format(prop['street'], prop['city'], prop['state'], prop['zipcode'])
    purchasePrice = prop['purchasePrice']
    grossRent = (prop['rent'] * 12 * (100 - Decimal(prop['vacancy'])) / 100) + prop['otherIncome'] * 12
    managementFee = grossRent * Decimal(prop['managementFees']) / 100
    grossExpenses = ((prop['electricity'] + prop['waterAndSewer'] + prop['pmi'] + 
        prop['garbage'] + prop['hoa'] + prop['insurance'] + prop['otherExpenses']) * 12 + prop['propertyTax'] + managementFee)
    if prop['payFees'] == 'oop':
        financeAmount = prop['purchasePrice'] * Decimal(prop['downPayment'])
    else:
        financeAmount = (prop['purchasePrice'] + prop['closingCosts']) * Decimal(prop['downPayment'])
    return render_template('analysis/analysisPage.html', title=title, address=address.title())