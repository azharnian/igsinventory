from datetime import datetime

from application import db
from application.models.users.users import *
from application.models.logs.events import *
from application.models.logs.components import *

class Log(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    affected_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id", nullable=False))
    component_id = db.Column(db.Integer, db.ForeignKey("components.id", nullable=False))
    ip_address = db.Column(db.String(256), nullable=False)