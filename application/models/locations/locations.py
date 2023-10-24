from datetime import datetime

from application import db
from application.models.users.users import *
from application.models.locations.buildings import *


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), nullable = False)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())
    date_updated = db.Column(db.DateTime)
    photo_location = db.Column(db.String(256), default = "default.jpg")
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    buildings = db.relationship("Building", backref = "buildings_in_location", lazy = True)

    def __repr__(self):
        return f"Location : {self.id} - {self.name} - ({self.longitude},{self.latitude})"

    