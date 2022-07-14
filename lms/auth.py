#authentication routes for the applucation
from flask import Blueprint, render_template, request, redirect, url_for, flash

#initialize the blueprint
auth = Blueprint('auth', __name__)

#route for login
@auth.route('/login')
def login():
    return render_template('/login.html')

@auth.route('/addUser')
def addUser():
    return 'add user'

@auth.route('/logout')
def logout():
    return 'log out'