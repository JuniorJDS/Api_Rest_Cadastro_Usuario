import unittest
from datetime import datetime
from unittest import mock
from api import create_app, db
import json
from api.entidades import usuario
from api.services import usuario_service
from api.models import usuario_model



class TestHome(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    #def test_01_hello_world(self):
        #""" Teste do servidor Flask"""
        #r = requests.get('http://127.0.0.1:5000/usuario')
        #print(r.text)
        #self.assertEqual(r.status_code, 200)
        
    def test_usuario_obj(self):
        user = usuario.Usuario(nome='name', data_nascimento='1988-01-01', cpf='12345678912', 
        cep='27325170', rua='rua jose fagundes', bairro='Ns Ap', cidade='Barra Mansa', estado='RJ')
        self.assertEqual(user.estado, 'RJ')
        self.assertEqual(user.cep, '27325170')
        self.assertEqual(user.data_nascimento, '1988-01-01')

    def test_cadastrar_cliente(self):
        user = usuario_model.Usuario(nome='name', data_nascimento=datetime(2012, 3, 3), cpf='123456712', 
        cep='27325170', rua='rua jose fagundes', bairro='Ns Ap', cidade='Barra Mansa', estado='RJ')
        db.session.add(user)
        db.session.commit()

        usuario_cadastrado = usuario_model.Usuario.query.filter_by(id=1).first()
        self.assertEqual(user.nome, usuario_cadastrado.nome)
        self.assertEqual(user.cpf, usuario_cadastrado.cpf)
        self.assertEqual(user.estado, usuario_cadastrado.estado)

    def test_listar_cliente(self):
        pass


if __name__=='__main__':
    unittest.main()