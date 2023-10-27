from application import db
from application.models.locations.buildings import Building

def create_building(building_data):
    new_building = Building(
        name=building_data["name"],
        address=building_data["address"],
        location_id=building_data["location_id"],
        rt=building_data.get("rt", "00"),
        rw=building_data.get("rw", "00"),
        kelurahan=building_data["kelurahan"],
        kecamatan=building_data["kecamatan"],
        city=building_data["city"],
        province=building_data["province"],
        zip_code=building_data.get("zip_code"),
        photo_location=building_data.get("photo_location", "default.jpg"),
        description=building_data.get("description"),
        created_by=building_data["created_by"],
    )
    db.session.add(new_building)
    db.session.commit()
    return new_building

def get_all_buildings():
    return Building.query.all()

def get_building_by_id(building_id):
    return Building.query.get(building_id)

def update_building(building_id, building_data):
    building = Building.query.get(building_id)
    if building:
        building.name = building_data.get("name", building.name)
        building.address = building_data.get("address", building.address)
        building.location_id = building_data.get("location_id", building.location_id)
        building.rt = building_data.get("rt", building.rt)
        building.rw = building_data.get("rw", building.rw)
        building.kelurahan = building_data.get("kelurahan", building.kelurahan)
        building.kecamatan = building_data.get("kecamatan", building.kecamatan)
        building.city = building_data.get("city", building.city)
        building.province = building_data.get("province", building.province)
        building.zip_code = building_data.get("zip_code", building.zip_code)
        building.photo_location = building_data.get("photo_location", building.photo_location)
        building.description = building_data.get("description", building.description)
        db.session.commit()
        return building
    return None

def delete_building(building_id):
    building = Building.query.get(building_id)
    if building:
        db.session.delete(building)
        db.session.commit()
        return True
    return False