import requests

from flask import Blueprint
from flask_restx import Resource

from application import api

miscs = Blueprint('miscs', __name__)

class HelloWorldResource(Resource):

    def get(self):
        """Get hello world message"""
        return {"message" : "Hello, world!"}, 200
    
class PingGoogleResource(Resource):

    def get(self):
        """Get Ping Internet Connection with Google Request"""
        try:
            response = requests.get("https://www.google.com/", timeout=5)
            if response.status_code == 200:
                return {"status" : "success", "message" : "Ping Success"}, 200
            else:
                return {"status" : "failed", "message" : "Ping Failed"}, 500
        except requests.exceptions.RequestException as e:
            return {"status" : "error", "message" : str(e)}, 500
    
api.add_resource(HelloWorldResource,
                 "/hello", methods = ["GET"])

api.add_resource(PingGoogleResource,
                 "/ping/google")