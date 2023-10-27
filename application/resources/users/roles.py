from application import db
from application.models.users.roles import Role

def create_role(role_data):
    new_role = Role(
        role=role_data["role"],
        description=role_data["description"],
        is_active=role_data.get("is_active", True),
    )
    db.session.add(new_role)
    db.session.commit()
    return new_role

def get_all_roles():
    return Role.query.all()

def get_role_by_id(role_id):
    return Role.query.get(role_id)

def update_role(role_id, role_data):
    role = Role.query.get(role_id)
    if role:
        role.role = role_data.get("role", role.role)
        role.description = role_data.get("description", role.description)
        role.is_active = role_data.get("is_active", role.is_active)
        db.session.commit()
        return role
    return None


def delete_role(role_id):
    role = Role.query.get(role_id)
    if role:
        db.session.delete(role)
        db.session.commit()
        return True
    return False