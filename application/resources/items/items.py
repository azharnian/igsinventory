import secrets
from datetime import datetime

from application import db
from application.models.items.items import Item
from application.utils import save_picture

def create_item(item_data):
    random_code = f"{datetime.now().year}{datetime.now().month}{datetime.now().day}{secrets.token_urlsafe(8)}"
    image_file = "default.jpg"
    if item_data.get("photo_item"):
            picture_file = save_picture(item_data.get("photo_item"), prefix="items")
            image_file = picture_file
    new_item = Item(
        code=random_code,
        name=item_data["name"],
        length=item_data.get("length", 0),
        width=item_data.get("width", 0),
        height=item_data.get("height", 0),
        weight=item_data.get("weight", 0),
        color=item_data.get("color"),
        photo_item=image_file,
        is_electronic=item_data.get("is_electronic", False),
        is_waterresistant=item_data.get("is_waterresistant", False),
        price=item_data.get("price", 0),
        make=item_data.get("make"),
        model=item_data.get("model"),
        store=item_data.get("store"),
        volume_cc=item_data.get("volume_cc", 0),
        material=item_data.get("material"),
        machine_number=item_data.get("machine_number"),
        police_state_number=item_data.get("police_state_number"),
        serial_number=item_data.get("serial_number"),
        date_purchased=item_data.get("date_purchased", datetime.utcnow()),
        budget_type=item_data.get("budget_type", "Dana Masyarakat"),
        origin_country=item_data.get("origin_country", "Indonesia"),
        percent_depreciation_per_year=item_data.get("percent_depreciation_per_year", 0),
        percent_demage=item_data.get("percent_demage", 0),
        is_available=item_data.get("is_available", True),
        is_broken=item_data.get("is_broken", False),
        is_active=item_data.get("is_active", True),
        photo_location=item_data.get("photo_location", "default.jpg"),
        room_id=item_data["room_id"],
        created_by=item_data["created_by"],
        item_type_id=item_data["item_type_id"],
        description=item_data.get("description"),
    )
    db.session.add(new_item)
    db.session.commit()
    return new_item

def get_all_items():
    return Item.query.all()

def get_item_by_id(item_id):
    return Item.query.get(item_id)

def get_items_by_room(room_id):
    return Item.query.filter_by(room_id=room_id).all()

def get_item_by_code(item_code):
    return Item.query.filter_by(code=item_code).first()


def update_item(item_id, item_data):
    item = Item.query.get(item_id)
    image_file = item.photo_item
    if item_data.get("photo_item") != image_file:
        picture_file = save_picture(item_data.get("photo_item"), prefix="items")
        image_file = picture_file
    if item:
        item.code = item_data.get("code", item.code)
        item.name = item_data.get("name", item.name)
        item.length = item_data.get("length", item.length)
        item.width = item_data.get("width", item.width)
        item.height = item_data.get("height", item.height)
        item.weight = item_data.get("weight", item.weight)
        item.color = item_data.get("color", item.color)
        item.photo_item = image_file
        item.is_electronic = item_data.get("is_electronic", item.is_electronic)
        item.is_waterresistant = item_data.get("is_waterresistant", item.is_waterresistant)
        item.price = item_data.get("price", item.price)
        item.make = item_data.get("make", item.make)
        item.model = item_data.get("model", item.model)
        item.store = item_data.get("store", item.store)
        item.volume_cc = item_data.get("volume_cc", item.volume_cc)
        item.material = item_data.get("material", item.material)
        item.machine_number = item_data.get("machine_number", item.machine_number)
        item.police_state_number = item_data.get("police_state_number", item.police_state_number)
        item.serial_number = item_data.get("serial_number", item.serial_number)
        item.date_purchased = item_data.get("date_purchased", item.date_purchased)
        item.budget_type = item_data.get("budget_type", item.budget_type)
        item.origin_country = item_data.get("origin_country", item.origin_country)
        item.percent_depreciation_per_year = item_data.get("percent_depreciation_per_year", item.percent_depreciation_per_year)
        item.percent_demage = item_data.get("percent_demage", item.percent_demage)
        item.is_available = item_data.get("is_available", item.is_available)
        item.is_broken = item_data.get("is_broken", item.is_broken)
        item.is_active = item_data.get("is_active", item.is_active)
        item.photo_location = item_data.get("photo_location", item.photo_location)
        item.room_id = item_data.get("room_id", item.room_id)
        item.created_by = item_data.get("created_by", item.created_by)
        item.item_type_id = item_data.get("item_type_id", item.item_type_id)
        item.description = item_data.get("description", item.description)
        
        db.session.commit()
        return item
    return None



def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return True
    return False