from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField,IntegerField, DateField, DecimalField
from wtforms import TextAreaField, StringField, PasswordField, SubmitField , SelectField, RadioField
from wtforms.validators import InputRequired, Email, Length, optional
from flask_wtf.file import FileField, FileAllowed, FileRequired


class RegisterForm(FlaskForm):
    first_name = StringField('first Name', validators=[InputRequired('Please enter your first name, e.g. John.')])
    last_name = StringField('last Name', validators=[InputRequired('Please enter your last name, e.g. Doe.')])
    email = EmailField('Email', validators = [InputRequired('Please enter your email address, e.g. johndoe@XXXX.XXX'), Email()])
    password = PasswordField('Password', validators=[InputRequired('Please enter a password.')])
    business_name = StringField('Business Name', validators=[InputRequired('Please enter your business name.')])
    
class LoginForm(FlaskForm):
    email = EmailField('Email', validators = [InputRequired('Please enter your email address e.g. johndoe@XXXX.XXX.'), Email()])
    password = PasswordField('Password', validators = [InputRequired('Please enter a password.')]) 

class orderForm(FlaskForm):
    fname = StringField('first Name', validators=[InputRequired('First name field should not be empty')])
    lname = StringField('last Name', validators=[InputRequired('Last Name field should not be empty')])
    trn = StringField('trn', validators=[InputRequired('TRN field should not be empty')])
    address = StringField('Address', validators=[InputRequired('Please enter your your address')])
    phone_num = StringField ('Telephone', validators =[InputRequired('Please enter your your phone number')])
    email = EmailField('Email', validators = [InputRequired('Email Field should not be  empty'), Email()])
    submit = SubmitField('Submit')

class websiteForm(FlaskForm):
    wel_head = StringField('Welcome Header', validators=[InputRequired('Welcome Header field should not be empty')])
    wel_mess = StringField('Welcome Message', validators=[InputRequired('Welcome Message field should not be empty')])
    prod_mess = StringField('Product Message', validators=[InputRequired('Product Message field should not be empty')])
    rec_head = StringField ('Receipt Header', validators =[InputRequired('Receipt Header field should not be empty')])
    rec_mess = StringField('Receipt Message', validators = [InputRequired('Receipt Message field should not be empty')])
    con_head = StringField('Contact Header', validators = [InputRequired('Contact Header field should not be empty')])
    con_mess = StringField('Contact Message', validators = [InputRequired('Contact Message field should not be empty')])
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

timeSpanYears = [
            ('Weeks', 'weeks'),
            ('Months', 'months'), 
            ('Years', 'years')
            ]

paid_using = [('By Cash', 'Cash'), ('By Cheque', 'Cheque'), ('On Credit', 'Credit')]
bought_sold= [('Bought Asset', 'Bought Asset'), ('Sold Asset', 'Sold Asset')]
tan_in= [('Tangible Asset', 'Tangible Asset'), ('Intangible Asset', 'Intangible Asset')]

"""
IT'S JUST LOGIC, you got this!
NEED TO HANDLE TYPE OF TRANSACTION: BOUGHT/SOLD, INCREASE/DECREASE 
this will help to determine whether the account is to be debited or credited 
- what will we use to determine operating versus non operating revenue and expense?

Look over the 7 classifications of general ledger 
How exactly will the general ledger be used to convert to financial statements 
General Legder should have the list of all accounts and their final balances that 
will be used to compute the statement

HOWEVER, the individual accounts will also be used to populate the dropdowns for each category 
So for each line item it should be account name and their final line balance.. and if it has a credit balance 
it should be bracketed. 
"""
class NCAForm(FlaskForm): 
    asset_name = StringField('Asset Name', validators = [InputRequired('Please enter the name of the asset, e.g. Motor Vehicle')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    dep_type = SelectField('Depreciation Type', choices = dep_types_list)
    dep_rate = DecimalField('Depreciation Rate', places=2, rounding=None, validators = [InputRequired('Please enter depreciation rate')])
    asset_desc = TextAreaField('Description', validators = [optional(), Length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter asset amount.')])
    asset_lifespan = IntegerField('LifeSpanNumber')
    tan_in = RadioField("Tangible or Intangible", choices = tan_in)
    bought_sold = RadioField('Bought or Sold', choices = bought_sold)
    paid_using = RadioField('Paid Using', choices = paid_using)

class CAForm(FlaskForm): 
    asset_name = StringField('Asset Name', validators = [InputRequired('Please enter the name of the asset.')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    asset_desc = TextAreaField('Description', validators = [optional(), Length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter asset amount.')])
    paid_using = SelectField('Paid Using', choices = paid_using)

class LTLiabForm(FlaskForm): 
    liab_name = StringField('Liability Name', validators = [InputRequired('Please enter liability name, e.g Notes Payable.')])
    person_owed = StringField('Creditor Name', validators = [optional()])
    loan_rate = DecimalField('Loan Rate', validators= [InputRequired('Please enter the interest rate at which the loan must be repaid, e.g. .10')])
    loan_periods = DecimalField('Loan Period', validators= [InputRequired("Please enter the number of " )])
    borrow_date = DateField('Loan Borrow Date', validators = [InputRequired('Please enter the date the loan was received.')])
    payment_start_date = DateField('Loan Payment Start Date', validators = [InputRequired('Please enter the date that repayment is expected to start.')])
    amount_borrowed = DecimalField('Amount Received', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])

class ExpForm(FlaskForm): 
    expense_name = StringField('Expense  Name', validators = [InputRequired('Please enter the name of the asset.')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    expence_desc = TextAreaField('Description', validators = [optional(), Length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])
    paid_using = SelectField('Paid Using', choices = paid_using)

class RevForm(FlaskForm): 
    revenue_name = StringField('Asset Name', validators = [InputRequired('Please enter the name of the asset.')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    revenue_desc = TextAreaField('Description', validators = [optional(), Length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])
    paid_using = SelectField('Paid Using', choices = paid_using)
