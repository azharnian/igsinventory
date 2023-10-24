import os
from decouple import config as cf
from dotenv import load_dotenv

load_dotenv()

class Config:
    #pycache
    PYTHONDONTWRITEBYTECODE = cf('PYTHONDONTWRITEBYTECODE', default=False, cast=bool)

    #secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')

    #sql
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_DEV')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

    #redis
    REDIS_URL = os.environ.get('REDIS_URL')

    #mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_ADDRESS')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    #recaptcha
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')

class DevConfig(Config):
    #secret key
    SECRET_KEY = os.environ.get('SECRET_KEY_DEV')

    #sql
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_DEV')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #redis
    REDIS_URL = os.environ.get('REDIS_URL_DEV')