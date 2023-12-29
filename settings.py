from os import getenv


class Config(object):
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY', 'value does not exist')
