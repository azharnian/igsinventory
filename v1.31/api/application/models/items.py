from datetime import datetime

from application import db
# from application.models.users import User

class ItemType(db.Model):
    __tablename__ = "item_type"

    id = db.Column(db.Integer, primary_key = True)
    name_type = db.Column(db.String(256), nullable = False)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())
    date_updated = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    items = db.relationship("Item", backref="item_category", lazy = True)


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(256), nullable = False, unique = True)
    length = db.Column(db.Float, default = 0)
    width = db.Column(db.Float, default = 0)
    height = db.Column(db.Float, default = 0)
    weight = db.Column(db.Float, default = 0)
    color = db.Column(db.String(128))
    photo_item = db.Column(db.String(256), default = "default.jpg")
    is_electronic = db.Column(db.Boolean, default = False)
    is_waterresistant = db.Column(db.Boolean, default = False)
    price = db.Column(db.Float, default = 0)
    make = db.Column(db.String(256))
    model = db.Column(db.String(256))
    store = db.Column(db.String(256))
    volume_cc = db.Column(db.Float, default = 0)
    material = db.Column(db.String(256))
    machine_number = db.Column(db.String(256))
    police_state_number = db.Column(db.String(256))
    serial_number = db.Column(db.String(256))
    date_purchased = db.Column(db.DateTime, default = datetime.utcnow())
    budget_type = db.Column(db.String(256), default = "Dana Masyarakat")
    origin_country = db.Column(db.String(256), default = "Indonesia")
    percent_depreciation_per_year = db.Column(db.Float, default = 0)
    percent_demage = db.Column(db.Float, default = 0)
    is_available = db.Column(db.Boolean, default = True)
    is_broken = db.Column(db.Boolean, default = False)
    is_active = db.Column(db.Boolean, default = True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())
    date_updated = db.Column(db.DateTime)
    photo_location = db.Column(db.String(256), default = "default.jpg")
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable = False)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    name_type_id = db.Column(db.Integer, db.ForeignKey("item_type.id"), nullable = False)
    description = db.Column(db.Text)

    items_transfered = db.relationship("Transfer", backref = "items_transfered", lazy = True)

    items_updated = db.relationship("Update", backref = "items_updated", lazy = True)