from datetime import datetime

from application import db
from application.models.users.users import *
from application.models.items.items import *

class Item_Type(db.Model):
    __tablename__ = "item_type"

    id = db.Column(db.Integer, primary_key = True)
    name_type = db.Column(db.String(256), nullable = False)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())
    date_updated = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    items = db.relationship("Item", backref="items_in_category", lazy = True)

    def __repr__(self):
        return f"User : {self.id} - {self.code} - {self.name}"
