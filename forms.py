from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms import validators
from wtforms.validators import DataRequired, Email
import re

class LoginForm(FlaskForm):

    __data_required_message = "This field is required";

    username = StringField('Username', 
                            validators=[DataRequired(__data_required_message)],
                            render_kw={'class': 'form-control'})
    
    password = PasswordField('Password', 
                            validators=[DataRequired(__data_required_message)],
                            render_kw={'class': 'form-control'})
    

class CreateAccount(FlaskForm):

    __data_required_message = "This field is required";
    __email_valid_message = "This field requires a valid email"
    __error_class = ''

    def __password_validation(form, field):
        
        if len(field.data) < 8:
            raise validators.ValidationError("The password must be 8 or more characters")

    #this methos validates if the input text has numbers
    def __text_validation(form, field):
        if re.search('[0-9]', field.data):
            raise validators.ValidationError("The name couldn't has numbers")

    name = StringField('Name', 
                        validators=[DataRequired(__data_required_message), __text_validation],
                        render_kw={'class': 'form-control', 'id':'input'})

    surnames = StringField('Surnames', 
                            validators=[DataRequired(__data_required_message), __text_validation], 
                            render_kw={'class': 'form-control'})

    age = StringField('Age', render_kw={'class': 'form-control'})
    
    email = StringField('E-mail', 
                        validators=[DataRequired(__data_required_message), Email(__email_valid_message)],
                        render_kw={'class': 'form-control'})
    
    password = PasswordField('Password', 
                        validators=[DataRequired(), __password_validation],
                        render_kw={'class': 'form-control', 'id': 'input'})

    user_name = StringField('User Name', 
                        validators=[DataRequired(__data_required_message)],
                        render_kw={'class': 'form-control'})