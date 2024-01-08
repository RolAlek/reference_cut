import string

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings import Config


PATTERN = '^[a-zA-Z0-9]+$'
MAX_LENGTH_SHORT_ID = 16
MAX_LENGTH_LONG_LINK = 256
SYMBOLS = string.ascii_letters + string.digits
LENGTH_SHORT_ID = 6

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


from . import api_views, error_handlers, views
