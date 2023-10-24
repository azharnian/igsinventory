from datetime import datetime

from application import db
from application.models.users.users import *

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.String(256), unique = True, nullable = False)
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default = True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())
    date_updated = db.Column(db.DateTime)

    users = db.relationship("User", backref="user_in_roles", lazy = True)

    def __repr__(self):
        return f"User {self.id} role as {self.role} : {self.description}, active since {self.date_created}, last update on {self.date_updated}"