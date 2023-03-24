from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import LoginManager
from flask_mail import Mail

from application.config import Config

migrate = Migrate()
db = SQLAlchemy()
api = Api()
mail = Mail()
login_manager = LoginManager()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    login_manager.init_app(app)

    from application.apis.activities.routes import activities
    from application.apis.items.routes import items
    from application.apis.locations.routes import locations
    from application.apis.logs.routes import logs
    from application.apis.users.routes import users

    app.register_blueprint(activities)
    app.register_blueprint(items)
    app.register_blueprint(locations)
    app.register_blueprint(logs)
    app.register_blueprint(users)

    return app