from datetime import datetime

from . import db, MAX_LENGTH_SHORT_ID, MAX_LENGTH_LONG_LINK


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LENGTH_LONG_LINK), nullable=False)
    short = db.Column(db.String(MAX_LENGTH_SHORT_ID), unique=True, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return {'url': self.original}
