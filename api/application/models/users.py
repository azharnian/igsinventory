from datetime import datetime
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer

from flask import current_app, jsonify
from flask_restx import fields
from flask_login import UserMixin

from sqlalchemy.exc import SQLAlchemyError

from application import db, login_manager
from application.models.model import Base
from application.models.locations import *
from application.models.activities import *
from application.models.items import *
from application.models.logs import *

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

user_role_model_json = {
        "id": fields.Integer(),
        "role" : fields.String(),
        "description" : fields.String(),
        "is_active" : fields.Boolean(),
        "date_created" : fields.DateTime(dt_format="rfc822"),
        "date_updated" : fields.DateTime(dt_format="rfc822"),
    }

class User_Role(db.Model, Base):
    __tablename__ = "user_role"

    id = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.String(256), unique = True, nullable = False)
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default = True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())
    date_updated = db.Column(db.DateTime)

    users = db.relationship("User", backref="user_in_roles", lazy = True)

    def __repr__(self):
        return f"User {self.id} role as {self.role} : {self.description}, active since {self.date_created}, last update on {self.date_updated}"

    def update(self, role, description):
        self.role = role
        self.description = description
        self.date_updated = datetime.utcnow()
        db.session.commit()


user_model_json = {
    "id" : fields.Integer(),
    "username" : fields.String(),
    "email" : fields.String(),
    "phone" : fields.String(),
    "password" : fields.String(),
    "first_name" : fields.String(),
    "last_name" : fields.String(),
    "full_name" : fields.String(),
    "role" : fields.Integer(),
    "is_active" : fields.Boolean(),
    "date_created" : fields.DateTime(dt_format="rfc822"),
    "date_updated" : fields.DateTime(dt_format="rfc822"),
    "profile_picture" : fields.String(),
    "is_login" : fields.Boolean(),
    "is_email_verified" : fields.Boolean(),
    "is_phone_verified" : fields.Boolean(),
    "last_login" : fields.DateTime(dt_format="rfc822"),
    "last_ip" : fields.String()
}

class User(db.Model, Base, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(256), unique = True, nullable = False)
    email = db.Column(db.String(256), unique = True, nullable = False)
    phone = db.Column(db.String(256), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    first_name = db.Column(db.String(128), nullable = False)
    last_name = db.Column(db.String(128), nullable = False)
    full_name = db.Column(db.String(256), nullable = False)
    role = db.Column(db.Integer, db.ForeignKey("user_role.id"), nullable = False)
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

    buildings = db.relationship("Building", backref = "creator_buildings", lazy = True)

    floors = db.relationship("Floor", backref = "creator_floors", lazy = True)

    locations = db.relationship("Location", backref = "creator_locations", lazy = True)

    type_items = db.relationship("Item_Type", backref = "creator_item_types", lazy = True)

    items = db.relationship("Item", backref = "creator_items", lazy = True)

    item_transfers = db.relationship("Transfer", backref = "transfered_executor", lazy = True)
    
    item_updates = db.relationship("Update", backref = "updated_executor", lazy = True)

    logs = db.relationship("Log", foreign_keys = "Log.user_id", backref = "logs_user", lazy = True)

    logs_affected = db.relationship("Log", foreign_keys = "Log.affected_user_id", backref = "affedted_logs_user", lazy = True)


    def __repr__(self):
        return f"User : {self.id} - {self.username} - {self.full_name} - {self.role} - {self.active}"
    
    def save(self):
        try:
            self.full_name = f"{self.first_name} {self.last_name}"
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            response = {
                    "status" : "failed",
                    "orig" : str(e.orig),
                    "statement" : str(e.statement),
                    "params" : str(e.params),
                    "ismulti" : str(e.ismulti)
            }
            return response
        else:
            return {"status" : "success"}


    def get_reset_token(self, expires_sec=120):
        serializer = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        token = serializer.dumps({"user_id":self.id}).decode("utf-8")

        return token

    @staticmethod
    def verify_reset_token(token):
        serial = Serializer(current_app.config["SECRET_KEY"])

        try:
            user_id = serial.loads(token)["user_id"]
        except:
            return None
        return User.query.get(user_id)
