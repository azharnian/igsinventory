from datetime import datetime

from application import db
from application.models.users.users import *
from application.models.items.items import *

class Update(db.Model):
    __tablename__ = "updates"
    
    id = db.Column(db.Integer, primary_key = True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable = False)
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    date_updated = db.Column(db.DateTime, default = datetime.utcnow())
    is_valid = db.Column(db.Boolean, default = True)
    update_detail = db.Column(db.Text)