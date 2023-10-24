from datetime import datetime

from application import db
from application.models.users.users import *

class Event(db.Model):
    # create, read, update, delete, log in, log out, click
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    event_name = db.Column(db.String(256), uniqie=True, nullable=False)
    note = db.Column(db.String(256))