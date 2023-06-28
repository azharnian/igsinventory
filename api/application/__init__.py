from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail

from dotenv import load_dotenv
load_dotenv()

from application.config import DevConfig

migrate = Migrate()
db = SQLAlchemy()
api = Api(doc = "/docs",
          title = "Inventory API",
          version = "",
          description = "An inventory api")

jwt = JWTManager()
cors = CORS()
mail = Mail()

def create_app(config_class = DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    from application.views.home import home
    from application.resources.activities.routes import activities
    from application.resources.items.routes import items
    from application.resources.locations.routes import locations
    from application.resources.logs.routes import logs
    from application.resources.users.routes import users
    from application.resources.miscs.routes import miscs

    app.register_blueprint(home)
    app.register_blueprint(activities)
    app.register_blueprint(items)
    app.register_blueprint(locations)
    app.register_blueprint(logs)
    app.register_blueprint(users)
    app.register_blueprint(miscs)

    db.init_app(app)
    api.init_app(app)
    jwt.init_app(app)
    # api.namespaces.pop(0)
    migrate.init_app(app, db)
    cors.init_app(app)
    mail.init_app(app)

    return app