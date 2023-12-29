from os import getenv


class Config(object):
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI', 'value does not exist')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY', 'value does not exist')
