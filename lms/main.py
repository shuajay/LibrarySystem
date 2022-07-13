#non auth routes for the app
from flask import Blueprint, render_template, request, redirect, url_for, flash


#initializing the blueprint
main = Blueprint('main', __name__)

#route for the landing page
@main.route('/')
def index():
    return 'Index'

@main.route('/home')
def homePage():
    return 'Homepage'

@main.route('/borrowBooks')
def borrowBooks():
    return 'Borrow books'

@main.route('/availableBooks')
def availableBooks():
    return 'available books'

@main.route('/borrowedBooks')
def borrowedBooks():
    return 'borrowed books'

@main.route('/addNewBook')
def addNewBook():
    return 'add new book'

