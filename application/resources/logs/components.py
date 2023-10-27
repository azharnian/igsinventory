from application import db
from application.models.logs.components import Component

def create_component(component_data):
    new_component = Component(
        component_name=component_data["component_name"],
        created_by=component_data.get("created_by", 0),
        note=component_data.get("note"),
    )
    db.session.add(new_component)
    db.session.commit()
    return new_component

def get_all_components():
    return Component.query.all()

def get_component_by_id(component_id):
    return Component.query.get(component_id)

def update_component(component_id, component_data):
    component = Component.query.get(component_id)
    if component:
        component.component_name = component_data.get("component_name", component.component_name)
        component.created_by = component_data.get("created_by", component.created_by)
        component.note = component_data.get("note", component.note)
        db.session.commit()
        return component
    return None

def delete_component(component_id):
    component = Component.query.get(component_id)
    if component:
        db.session.delete(component)
        db.session.commit()
        return True
    return False