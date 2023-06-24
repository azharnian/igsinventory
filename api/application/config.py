import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = config("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIR,config("DB_URI_DEV"))
    DEBUG = True
    SQLALCHEMY_ECHO = True 

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass