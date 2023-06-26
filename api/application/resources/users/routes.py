from datetime import datetime
from jsonschema import validate, ValidationError

from flask import Blueprint, request
from flask_restx import Resource, marshal_with, marshal

from application import api
from application.models.users import User_Role, user_role_model_json, User, user_model_json
from application.utils.json_schema import user_role_schema, user_schema

from application.utils.error_json import error_model_json

users = Blueprint('users', __name__)


class UserRolesResource(Resource):

    @marshal_with(user_role_model_json)
    def get(self):
        """Get all role users"""
        userroles = User_Role.query.all()
        return userroles, 200
    
    def post(self):
        """Create a new user role"""
        data = request.get_json()
        
        try:
            validate(data, user_role_schema)
        except ValidationError as e:
            return error_model_json(e), 400

        new_user_role = User_Role(
            role = data.get("role"),
            description = data.get("description"),
            is_active = True,
            date_created = datetime.utcnow()
        )
        new_user_role.save()
        response = marshal(new_user_role, user_role_model_json)
        return response, 201

class UserRoleResource(Resource):

    @marshal_with(user_role_model_json)
    def get(self, id):
        """Get a role user by id"""
        userrole = User_Role.query.get_or_404(id)
        return userrole, 200
    
    def put(self, id):
        """Update a role user by id"""
        userrole_to_update = User_Role.query.get_or_404(id) 
        data = request.get_json()

        try:
            validate(data, user_role_schema)
        except ValidationError as e:
            return {"errors" : e.message}, 400
        
        userrole_to_update.update(
            role = data.get("role"),
            description = data.get("description"))
        
        return {
                "updated" : True,
                "userrole" : marshal(userrole_to_update, user_role_model_json)
            }, 200

    def delete(self, id):
        """Delete a role user by id"""
        userrole_to_delete = User_Role.query.get_or_404(id)
        userrole_to_delete.delete()

        return {
            "deleted" : True,
            "userrole" : marshal(userrole_to_delete, user_role_model_json)
        }, 200


class UsersResource(Resource):

    @marshal_with(user_model_json)
    def get(self):
        """Get all users"""
        users = User.query.all()
        return users
    
    

class SignUpResource(Resource):

    def post(self):
        """Add new user"""
        data = request.get_json()

        try:
            validate(data, user_schema)
        except ValidationError as e:
            return error_model_json(e), 400
        
        new_user = User(
            username = data.get("username"),
            email = data.get("email"),
            phone = data.get("phone"),
            password = data.get("password"),
            first_name = data.get("first_name"),
            last_name = data.get("last_name"),
            role = data.get("role")
        )
        if data.get("profile_picture"):
            new_user.profile_picture = f"/profile_picture/{data.get('profile_picture')}"

        response = {
            "added" : new_user.save(),
        }
        if response["added"]["status"] == "success":
            response["user"] = marshal(new_user, user_model_json)
            return response, 201
        return response, 500


api.add_resource(UserRolesResource, 
                 "/userroles", 
                 methods = ["GET", "POST"])

api.add_resource(UserRoleResource, 
                 "/userrole/<int:id>", 
                 methods = ["GET", "POST", "PUT", "DELETE"])

api.add_resource(UsersResource, 
                 "/users",
                  methods = ["GET"] )

api.add_resource(SignUpResource,
                 "/signup",
                 methods = ["POST"])