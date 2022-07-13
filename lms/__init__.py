#for setting up the application
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

    #register the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #register the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app