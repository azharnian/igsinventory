from datetime import datetime

from application import db
# from application.models.users import *

class Building(db.Model):
    __tablename__ = "buildings"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), nullable = False)
    address = db.Column(db.String(256), nullable = False)
    rt = db.Column(db.String(3), default="00")
    rw = db.Column(db.String(3), default="00")
    kelurahan = db.Column(db.String(256), nullable = False)
    kecamatan = db.Column(db.String(256), nullable = False)
    kota = db.Column(db.String(256), nullable = False)
    provinsi = db.Column(db.String(256), nullable = False)
    zip_code = db.Column(db.String(6))
    photo_location = db.Column(db.String(256), default="default.jpg")
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    date_updated = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    floors = db.relationship("Floor", backref = "floors_in_buildings", lazy = True)


class Floor(db.Model):
    __tablename__ = "floors"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), nullable = False)
    description = db.Column(db.Text)
    buildings = db.Column(db.Integer, db.ForeignKey("buildings.id"), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())
    date_updated = db.Column(db.DateTime)
    photo_location = db.Column(db.String(256), default = "default.jpg")
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    locations = db.relationship("Location", backref = "location_in_floor", lazy = True)


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), nullable = False)
    description = db.Column(db.Text)
    floor = db.Column(db.Integer, db.ForeignKey("floors.id"), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())
    date_updated = db.Column(db.DateTime)
    photo_location = db.Column(db.String(256), default = "default.jpg")
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    origin_items_transfered = db.relationship("Transfer", foreign_keys = "Transfer.origin_id", backref = "origin_items_transfered", lazy = True)

    destination_items_transfered = db.relationship("Transfer", foreign_keys = "Transfer.destination_id", backref = "destination_items_transfered", lazy = True)

    