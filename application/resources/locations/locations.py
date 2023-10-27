from application import db
from application.models.locations.locations import Location

def create_location(location_data):
    new_location = Location(
        name=location_data["name"],
        longitude=location_data.get("longitude"),
        latitude=location_data.get("latitude"),
        description=location_data.get("description"),
        photo_location=location_data.get("photo_location", "default.jpg"),
        created_by=location_data["created_by"],
    )
    db.session.add(new_location)
    db.session.commit()
    return new_location

def get_all_locations():
    return Location.query.all()

def get_location_by_id(location_id):
    return Location.query.get(location_id)

def update_location(location_id, location_data):
    location = Location.query.get(location_id)
    if location:
        location.name = location_data.get("name", location.name)
        location.longitude = location_data.get("longitude", location.longitude)
        location.latitude = location_data.get("latitude", location.latitude)
        location.description = location_data.get("description", location.description)
        location.photo_location = location_data.get("photo_location", location.photo_location)
        db.session.commit()
        return location
    return None

def delete_location(location_id):
    location = Location.query.get(location_id)
    if location:
        db.session.delete(location)
        db.session.commit()
        return True
    return False