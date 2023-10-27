from application import db
from application.models.logs.events import Event

def create_event(event_data):
    new_event = Event(
        event_name=event_data["event_name"],
        created_by=event_data.get("created_by", 0),
        note=event_data.get("note"),
    )
    db.session.add(new_event)
    db.session.commit()
    return new_event

def get_all_events():
    return Event.query.all()

def get_event_by_id(event_id):
    return Event.query.get(event_id)


def update_event(event_id, event_data):
    event = Event.query.get(event_id)
    if event:
        event.event_name = event_data.get("event_name", event.event_name)
        event.created_by = event_data.get("created_by", event.created_by)
        event.note = event_data.get("note", event.note)
        db.session.commit()
        return event
    return None

def delete_event(event_id):
    event = Event.query.get(event_id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return True
    return False