from datetime import datetime

from application import db
from application.models.users.users import *
from application.models.locations.buildings import *
from application.models.locations.rooms import *

class Floor(db.Model):
    __tablename__ = "floors"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), nullable = False)
    description = db.Column(db.Text)
    building_id = db.Column(db.Integer, db.ForeignKey("buildings.id"), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())
    date_updated = db.Column(db.DateTime)
    photo_location = db.Column(db.String(256), default = "default.jpg")
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    rooms = db.relationship("Room", backref = "rooms_in_floor", lazy = True)

    def __repr__(self):
        return f"Floor : {self.id} - {self.name} - ({self.building_id})"

