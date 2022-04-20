from .users import User
from passlib.hash import pbkdf2_sha256
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError


def invalid_credentials(form, field):
    """"Username and password validator"""
    username_entered = form.username.data
    password_entered = field.data

    user_object = User.query.filter_by(username=username_entered).first()
    if not user_object:
        raise ValidationError("Username and or password is incorrect.")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Username and or password is incorrect.")


class RegistrationForm(FlaskForm):
    """ we define registration form"""
    username = StringField('Username', validators=[
        InputRequired(message="Username Required"),
        Length(min=6, max=25, 
        message="Username must be between 6 and 25 characters")])
    email = EmailField('Email', validators=[
        InputRequired(message="Email is Required")])
    password = PasswordField('Password', validators=[
        InputRequired(message="Password is required"),
        Length(min=6, max=25, 
        message="Password must be between 6 and 25 characters")])
    
    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already taken, Select a different one.")


class LoginForm(FlaskForm):
    """login form"""
    username = StringField('Username', validators=[
        InputRequired(message="Username required")])
    password = PasswordField('Password', validators=[
        InputRequired(message="Password Required"), invalid_credentials])


class ResetPasswordLinkForm(FlaskForm):
    """ reset link form"""
    email = EmailField('Email', validators=[
        InputRequired(message="Email is Required")])


class UpdatePasswordForm(FlaskForm):
    """ update password form"""
    password = PasswordField('Password', validators=[
        InputRequired(message="Password Required")])
