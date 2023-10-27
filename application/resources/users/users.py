from application import db
from application.models.users.users import User

def create_user(user_data):
    new_user = User(
        username=user_data["username"],
        email=user_data["email"],
        phone=user_data["phone"],
        password=user_data["password"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        full_name=f"{user_data['first_name']} {user_data['last_name']}",
        role=user_data["role"],
        is_active=user_data.get("is_active", True),
        profile_picture=user_data.get("profile_picture", "/profile_picture/default.jpg"),
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def update_user(user_id, user_data):
    user = User.query.get(user_id)
    if user:
        user.username = user_data.get("username", user.username)
        user.email = user_data.get("email", user.email)
        user.phone = user_data.get("phone", user.phone)
        user.password = user_data.get("password", user.password)
        user.first_name = user_data.get("first_name", user.first_name)
        user.last_name = user_data.get("last_name", user.last_name)
        user.full_name = f"{user_data.get('first_name', user.first_name)} {user_data.get('last_name', user.last_name)}"
        user.role = user_data.get("role", user.role)
        user.is_active = user_data.get("is_active", user.is_active)
        user.profile_picture = user_data.get("profile_picture", user.profile_picture)
        db.session.commit()
        return user
    return None

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False