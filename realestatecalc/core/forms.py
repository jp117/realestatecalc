from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from realestatecalc import db

from flask_login import current_user

class LogInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class RentalPropertyForm(FlaskForm):
    Title = StringField('Report Title')
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
    #Confirm how selectfield shows choices then finish choice list
    downPayment = SelectField('Down Payment (Percentage of Purchase Price)', choices=[(.2, '20%')])
    interestRate = IntegerField('Interest Rate %')
    feesAndPoints = IntegerField('Other fees and points from lender')
    payFees = RadioField('How will you pay lender fees and points?', choices=['Wrap points/fees into loan', 'Pay fees/points out of pocket'])
    interestOnly = RadioField('Intesrest Only?', choices=['Yes', 'No'], validators=[DataRequired()])
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






