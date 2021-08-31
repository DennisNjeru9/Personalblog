from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired,Email,Length,EqualTo, Regexp
from ..models import User

class SignupForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Length (1, 64),Email()])
    username = StringField('Enter your username',validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('PasswordField',validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('That email is associated with an existing account')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember_me = BooleanField('Keep me loggin in')
    submit = SubmitField('Log In')