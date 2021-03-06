import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')
    MYSQL_TABLE = os.environ.get('MYSQL_TABLE')

    SQLALCHEMY_DATABASE_URI += MYSQL_USER
    SQLALCHEMY_DATABASE_URI += ':' + MYSQL_PASSWORD
    SQLALCHEMY_DATABASE_URI += '@' + MYSQL_HOST
    SQLALCHEMY_DATABASE_URI += ':' + MYSQL_PORT
    SQLALCHEMY_DATABASE_URI += '/' + MYSQL_TABLE

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')