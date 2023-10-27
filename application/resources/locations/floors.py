from application import db
from application.models.locations.buildings import Floor

def create_floor(floor_data):
    new_floor = Floor(
        name=floor_data["name"],
        description=floor_data.get("description"),
        building_id=floor_data["building_id"],
        photo_location=floor_data.get("photo_location", "default.jpg"),
        created_by=floor_data["created_by"],
    )
    db.session.add(new_floor)
    db.session.commit()
    return new_floor

def get_all_floors():
    return Floor.query.all()

def get_floor_by_id(floor_id):
    return Floor.query.get(floor_id)

def update_floor(floor_id, floor_data):
    floor = Floor.query.get(floor_id)
    if floor:
        floor.name = floor_data.get("name", floor.name)
        floor.description = floor_data.get("description", floor.description)
        floor.building_id = floor_data.get("building_id", floor.building_id)
        floor.photo_location = floor_data.get("photo_location", floor.photo_location)
        db.session.commit()
        return floor
    return None

def delete_floor(floor_id):
    floor = Floor.query.get(floor_id)
    if floor:
        db.session.delete(floor)
        db.session.commit()
        return True
    return False