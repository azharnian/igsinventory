from application import db
from application.models.locations.rooms import Room

def create_room(room_data):
    new_room = Room(
        note=room_data.get("note"),
        active=room_data.get("active", True),
        created_by=room_data.get("created_by", 0),
        room_code=room_data["room_code"],
        room_name=room_data["room_name"],
        floor_id=room_data.get("floor_id", 0),
    )
    db.session.add(new_room)
    db.session.commit()
    return new_room

def get_all_rooms():
    return Room.query.all()

def get_room_by_id(room_id):
    return Room.query.get(room_id)

def update_room(room_id, room_data):
    room = Room.query.get(room_id)
    if room:
        room.note = room_data.get("note", room.note)
        room.active = room_data.get("active", room.active)
        room.created_by = room_data.get("created_by", room.created_by)
        room.room_code = room_data.get("room_code", room.room_code)
        room.room_name = room_data.get("room_name", room.room_name)
        room.floor_id = room_data.get("floor_id", room.floor_id)
        db.session.commit()
        return room
    return None


def delete_room(room_id):
    room = Room.query.get(room_id)
    if room:
        db.session.delete(room)
        db.session.commit()
        return True
    return False