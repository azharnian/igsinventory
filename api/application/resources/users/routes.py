from datetime import datetime
from jsonschema import validate, ValidationError

from flask import Blueprint, request
from flask_restx import Resource, marshal_with, marshal
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from werkzeug.security import check_password_hash

from application import api

from application.models.users import User_Role, user_role_model_json, User, user_model_json, user_login_model_json

from application.utils.json_schema import user_role_schema, user_schema, user_login_schema

from application.utils.error_json import error_model_json

users = Blueprint('users', __name__)

user_role_model = api.model(
    "User Role",
    user_role_model_json
)

user_model = api.model(
    "User",
    user_model_json
)

login_model = api.model(
    "Login",
    user_login_model_json
)

class UserRolesResource(Resource):

    @marshal_with(user_role_model_json)
    @jwt_required()
    def get(self):
        """Get all role users"""
        userroles = User_Role.query.all()
        return userroles, 200
    
    @api.expect(user_role_model)
    @jwt_required()
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
    @jwt_required()
    def get(self, id):
        """Get a role user by id"""
        userrole = User_Role.query.get_or_404(id)
        return userrole, 200
    
    @api.expect(user_role_model)
    @jwt_required()
    def put(self, id):
        """Update a role user by id"""
        userrole_to_update = User_Role.query.get_or_404(id) 
        data = request.get_json()

        try:
            validate(data, user_role_schema)
        except ValidationError as e:
            return error_model_json(e), 400
        
        userrole_to_update.update(
            role = data.get("role"),
            description = data.get("description"))
        
        return {
                "updated" : True,
                "userrole" : marshal(userrole_to_update, user_role_model_json)
            }, 200

    @api.expect(user_role_model)
    @jwt_required()
    def delete(self, id):
        """Delete a role user by id"""
        userrole_to_delete = User_Role.query.get_or_404(id)
        userrole_to_delete.delete()

        return {
            "deleted" : True,
            "userrole" : marshal(userrole_to_delete, user_role_model_json)
        }, 200


class UsersResource(Resource):

    @marshal_with(user_model)
    @jwt_required()
    def get(self):
        """Get all users"""
        users = User.query.all()
        return users
    
    

class SignUpResource(Resource):

    @api.expect(user_model)
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
            role = 2 #data.get("role")
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


class LoginResource(Resource):

    @api.expect(login_model)
    def post(self):
        data = request.get_json()

        try:
            validate(data, user_login_schema)
        except ValidationError as e:
            return error_model_json(e), 400
        
        user_to_login = User.query.filter_by(
            username = data.get("username")
            ).first()
        
        if user_to_login and check_password_hash(user_to_login.password, data.get("password")):
            access_token = create_access_token(identity = user_to_login.username)
            refresh_token = create_refresh_token(identity = user_to_login.username)
            
            response = {
                "login" : True,
                "access_token" : access_token,
                "refresh_token" : refresh_token
            }

            return response, 200
        return {"login" : False}, 401
    

class RefreshResource(Resource):

    @jwt_required(refresh=True)
    def post(self):

        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity = current_user)

        return {"access_token" : new_access_token} , 200

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

api.add_resource(LoginResource,
                 "/login",
                 methods = ["POST"])

api.add_resource(RefreshResource,
                 "/refresh",
                 methods = ["POST"])