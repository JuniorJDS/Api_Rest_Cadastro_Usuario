from flask import Flask
from flask_restful import Api
from config import app_config

api = Api()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    api.init_app(app)

    return app

from .views import usuario_views