import unittest
from unittest import mock
from datetime import datetime
from api import create_app, db
import json
from api.entidades import usuario
from api.services import usuario_service
from api.models import usuario_model
import requests



class TestIntegracao(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client
        self.user = {'nome': 'Junior tr', 
                     'data_nascimento': '2019-01-22', 
                     'cpf': '12312312312', 
                     'cep': '20751060'
                    }

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    

    def test_01_hello_world(self):
        """Test API can create a bucketlist (POST request)"""
        res = self.client().post('/usuario', data=self.user)
        print(res)
        print(self.user)
        #self.assertEqual(res.status_code, 201)
        #self.assertIn('Go to Borabora', str(res.data))


if __name__=='__main__':
    unittest.main()