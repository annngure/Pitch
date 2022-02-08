from flask_wtf import FlaskForm
from wtforms import StringField,PasswordFeild,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordFeild('Password',validators = [Required(), EqualTo('password_confirm', message = 'Password must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up') 