from datetime import datetime

from application import db
from application.models.users.users import *
from application.models.items.items import *

class Transfer(db.Model):
    __tablename__ = "transfers"

    id = db.Column(db.Integer, primary_key = True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable = False)
    origin_id = db.Column(db.Integer, db.ForeignKey("rooms.id"), nullable = False)
    destination_id = db.Column(db.Integer, db.ForeignKey("rooms.id"), nullable = False)
    date_transfered = db.Column(db.DateTime, default = datetime.utcnow())
    transfered_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    is_valid = db.Column(db.Boolean, default = True)
    reason = db.Column(db.Text)
    note = db.Column(db.Text)
