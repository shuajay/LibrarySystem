#authentication routes for the applucation
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from . import db
from .models import UserDetails

#initialize the blueprint
auth = Blueprint('auth', __name__)

#route for login
@auth.route('/login')
def login():
    return render_template('/login.html')

@auth.route('/login', methods=['POST'])
def login_post():

    userEmail = request.form.get('userEmail')
    userPassword = request.form.get('userPassword')
    remember = True if request.form.get('remember') else False

    user = UserDetails.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('USERNAME OR PASSWORD IS INCORRECT')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember, duration=None)
    redirect(url_for('main.home'))

@auth.route('/addUser')
def addUser():
    return 'add user'

@auth.route('/logout')
def logout():
    return 'log out'