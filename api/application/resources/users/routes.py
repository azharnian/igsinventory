from datetime import datetime
from jsonschema import validate, ValidationError

from flask import Blueprint, request
from flask_restx import Resource, Namespace, marshal_with, marshal

from application import api
from application.models.users import User_Role, user_role_model_json
from application.utils.json_schema import user_role_schema

users = Blueprint('users', __name__)


user_roles_namespace = Namespace(
    "User Roles",
    description = ""
)
api.add_namespace(user_roles_namespace)
@user_roles_namespace.route("/userroles")
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
            return {"errors" : e.message}, 400

        new_user_role = User_Role(
            role = data.get("role"),
            description = data.get("description"),
            is_active = True,
            date_created = datetime.utcnow()
        )
        new_user_role.save()
        response = marshal(new_user_role, user_role_model_json)
        return response, 201

user_role_namespace = Namespace(
    "User Role",
    description = ""
)
api.add_namespace(user_role_namespace)
@user_role_namespace.route("/userrole/<int:id>")
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


class SignupResource(Resource):
    def post(self):
        pass


api.add_resource(UserRolesResource, "/userroles", methods=["GET", "POST"])
# docs.register(UserRolesResource)

api.add_resource(UserRoleResource, "/userrole/<int:id>", methods=["GET", "POST", "PUT", "DELETE"])