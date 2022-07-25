#creating the database
from flask_login import UserMixin #This provides default implementations for the methods that Flask-Login expects user objects to have.
from . import db

#table for userDetails
class UserDetails(UserMixin, db.Model):
    #id column
    userId = db.Column(db.Integer, primary_key = True)
    #username column
    userName = db.Column(db.String(50), nullable = False)
    #email column
    userEmail = db.Column(db.String(100), unique = True)
    #password column
    userPassword = db.Column(db.String(12), nullable = False)

#table for the bookDetails
class BookDetails(UserMixin, db.Model):
    #id column
    bookID = db.Column(db.String(20), primary_key = True, unique = True)
    #title column
    bookTitle = db.Column(db.String(200), nullable = False)
    #tape number
    tapeNumber = db.Column(db.String(8), nullable = False)
    #shelf number
    shelfNumber = db.Column(db.String(12), nullable = False)
    #creating a one to many relationship
    borrowerName = db.relationship('BorrowerDetails', backref='BookDetails')

#table for the borrower details
class BorrowerDetails(UserMixin, db.Model):
    #borrower name column
    borrowerName = db.Column(db.String(75), primary_key = True, nullable = False)
    #phone number column
    phoneNumber = db.Column(db.String(10), nullable = False)
    #address
    residentialAddress = db.Column(db.String(500), nullable = False)
    #book title
    bookTitle = db.Column(db.String(200), nullable = False)
    #tape Number
    tapeNumber = db.Column(db.String(8), nullable = False)
    #date of issue
    dateOfIssue = db.Column(db.Text, nullable = False)
    #creating foreign key to link the book details table
    bookID = db.Column(db.String, db.ForeignKey('BookDetails.bookID'))