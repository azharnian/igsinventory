from datetime import datetime

from application import db
from application.models.users.users import *

class Component(db.Model):
    # User, Location, Activity, Log
    __tablename__ = "components"
    id = db.Column(db.Integer, primary_key=True)
    component_name = db.Column(db.String(256), unique=True, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    note = db.Column(db.String(256))