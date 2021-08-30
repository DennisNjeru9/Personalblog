from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Email,Length,EqualTo
from ..models import User

class SignUpForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter your username',validators=[DataRequired()])
    password = PasswordField('PasswordField',validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('That email is associated with an existing account')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember_me = BooleanField('Keep me loggin in')
    submit = SubmitField('Log In')