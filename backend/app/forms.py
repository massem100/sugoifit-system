from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField,IntegerField
from wtforms import TextAreaField, StringField, PasswordField, SubmitField 
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators = [InputRequired('Email Field should not be  empty'), Email()])
    password = PasswordField('password', validators=[InputRequired('Please enter a password.')])
    first_name = StringField('first Name', validators=[InputRequired('First name field should not be empty')])
    last_name = StringField('last Name', validators=[InputRequired('Last Name field should not be empty')])
    business_name = StringField('business name', validators=[InputRequired('Please enter your business name')])
    revenue = IntegerField ('revenue', validators =[InputRequired('If you have not started earning enter 0')])

class LoginForm(FlaskForm):
    email = EmailField('Email', validators = [InputRequired('Email Field should not be  empty'), Email()])
    password = PasswordField('Password', validators = [InputRequired('Please enter a password')]) 

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