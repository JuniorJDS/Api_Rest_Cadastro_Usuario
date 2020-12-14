from flask_restful import Resource
from api import api

class Usuario(Resource):
    def get(self):
        return 'Primeiro Commit'


api.add_resource(Usuario, '/usuario')