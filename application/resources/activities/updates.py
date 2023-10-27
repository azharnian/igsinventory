from application import db
from application.models.activities.updates import Update

def create_update(update_data):
    new_update = Update(
        item_id=update_data["item_id"],
        updated_by=update_data["updated_by"],
        update_detail=update_data.get("update_detail"),
    )
    db.session.add(new_update)
    db.session.commit()
    return new_update

def get_all_updates():
    return Update.query.all()

def get_update_by_id(update_id):
    return Update.query.get(update_id)

def update_update(update_id, update_data):
    update = Update.query.get(update_id)
    if update:
        update.item_id = update_data["item_id"]
        update.updated_by = update_data["updated_by"]
        update.update_detail = update_data.get("update_detail", update.update_detail)
        db.session.commit()
        return update
    return None

def delete_update(update_id):
    update = Update.query.get(update_id)
    if update:
        db.session.delete(update)
        db.session.commit()
        return True
    return False