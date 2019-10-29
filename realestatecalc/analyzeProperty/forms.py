from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms import ValidationError

class RentalPropertyForm(FlaskForm):
    title = StringField('Report Title')
    street = StringField('Street address')
    city = StringField('City')
    state = StringField('State')
    zip = IntegerField('Zipcode')
    purchasePrice = IntegerField('Purchase Price', validators=[DataRequired()])
    improvementCosts = IntegerField('Improvement Costs')
    closingCosts = IntegerField('Closing Costs')
    miscCosts = IntegerField('Miscellaneous Other Costs')
    afterRepairValue = IntegerField('After Repair Value')
    cashPurchase = BooleanField('All Cash Purchase?')
    downPayment = SelectField('Down Payment (Percentage of Purchase Price)', choices=[
        (' ',' '),(.05, '5%'),(.1, '10%'),(.15, '15%'),
        (.2, '20%'),(.25, '25%'),(.3, '30%'),(.35, '35%'),
        (.4, '40%'),(.45, '45%'),(.5, '50%'), (.55, '55%'),
        (.6, '60%'),(.65, '65%'),(.7, '70%'), (.75, '75%'),
        (.8, '80%'),(.85, '85%'),(.9, '90%'), (.95, '95%'),
        (1, '100%')])
    interestRate = IntegerField('Interest Rate %')
    feesAndPoints = IntegerField('Other fees and points from lender')
    payFees = RadioField('How will you pay lender fees and points?', choices=[('wrap', 'Wrap points/fees into loan'), ('oop','Pay fees/points out of pocket')])
    interestOnly = RadioField('Intesrest Only?', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    rent = IntegerField('Gross Monthly Rent', validators=[DataRequired()])
    otherIncome = IntegerField('Other Monthly Income')
    electricity = IntegerField('Monthly Electric')
    waterAndSewer = IntegerField('Monthly Water and Sewer')
    pmi = IntegerField('Monthly PMI')
    garbage = IntegerField('Monthly Garbage')
    hoa = IntegerField('Monthly HOA')
    insurance = IntegerField('Monthly Insurnace')
    propertyTax = IntegerField('Yearly Property Taxes')
    otherExpenses = IntegerField('Other Monthly Expenses')
    vacancy = IntegerField('Vacancy Rate %')
    repairsAndMaint = IntegerField('Repairs and Maintenance %')
    capex = IntegerField('Capital Expenditures %')
    managementFees = IntegerField('Management Fee %')
    incomeGrowth = IntegerField('Income Growth %')
    appreciation = IntegerField('Property Value Appreciation %')
    expenseGrowth = IntegerField('Expense Growth %')
    salesExpenses = IntegerField('Sales Expense %')
    submit = SubmitField('Analyze Property')