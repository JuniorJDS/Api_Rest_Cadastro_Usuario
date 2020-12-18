from flask import Flask
from flask_restful import Api
from config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flasgger import Swagger

api = Api()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
swagger = Swagger()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    api.init_app(app)
    swagger.init_app(app)

    return app

from .views import usuario_views
from .models import usuario_model