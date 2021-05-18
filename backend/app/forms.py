from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField,IntegerField, DateField, DecimalField
from wtforms import TextAreaField, StringField, PasswordField, SubmitField , SelectField, RadioField
from wtforms.validators import InputRequired, Email, Length, optional
from flask_wtf.file import FileField, FileAllowed, FileRequired

class LoginForm(FlaskForm):
    email = EmailField('Email', validators = [InputRequired('Please enter your email address e.g. johndoe@XXXX.XXX.'), Email()])
    password = PasswordField('Password', validators = [InputRequired('Please enter a password.')]) 

class RegisterForm(FlaskForm):
    first_name = StringField('first Name', validators=[InputRequired('Please enter your first name, e.g. John.')])
    last_name = StringField('last Name', validators=[InputRequired('Please enter your last name, e.g. Doe.')])
    email = EmailField('Email', validators = [InputRequired('Please enter your email address, e.g. johndoe@XXXX.XXX'), Email()])
    password = PasswordField('Password', validators=[InputRequired('Please enter a password.')])
    business_name = StringField('Business Name', validators=[InputRequired('Please enter your business name.')])
    
class NewProductForm(FlaskForm):
    product_name = StringField('Product Name', validators=[InputRequired('Please enter the product name, e.g. x shampoo.')])
    quantity = StringField('Quantity', validators=[InputRequired('Please enter the quantity')])
    man_units = StringField('Manufacture Units', validators=[InputRequired('Please enter the unit of measurement')])
    unit_price = StringField('Unit Price', validators=[InputRequired('Please enter the unit price')])
    tax = StringField('Tax Percent', validators=[InputRequired('Please enter the tax percent')])
    status = StringField('Product Status', validators=[InputRequired('Please enter the product status')])
    image = FileField('Image', validators=[FileAllowed(['jpg','jpeg','png'], 'Images only!')])


class orderForm(FlaskForm):
    fname = StringField('first Name', validators=[InputRequired('First name field should not be empty')])
    lname = StringField('last Name', validators=[InputRequired('Last Name field should not be empty')])
    trn = StringField('trn', validators=[InputRequired('TRN field should not be empty')])
    address = StringField('Address', validators=[InputRequired('Please enter your your address')])
    phone_num = StringField ('Telephone', validators =[InputRequired('Please enter your your phone number')])
    email = EmailField('Email', validators = [InputRequired('Email Field should not be  empty'), Email()])
    # submit = SubmitField('Submit')

class ProofOfPaymentForm(FlaskForm): 
    pass

class ContactForm(FlaskForm):
    pass

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

paid_using = [('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Credit', 'Credit')]
bought_sold= [('Bought Asset', 'Bought Asset'), ('Sold Asset', 'Sold Asset')]
increase_decrease= [('Increase', 'Increase'), ('Decrease', 'Decrease')]
expense_type= [('Operating Expense', 'Operating Expense'), ('Non Operating Expense', 'Non Operating Expense')]
revenue_type= [('Operating Revenue', 'Operating Revenue'), ('Non Operating Revenue', 'Non Operating Revenue')]
tan_in= [('Tangible Asset', 'Tangible Asset'), ('Intangible Asset', 'Intangible Asset')]
nca_tags= [
            ('Property, Plant & Equipment', 'Property, Plant & Equipment'), 
            ('Intangible Assets', 'Intangible Assets'),
            ('Investments', 'Investments'),
            ('Other Non Current Assets', 'Other Non Current Assets'),
        ]
ca_tags= [
        ('Inventory', 'Inventory'), 
        ('Cash', 'Cash'),
        ('Cash Equivalents', 'Cash Equivalents'),
        ('Accounts Receivables', 'Accounts Receivables'),
        ('Prepaid Expenses', 'Prepaid Expenses'),
        ('Marketable Securities', 'Marketable Securities'),
        ('Other Current Assets', 'Other Current Assets'),
    ]
cl_tags= [
        ('Accounts Payable', 'Accounts Payable'), 
        ('Accrued Expenses', 'Accrued Expenses'),
        ('Short Term Loans', 'Short Term Loans'),
        ('Other Current Liabilities', 'Other Current Liabilities'),
        
]
ltl_tags= [
        ('Long Term Loans', 'Long Term Loans'), 
        ('', 'Accrued Expenses'),
        ('Short Term Loans', 'Short Term Loans'),
        ('Other Long Term Liabilities', 'Other Long Term Liabilities'),
        
]

class NCAForm(FlaskForm): 
    asset_name = StringField('Asset Name', validators = [InputRequired('Please enter the name of the asset, e.g. Motor Vehicle')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    due_date = DateField('Due Date', validators = [InputRequired('Please Enter a due date for payment on credit.')])
    dep_type = SelectField('Depreciation Type', choices = dep_types_list)
    asset_desc = TextAreaField('Description', validators = [optional(), Length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter asset amount.')])
    salvage_val = DecimalField('Salvage Value', places=2, rounding=None, validators = [InputRequired('Please enter salvage value amount')])
    asset_lifespan = IntegerField('LifeSpanNumber')
    totalUnits = IntegerField('Total Units')
    tan_in = RadioField("Tangible or Intangible", choices = tan_in)
    bought_sold = RadioField('Bought or Sold', choices = bought_sold)
    paid_using = RadioField('Paid Using', choices = paid_using)
    tag = SelectField('Tag', choices= nca_tags)

class CAForm(FlaskForm): 
    asset_name = StringField('Asset Name', validators = [InputRequired('Please enter the name of the asset.')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    asset_desc = TextAreaField('Description', validators = [optional(), Length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter asset amount.')])
    asset_lifespan = IntegerField('LifeSpanNumber')
    loan_period = IntegerField('Loan Period')
    increase_decrease = RadioField('Increase or Decrease', choices = increase_decrease)
    paid_using = SelectField('Paid Using', choices = paid_using)
    tag = SelectField('Tag', choices= ca_tags)

class LTLiabForm(FlaskForm): 
    liab_name = StringField('Liability Name', validators = [InputRequired('Please enter liability name, e.g Notes Payable.')])
    person_owed = StringField('Creditor Name', validators = [optional()])
    loan_rate = DecimalField('Loan Rate', validators= [InputRequired('Please enter the interest rate at which the loan must be repaid, e.g. .10')])
    loan_periods = DecimalField('Loan Period', validators= [InputRequired("Please enter the number of " )])
    borrow_date = DateField('Loan Borrow Date', validators = [InputRequired('Please enter the date the loan was received.')])
    payment_start_date = DateField('Loan Payment Start Date', validators = [InputRequired('Please enter the date that repayment is expected to start.')])
    amount_borrowed = DecimalField('Amount Received', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])
    account_affected= SelectField('Paid Using', choices = paid_using)
    increase_decrease = RadioField('Increase or Decrease', choices = increase_decrease)
    tag = SelectField('Tag', choices= ltl_tags)

class CLiabForm(FlaskForm): 
    liab_name = StringField('Liability Name', validators = [InputRequired('Please enter liability name, e.g Notes Payable.')])
    person_owed = StringField('Creditor Name', validators = [optional()])
    loan_rate = DecimalField('Loan Rate', validators= [InputRequired('Please enter the interest rate at which the loan must be repaid, e.g. .10')])
    loan_periods = DecimalField('Loan Period', validators= [InputRequired("Please enter the number of " )])
    borrow_date = DateField('Loan Borrow Date', validators = [InputRequired('Please enter the date the loan was received.')])
    payment_start_date = DateField('Loan Payment Start Date', validators = [InputRequired('Please enter the date that repayment is expected to start.')])
    amount_borrowed = DecimalField('Amount Received', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])
    tag = SelectField('Tag', choices= cl_tags)

class ExpForm(FlaskForm): 
    expense_name = StringField('Expense  Name', validators = [InputRequired('Please enter the name of the asset.')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    expense_type = RadioField('Expense Type', choices = expense_type)
    expense_desc = TextAreaField('Description', validators = [optional(), Length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])
    paid_using = SelectField('Paid Using', choices = paid_using)
    increase_decrease = RadioField('Increase or Decrease', choices = increase_decrease)
    # tag = SelectField('Tag', choices= nca_tags)
    
class RevForm(FlaskForm): 
    revenue_name = StringField('Asset Name', validators = [InputRequired('Please enter the name of the asset.')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please Enter a transaction date.')])
    revenue_type = RadioField('Revenue Type', choices = revenue_type)
    revenue_desc = TextAreaField('Description', validators = [optional(), Length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])
    paid_using = SelectField('Paid Using', choices = paid_using)
    increase_decrease = RadioField('Increase or Decrease', choices = increase_decrease)
    #   tag = SelectField('Tag', choices= nca_tags)

class EquityForm(FlaskForm): 
    equity_name = StringField('Equity Name', validators = [InputRequired('Please enter the equity name')])
    transaction_date = DateField('Transaction Date', validators = [InputRequired('Please enter a transaction date')])
    equity_desc = TextAreaField('Description', validators = [optional(), Length(max=200)])
    amount = DecimalField('Amount', places=2, rounding=None, validators = [InputRequired('Please enter expense amount.')])
    paid_using = SelectField('Paid Using', choices = paid_using)
    increase_decrease = RadioField('Increase or Decrease', choices = increase_decrease)
    #   tag = SelectField('Tag', choices= nca_tags)
