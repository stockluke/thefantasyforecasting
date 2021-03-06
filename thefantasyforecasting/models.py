# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, MetaData, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from thefantasyforecasting import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class ForecastEntry(db.Model):
    __tablename__ = 'forecast_entry'

    id_forecast_entry = Column(Integer, primary_key=True, unique=True)
    id_user = Column(ForeignKey('user.id_user'), nullable=False, index=True)
    id_forecast_period = Column(ForeignKey('forecast_period.id_forecast_period'), nullable=False, index=True)
    submitted = Column(DateTime, nullable=False)
    predicting = Column(DateTime, nullable=False)
    temperature_low = Column(Integer)
    temperature_high = Column(Integer)
    wind_max = Column(Integer)
    precipitation_chance = Column(Numeric(2, 0))
    precipitation_amount = Column(Numeric(2, 0))

    forecast_period = relationship('ForecastPeriod', primaryjoin='ForecastEntry.id_forecast_period == ForecastPeriod.id_forecast_period', backref='forecast_entries')
    user = relationship('User', primaryjoin='ForecastEntry.id_user == User.id_user', backref='forecast_entries')


class ForecastPeriod(db.Model):
    __tablename__ = 'forecast_period'

    id_forecast_period = Column(Integer, primary_key=True, unique=True)
    location = Column(String(45, 'utf8_bin'), nullable=False)
    icao = Column(String(45, 'utf8_bin'), nullable=False)
    effective = Column(String(45, 'utf8_bin'), nullable=False, unique=True)


class Post(db.Model):
    __tablename__ = 'post'

    id_post = Column(Integer, primary_key=True, unique=True)
    id_user = Column(ForeignKey('user.id_user'), nullable=False, index=True)
    title = Column(String(45, 'utf8_bin'), nullable=False)
    date_posted = Column(DateTime, nullable=False)
    content = Column(String(255, 'utf8_bin'), nullable=False)
    image = Column(String(45, 'utf8_bin'))
    category = Column(String(45, 'utf8_bin'), nullable=False)

    user = relationship('User', primaryjoin='Post.id_user == User.id_user', backref='posts')


class Role(db.Model):
    __tablename__ = 'role'

    id_role = Column(String(45, 'utf8_bin'), primary_key=True, unique=True)


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True, unique=True)
    username = Column(String(45, 'utf8_bin'), nullable=False, unique=True)
    firstname = Column(String(45, 'utf8_bin'), nullable=False)
    lastname = Column(String(45, 'utf8_bin'), nullable=False)
    email = Column(String(255, 'utf8_bin'), nullable=False, unique=True)
    password = Column(String(60, 'utf8_bin'), nullable=False)
    role = Column(ForeignKey('role.id_role'), nullable=False, index=True, server_default=FetchedValue())

    role1 = relationship('Role', primaryjoin='User.role == Role.id_role', backref='users')

    def get_id(self):
        return self.id_user
