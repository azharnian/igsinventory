from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import LoginManager
from flask_mail import Mail

from dotenv import load_dotenv
load_dotenv()

from application.config import DevConfig

migrate = Migrate()
db = SQLAlchemy()
api = Api()
mail = Mail()
login_manager = LoginManager()

def create_app(config_class = DevConfig):
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    
    from application.views.docs import docs
    from application.resources.activities.routes import activities
    from application.resources.items.routes import items
    from application.resources.locations.routes import locations
    from application.resources.logs.routes import logs
    from application.resources.users.routes import users

    app.register_blueprint(docs)
    app.register_blueprint(activities)
    app.register_blueprint(items)
    app.register_blueprint(locations)
    app.register_blueprint(logs)
    app.register_blueprint(users)

    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    login_manager.init_app(app)

    return app