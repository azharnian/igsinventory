from datetime import datetime

from application import db
from application.models.users.users import *
from application.models.locations.floors import *

class Building(db.Model):
    __tablename__ = "buildings"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), nullable = False)
    address = db.Column(db.String(256), nullable = False)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable = False)
    rt = db.Column(db.String(3), default="00")
    rw = db.Column(db.String(3), default="00")
    kelurahan = db.Column(db.String(256), nullable = False)
    kecamatan = db.Column(db.String(256), nullable = False)
    city = db.Column(db.String(256), nullable = False)
    province = db.Column(db.String(256), nullable = False)
    zip_code = db.Column(db.String(6))
    photo_location = db.Column(db.String(256), default="default.jpg")
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    date_updated = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    floors = db.relationship("Floor", backref = "floors_in_building", lazy = True)

    def __repr__(self):
        return f"Building : {self.id} - {self.name} - ({self.location_id})"