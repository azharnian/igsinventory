from datetime import datetime

from application import db
from application.models.users.roles import *
from application.models.locations.locations import *
from application.models.locations.buildings import *
from application.models.locations.floors import *
from application.models.locations.rooms import *
from application.models.activities.transfers import *
from application.models.activities.updates import *
from application.models.items.item_types import *
from application.models.items.items import *
from application.models.logs.logs import *

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(256), unique = True, nullable = False, index = True)
    email = db.Column(db.String(256), unique = True, nullable = False, index = True)
    phone = db.Column(db.String(256), nullable = False)
    password = db.Column(db.String(256), nullable = False)
    first_name = db.Column(db.String(128), nullable = False)
    last_name = db.Column(db.String(128), nullable = False)
    full_name = db.Column(db.String(256), nullable = False)
    role = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable = False)
    is_active = db.Column(db.Boolean, default = True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())
    date_updated = db.Column(db.DateTime)
    profile_picture = db.Column(db.String(256), default = "/profile_picture/default.jpg")
    is_login = db.Column(db.Boolean, default = False)
    is_email_verified = db.Column(db.Boolean, default = False)
    is_suspended = db.Column(db.Boolean, default = False)
    is_phone_verifed = db.Column(db.Boolean, default = False)
    last_login = db.Column(db.DateTime)
    last_ip = db.Column(db.String(64))

    locations = db.relationship("Location", backref = "creator_locations", lazy = True)
    buildings = db.relationship("Building", backref = "creator_buildings", lazy = True)
    floors = db.relationship("Floor", backref = "creator_floors", lazy = True)
    room = db.relationship("Room", backref="creator_rooms", lazy = True)
    item_types = db.relationship("Item_Type", backref = "creator_item_types", lazy = True)
    items = db.relationship("Item", backref = "creator_items", lazy = True)
    item_transfers = db.relationship("Transfer", backref = "transfered_executor", lazy = True)
    item_updates = db.relationship("Update", backref = "updated_executor", lazy = True)
    logs = db.relationship("Log", foreign_keys = "Log.user_id", backref = "logs_user", lazy = True)
    logs_affected = db.relationship("Log", foreign_keys = "Log.affected_user_id", backref = "affedted_logs_user", lazy = True)

    def __repr__(self):
        return f"User : {self.id} - {self.username} - {self.full_name} - {self.role} - {self.active}"