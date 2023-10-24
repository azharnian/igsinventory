from datetime import datetime

from application import db
from application.models.users.users import *
from application.models.locations.floors import *

class Room(db.Model):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(256))
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    room_code = db.Column(db.String(256), unique=True, nullable=False)
    room_name = db.Column(db.String(256), nullable=False)
    floor_id = db.Column(db.Integer, db.ForeignKey("floors.id"), nullable=False, default=0)

    def __repr__(self):
        return f"Floor : {self.id} - {self.room_code} - {self.room_name} - ({self.floor_id})"