from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

from application.config import Config, DevConfig

db = SQLAlchemy()
redis = FlaskRedis()
migrate = Migrate()
mail = Mail()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'



def create_app(config_class=Config):
    app = Flask(__name__, template_folder='views')
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    redis.init_app(app)
    migrate.init_app(app, db)

    from application.routes.users.roles import roles
    from application.routes.users.users import users
    from application.routes.locations.locations import locations
    from application.routes.locations.buildings import buildings
    from application.routes.locations.floors import floors
    from application.routes.locations.rooms import rooms
    from application.routes.items.item_types import item_types
    from application.routes.items.items import items
    from application.routes.activities.transfers import transfers
    from application.routes.activities.updates import updates
    from application.routes.logs.components import components
    from application.routes.logs.events import events
    from application.routes.logs.logs import logs

    app.register_blueprint(roles)
    app.register_blueprint(users)
    app.register_blueprint(locations)
    app.register_blueprint(buildings)
    app.register_blueprint(floors)
    app.register_blueprint(rooms)
    app.register_blueprint(item_types)
    app.register_blueprint(items)
    app.register_blueprint(transfers)
    app.register_blueprint(updates)
    app.register_blueprint(components)
    app.register_blueprint(events)
    app.register_blueprint(logs)

    return app