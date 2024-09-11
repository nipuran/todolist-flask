from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


""" Register Form """
class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), 
        Length(min=6), 
        EqualTo('password', message='Passwords must match')
    ])
    signup = SubmitField('Sign Up')


""" Verify Form """
class VerifyForm(FlaskForm):
    otp = StringField('OTP', validators=[DataRequired()])
    verify = SubmitField('Verify')


""" Forget Password Form """
class ForgetPasswordForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


""" New Password Form """
class NewPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Submit')


""" Login Form """
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Log In')
