from datetime import datetime

from flask import Blueprint, jsonify
from flask_restful import Resource, marshal_with

from application import db, api
from application.models.users import User_Role, user_role_model_json, user_role_list_model_json
from application.forms.users_form import SignUpForm, UserRoleForm

users = Blueprint('users', __name__)

""" resource user test api """
class UserTestApi(Resource):

    def get(self):
        return jsonify({
            "success" : True,
            "massage" : "API works!"
        }, 200)
""" end point user test api """
api.add_resource(UserTestApi, "/user/test", methods=["GET"])



class UserRolesApi(Resource):

    @marshal_with(user_role_list_model_json)
    def get(self):
        """Get all role users"""
        userroles = User_Role.query.all()
        return userroles

api.add_resource(UserRolesApi, "/userroles", methods=["GET"])


class UserRoleApi(Resource):

    @marshal_with(user_role_model_json)
    def get(self, id):
        """Get a role user by id"""
        pass

    @marshal_with(user_role_model_json)
    def put(self, id):
        """Update a role user by id"""
        pass

    @marshal_with(user_role_model_json)
    def delete(self, id):
        """Delete a role user by id"""
        pass

    @marshal_with(user_role_model_json)
    def post(self):
        """Create a new user role"""
        form = UserRoleForm()
        if form.validate_on_submit():
            new_user_role = User_Role(
                role = form.role.data,
                description = form.description.data,
                is_active = True,
                date_created = datetime.utcnow(),
                date_updated = datetime.utcnow()
            )
            print(new_user_role)
            new_user_role.save()
            return new_user_role, 201
        else:
            return jsonify({
                "errors" : form.errors
            })
        return form
api.add_resource(UserRoleApi, "/userrole/add", methods=["POST"])

class SignupApi(Resource):
    def post(self):
        form = SignUpForm()
        pass



