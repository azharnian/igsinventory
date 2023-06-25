from datetime import datetime

from flask import Blueprint, request
from flask_restful import Resource, marshal_with, marshal

from jsonschema import validate, ValidationError

from application import db, api
from application.models.users import User_Role, user_role_model_json
from application.utils.json_schema import user_role_schema



users = Blueprint('users', __name__)


class UserRolesApi(Resource):

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


class UserRoleApi(Resource):

    @marshal_with(user_role_model_json)
    def get(self, id):
        """Get a role user by id"""
        userrole = User_Role.query.get_or_404(id)
        return userrole, 200
    
    @marshal_with(user_role_model_json)
    def put(self, id):
        """Update a role user by id"""
        pass

    @marshal_with(user_role_model_json)
    def delete(self, id):
        """Delete a role user by id"""
        pass


class SignupApi(Resource):
    def post(self):
        pass


api.add_resource(UserRolesApi, "/userroles", methods=["GET", "POST"])

api.add_resource(UserRoleApi, "/userrole/<int:id>", methods=["GET", "POST"])