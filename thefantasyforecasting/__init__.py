from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from thefantasyforecasting.config import Config


bcrypt = Bcrypt()
mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'account.login'
login_manager.login_message = 'info'
admin = Admin()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    bcrypt.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    from thefantasyforecasting.account.routes import account
    from thefantasyforecasting.bulletin.routes import bulletin
    from thefantasyforecasting.challenge.routes import challenge
    from thefantasyforecasting.error.routes import error
    from thefantasyforecasting.extra.routes import extra
    from thefantasyforecasting.main.routes import main

    app.register_blueprint(account)
    app.register_blueprint(bulletin)
    app.register_blueprint(challenge)
    app.register_blueprint(error)
    app.register_blueprint(extra)
    app.register_blueprint(main)

    from thefantasyforecasting.models import User, ForecastEntry, ForecastPeriod, Post, Location

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(ForecastEntry, db.session))
    admin.add_view(ModelView(ForecastPeriod, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Location, db.session))

    return app