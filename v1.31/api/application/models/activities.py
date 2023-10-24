from datetime import datetime

from application import db
# from application.models.users import User

class Transfer(db.Model):
    __tablename__ = "transfers"

    id = db.Column(db.Integer, primary_key = True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable = False)
    origin_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable = False)
    destination_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable = False)
    date_transfered = db.Column(db.DateTime, default = datetime.utcnow())
    transfered_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    is_valid = db.Column(db.Boolean, default = True)
    reason = db.Column(db.Text)
    note = db.Column(db.Text)



class Update(db.Model):
    __tablename__ = "updates"
    
    id = db.Column(db.Integer, primary_key = True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable = False)
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    date_updated = db.Column(db.DateTime, default = datetime.utcnow())
    is_valid = db.Column(db.Boolean, default = True)
    update_detail = db.Column(db.Text)