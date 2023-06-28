from flask import Blueprint
from flask_restx import Resource

from application import api

miscs = Blueprint('miscs', __name__)

class HelloWorldResource(Resource):

    def get(self):
        """Get hello world message"""
        return {"message" : "Hello, world!"}, 200
    
api.add_resource(HelloWorldResource,
                 "/hello", methods = ["GET"])