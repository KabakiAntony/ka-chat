from flask import render_template, redirect, url_for, flash
from passlib.hash import pbkdf2_sha256
from app.api import users
from app.api.models.users import User
from app.api.models import db
from app.api.models.form_fields import (
    RegistrationForm,
    LoginForm,
    # ResetPasswordLinkForm,
    # UpdatePasswordForm
)
from flask_login import (
    login_user,
    current_user, logout_user
    )

# these are default rooms for a start
# we will eventually have the ability to create rooms
# and moderate them.
ROOMS = ["lounge", "news", "games", "coding"]


@users.route('/', methods=['GET', 'POST'])
def index():
    """ registration route also the root of the app """
    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        email = reg_form.email.data
        password = reg_form.password.data

        hashed_pass = pbkdf2_sha256.hash(password)   

        new_user = User(username=username, email=email, password=hashed_pass)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful, Please login", 'success')
        # I will add ability to send emails on successful registration
        # so this flash message will be replaced with that
        # but in the mean time this stays for testing purposes.

        return redirect(url_for('login'))
  
    return render_template("index.html", form=reg_form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    """ login a user"""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(
            username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))

    return render_template("login.html", form=login_form)


@users.route("/chat", methods=['GET', 'POST'])
def chat():
    if not current_user.is_authenticated:
        flash('Please login', 'danger')
        return redirect(url_for('login'))

    return render_template(
        'chat.html', username=current_user.username, rooms=ROOMS)


@users.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('You have logged out successfully', 'success')
    return redirect(url_for('login'))