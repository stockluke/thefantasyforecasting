from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_login import UserMixin
from thefantasyforecasting import db, login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as TimedSignature
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class ForecastEntry(db.Model):
    __tablename__ = 'forecast_entry'

    id_forecast_entry = db.Column(db.Integer, primary_key=True, unique=True)
    id_user = db.Column(db.ForeignKey('user.id_user'), nullable=False, index=True)
    id_forecast_period = db.Column(db.ForeignKey('forecast_period.id_forecast_period'), nullable=False, index=True)
    submitted = db.Column(db.DateTime, nullable=False)
    predicting = db.Column(db.DateTime, nullable=False)
    temperature_low = db.Column(db.Integer)
    temperature_high = db.Column(db.Integer)
    wind_max = db.Column(db.Integer)
    precipitation_chance = db.Column(db.Numeric(2, 0))
    precipitation_amount = db.Column(db.Numeric(2, 0))

    forecast_period = db.relationship('ForecastPeriod', primaryjoin='ForecastEntry.id_forecast_period == ForecastPeriod.id_forecast_period', backref='forecast_entries')
    user = db.relationship('User', primaryjoin='ForecastEntry.id_user == User.id_user', backref='forecast_entries')


class ForecastPeriod(db.Model):
    __tablename__ = 'forecast_period'

    id_forecast_period = db.Column(db.Integer, primary_key=True, unique=True)
    location = db.Column(db.ForeignKey('location.id_location'), nullable=False, index=True)
    effective = db.Column(db.String(45, 'utf8_bin'), nullable=False, unique=True)

    location1 = db.relationship('Location', primaryjoin='ForecastPeriod.location == Location.id_location', backref='forecast_periods')


class Post(db.Model):
    __tablename__ = 'post'

    id_post = db.Column(db.Integer, primary_key=True, unique=True)
    id_user = db.Column(db.ForeignKey('user.id_user'), nullable=False, index=True)
    title = db.Column(db.String(45, 'utf8_bin'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.String(255, 'utf8_bin'), nullable=False)
    image = db.Column(db.String(45, 'utf8_bin'))
    category = db.Column(db.ForeignKey('post_category.id_post_category'), nullable=False, index=True)

    post_category = db.relationship('PostCategory', primaryjoin='Post.category == PostCategory.id_post_category', backref='posts')
    user = db.relationship('User', primaryjoin='Post.id_user == User.id_user', backref='posts')


class PostCategory(db.Model):
    __tablename__ = 'post_category'

    id_post_category = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(45, 'utf8_bin'), nullable=False, unique=True)


class Role(db.Model):
    __tablename__ = 'role'

    id_role = db.Column(db.String(45, 'utf8_bin'), primary_key=True, unique=True)


class User(db.Model):
    __tablename__ = 'user'

    id_user = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(45, 'utf8_bin'), nullable=False, unique=True)
    firstname = db.Column(db.String(45, 'utf8_bin'), nullable=False)
    lastname = db.Column(db.String(45, 'utf8_bin'), nullable=False)
    email = db.Column(db.String(255, 'utf8_bin'), nullable=False, unique=True)
    password = db.Column(db.String(60, 'utf8_bin'), nullable=False)
    role = db.Column(db.ForeignKey('role.id_role'), nullable=False, index=True, server_default=db.FetchedValue())
    timezone = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())

    role1 = db.relationship('Role', primaryjoin='User.role == Role.id_role', backref='users')

    def get_id(self):
        return self.id_user

    def get_reset_token(self, expires_sec=1800):
        ts = TimedSignature(current_app.config['SECRET_KEY'], expires_sec)
        return ts.dumps({'user_id': self.id_user}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        ts = TimedSignature(current_app.config['SECRET_KEY'])
        try:
            user_id = ts.loads(token)['user_id']
        except Exception as e:
            print(e)
            return None
        return User.query.get(user_id)


class Location(db.Model):
    __tablename__ = 'location'

    id_location = db.Column(db.Integer, primary_key=True, unique=True)
    icao = db.Column(db.String(45, 'utf8_bin'), nullable=False, unique=True)
    city = db.Column(db.String(45, 'utf8_bin'), nullable=False)
    state = db.Column(db.String(45, 'utf8_bin'), nullable=False)
    country = db.Column(db.String(45, 'utf8_bin'), nullable=False)