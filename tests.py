import unittest
from unittest import mock
from api import create_app, db
import json
from api.entidades import usuario
from api.services import usuario_service
from api.models import usuario_model
import requests


class TestIntegracao(unittest.TestCase):

    @classmethod
    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
    

    def test_01_hello_world(self):
        # Send a request to the API server and store the response.
        response = requests.get('http://127.0.0.1:5000/usuario')

        # Confirm that the request-response cycle completed successfully.
        assert_true(response.ok)
        #""" Teste do servidor Flask"""
        #r = requests.get('http://127.0.0.1:5000/usuario')
        #print(r.text)
        #self.assertEqual(r.status_code, 200)

    #def test_usuario_obj(self):
        #user = usuario_model.Usuario(nome='name', data_nascimento='23/01/1988', cpf='12345678912', 
        #cep='27325170', rua='rua jose fagundes', bairro='Ns Ap', cidade='Barra Mansa', estado='RJ')
        #self.assertEqual(user.estado, 'RJ')
        #self.assertEqual(user.cep, '27325170')
        #self.assertEqual(user.data_nascimento, '23/01/1988')


if __name__=='__main__':
    unittest.main()