from flask import render_template, redirect, url_for, flash, session
from flask_mail import Message
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User
from app.extensions import db, bcrypt, mail
from app.utils import generate_otp, send_otp_email
from .forms import RegisterForm, VerifyForm, ForgetPasswordForm, NewPasswordForm, LoginForm
from . import auth_bp


@auth_bp.route("/register_user", methods=["POST", "GET"])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        is_exist_email = User.query.filter_by(email=email).first()
        is_exist_username = User.query.filter_by(username=username).first()
        if is_exist_email or is_exist_username:
            return render_template("register_user.html", form=form)
        new_user = User(email=email, username=username, password=pw_hash)
        session['new_user'] = new_user
        session['otp'] = generate_otp()
        send_otp_email(email, session['otp'])
        session['origin'] = 'register_user'
        return redirect(url_for("auth_bp.verify_otp") )
    return render_template("register_user.html", form=form)


@auth_bp.route("/verify_otp", methods=["GET", "POST"])
def verify_otp():
    form = VerifyForm()
    if form.validate_on_submit():
        otp = int(form.otp.data)
        if otp == session["otp"]:
            session['otp'] = None
            if session['origin'] == 'register_user':
                new_user = session['new_user']
                db.session.add(new_user)
                db.session.commit()
                session['new_user'] = None
                return redirect(url_for('auth_bp.user_login'))
            elif session['origin'] == 'forget_password':
                return redirect(url_for('auth_bp.reset_password'))
    return render_template("verify_otp.html", form=form)


@auth_bp.route("/forget_password", methods=["GET", "POST"])
def forget_password():
    form = ForgetPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            session['email'] = email
            session['otp'] = generate_otp()
            send_otp_email(email, session['otp'])
            session['origin'] = 'forget_password'
            return redirect(url_for("auth_bp.verify_otp"))
    return render_template("forget_password.html", form=form)


@auth_bp.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    form = NewPasswordForm()
    if form.validate_on_submit():
        new_password = form.password.data
        email = session['email']
        user = User.query.filter_by(email=email).first()
        user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        db.session.commit()
        session['email'] = None
        return redirect(url_for('auth_bp.user_login'))
    return render_template("reset_password.html", form=form)


@auth_bp.route("/user_login", methods=["GET", "POST"])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard_bp.dashboard'))
    return render_template("user_login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.user_login'))
