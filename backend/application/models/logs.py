from datetime import datetime

from application import db
from application.models.users import User

class Log(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    affected_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    event_context  = db.Column(db.String(64), nullable = False)
    component = db.Column(db.String(64), nullable = False)
    event_name = db.Column(db.String(64), nullable = False)
    description = db.Column(db.String(64), nullable = False)
    ip_address = db.Column(db.String(64), nullable = False)