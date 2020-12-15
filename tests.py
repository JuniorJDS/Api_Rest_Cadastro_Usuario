import unittest
from unittest import mock
from api import create_app, db
import json
from api.entidades import usuario
from api.services import usuario_service
from api.models import usuario_model


class TestIntegracao(unittest.TestCase):

    @classmethod
    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_01_hello_world(self):
        """ Teste do servidor Flask"""
        r = self.app.get('http://127.0.0.1:5000/usuario')
        self.assertEqual(r.status_code, 200)

    #def test_usuario_obj(self):
        #user = usuario_model.Usuario(nome='name', data_nascimento='23/01/1988', cpf='12345678912', 
        #cep='27325170', rua='rua jose fagundes', bairro='Ns Ap', cidade='Barra Mansa', estado='RJ')
        #self.assertEqual(user.estado, 'RJ')
        #self.assertEqual(user.cep, '27325170')
        #self.assertEqual(user.data_nascimento, '23/01/1988')


if __name__=='__main__':
    unittest.main()