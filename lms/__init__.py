from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#init the database
db = SQLAlchemy()

#application factory
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'bud1r1r0l1brary'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///librarymanagementsystem.sqlite'

    db.init_app(app)

    return app