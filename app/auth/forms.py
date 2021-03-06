from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Enter your email address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('password',validators = [Required(), EqualTo('password_confirm', message = 'Password must match')])
    password_confirm = PasswordField('Confirm your passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data.feild.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Enter your  email address', validators=[Required(),Email()])
    password = PasswordField('password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')