from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Optional
from wtforms import ValidationError

class RentalPropertyForm(FlaskForm):
    title = StringField('Report Title', validators=[DataRequired()])
    street = StringField('Street address', validators=[Optional()])
    city = StringField('City', validators=[Optional()])
    state = StringField('State', validators=[Optional()])
    zipcode = IntegerField('Zipcode', validators=[Optional()])
    purchasePrice = IntegerField('Purchase Price', validators=[DataRequired()])
    improvementCosts = IntegerField('Improvement Costs', validators=[Optional()])
    closingCosts = IntegerField('Closing Costs', validators=[Optional()])
    miscCosts = IntegerField('Miscellaneous Other Costs', validators=[Optional()])
    afterRepairValue = IntegerField('After Repair Value', validators=[Optional()])
    cashPurchase = BooleanField('All Cash Purchase?', validators=[Optional()])
    downPayment = SelectField('Down Payment (Percentage of Purchase Price)', choices=[
        (' ',' '),('.05', '5%'),('.1', '10%'),(.15, '15%'),
        (.2, '20%'),(.25, '25%'),(.3, '30%'),(.35, '35%'),
        (.4, '40%'),(.45, '45%'),(.5, '50%'), (.55, '55%'),
        (.6, '60%'),(.65, '65%'),(.7, '70%'), (.75, '75%'),
        (.8, '80%'),(.85, '85%'),(.9, '90%'), (.95, '95%'),
        (1, '100%')],
        validators=[Optional()])
    interestRate = IntegerField('Interest Rate %', validators=[Optional()])
    feesAndPoints = IntegerField('Other fees and points from lender', validators=[Optional()])
    payFees = RadioField('How will you pay lender fees and points?', choices=[('wrap', 'Wrap points/fees into loan'), ('oop','Pay fees/points out of pocket')], validators=[Optional()])
    interestOnly = RadioField('Intesrest Only?', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()], default="No")
    rent = IntegerField('Gross Monthly Rent', validators=[DataRequired()])
    otherIncome = IntegerField('Other Monthly Income', validators=[Optional()])
    electricity = IntegerField('Monthly Electric', validators=[Optional()])
    waterAndSewer = IntegerField('Monthly Water and Sewer', validators=[Optional()])
    pmi = IntegerField('Monthly PMI', validators=[Optional()])
    garbage = IntegerField('Monthly Garbage', validators=[Optional()])
    hoa = IntegerField('Monthly HOA', validators=[Optional()])
    insurance = IntegerField('Monthly Insurnace', validators=[Optional()])
    propertyTax = IntegerField('Yearly Property Taxes', validators=[Optional()])
    otherExpenses = IntegerField('Other Monthly Expenses', validators=[Optional()])
    vacancy = IntegerField('Vacancy Rate %', validators=[Optional()])
    repairsAndMaint = IntegerField('Repairs and Maintenance %', validators=[Optional()])
    capex = IntegerField('Capital Expenditures %', validators=[Optional()])
    managementFees = IntegerField('Management Fee %', validators=[Optional()])
    incomeGrowth = IntegerField('Income Growth %', validators=[Optional()])
    appreciation = IntegerField('Property Value Appreciation %', validators=[Optional()])
    expenseGrowth = IntegerField('Expense Growth %', validators=[Optional()])
    salesExpenses = IntegerField('Sales Expense %', validators=[Optional()])
    submit = SubmitField('Analyze Property', validators=[Optional()])