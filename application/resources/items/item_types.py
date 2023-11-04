from application import db
from application.models.items.item_types import ItemType

def create_item_type(item_type_data):
    new_item_type = ItemType(
        name_type=item_type_data["name_type"],
        description=item_type_data["description"],
        created_by=item_type_data["created_by"],
    )
    db.session.add(new_item_type)
    db.session.commit()
    return new_item_type

def get_all_item_types():
    return ItemType.query.all()

def get_item_type_by_id(item_type_id):
    return ItemType.query.get(item_type_id)

def update_item_type(item_type_id, item_type_data):
    item_type = ItemType.query.get(item_type_id)
    if item_type:
        item_type.name_type = item_type_data.get("name_type", item_type.name_type)
        item_type.description = item_type_data.get("description", item_type.description)
        db.session.commit()
        return item_type
    return None

def delete_item_type(item_type_id):
    item_type = ItemType.query.get(item_type_id)
    if item_type:
        db.session.delete(item_type)
        db.session.commit()
        return True
    return False