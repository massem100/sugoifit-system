from flask_wtf import FlaskForm
from wtforms.fields import EmailField,IntegerField, DateField, DecimalField
from wtforms import TextAreaField, StringField, PasswordField, SubmitField 
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired


class RegisterForm(FlaskForm):
    first_name = StringField('first Name', validators=[InputRequired('Please enter your first name, e.g. John.')])
    last_name = StringField('last Name', validators=[InputRequired('Please enter your last name, e.g. Doe.')])
    email = EmailField('Email', validators = [InputRequired('Please enter your email address, e.g. johndoe@XXXX.XXX'), Email()])
    password = PasswordField('password', validators=[InputRequired('Please enter a password.')])
    business_name = StringField('business name', validators=[InputRequired('Please enter your business name.')])
    
class LoginForm(FlaskForm):
    email = EmailField('Email', validators = [InputRequired('Please enter your email address e.g. johndoe@XXXX.XXX.'), Email()])
    password = PasswordField('Password', validators = [InputRequired('Please enter a password.')]) 

class orderForm(FlaskForm):
    fname = StringField('first Name', validators=[InputRequired('Please enter your first name, e.g "John".')])
    lname = StringField('last Name', validators=[InputRequired('Please enter your last name, e.g. "Doe".')])
    trn = StringField('trn', validators=[InputRequired('Please enter your TRN Number, e.g 001-001-001.')])
    address = StringField('Address', validators=[InputRequired('Please enter your address.')])
    phone_num = StringField ('Telephone', validators =[InputRequired('Please enter your your phone number.')])
    email = EmailField('Email', validators = [InputRequired('Please enter your email address, e.g. johndoe@XXXX.XXX.'), Email()])
    submit = SubmitField('Submit')

dep_types_list = [
            ('Straight Line Method', "Straight Line Method"),
            ('Declining balance', "Declining balance"), 
            ('Sum-of-the-years \'digits', "Sum-of-the-years \'digits"),
            ('Units of Production', "Units of Production")
]

timeSpanYears = [('Weeks', 'weeks'),('Months', 'months') ('Years', 'years')]

paid_using = [('By Cash', 'Cash'), ('By Cheque', 'Cheque'), ('On Credit', 'Credit')]

class NCAForm(FlaskForm): 
    asset_name = StringField('Asset Name', validators = [InputRequired('Please enter the name of the asset, e.g. Motor Vehicle')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    dep_type = SelectField('Depreciation Type', choices = dep_types_list)
    asset_desc = TextAreaField('Description', [validators.optional(), validators.length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter asset amount.')])
    e_timespan = IntegerField('LifeSpanNumber')
    e_timespan_unit = SelectField('LifeSpanUnit', choices = timeSpanYears)
    paid_using = SelectField('Paid Using', choices = paid_using)

class CAForm(FlaskForm): 
    asset_name = StringField('Asset Name', validators = [InputRequired('Please enter the name of the asset.')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    asset_desc = TextAreaField('Description', [validators.optional(), validators.length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter asset amount.')])
    paid_using = SelectField('Paid Using', choices = paid_using)

class LTLiabForm(FlaskForm): 
    liab_name = StringField('Liability Name', validators = [InputRequired('Please enter liability name, e.g Notes Payable.')])
    person_owed = StringField('Creditor Name')
    loan_rate = DecimalField('Loan Rate', validators= [InputRequired('Please enter the interest rate at which the loan must be repaid, e.g. .10')])
    loan_periods = DecimalField('Loan Period', validators= [InputRequired("Please enter the number of " )])
    borrow_date = DateField('Loan Borrow Date', validators = [InputRequired('Please enter the date the loan was received.')])
    payment_start_date = DateField('Loan Payment Start Date', validators = [InputRequired('Please enter the date that repayment is expected to start.')])
    amount_borrowed = DecimalField('Amount Received', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])

class ExpForm(FlaskForm): 
    expense_name = StringField('Expense  Name', validators = [InputRequired('Please enter the name of the asset.')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    expence_desc = TextAreaField('Description', [validators.optional(), validators.length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])
    paid_using = SelectField('Paid Using', choices = paid_using)

class RevForm(FlaskForm): 
    revenue_name = StringField('Asset Name', validators = [InputRequired('Please enter the name of the asset.')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    revenue_desc = TextAreaField('Description', [validators.optional(), validators.length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])
    paid_using = SelectField('Paid Using', choices = paid_using)