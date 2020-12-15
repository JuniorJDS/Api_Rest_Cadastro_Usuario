import unittest
from api import create_app
from api.entidades import usuario


class TestHome(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        app = create_app("testing")
        self.app = app.test_client()

    def test_01_get_verify(self):
        """ Teste do servidor Flask"""
        r = self.app.get('http://127.0.0.1:5000/usuario')
        self.assertEqual(r.status_code, 200)

    def test_usuario_obj(self):
        user = usuario.Usuario(nome='junior', data_nascimento='23/01/1987', cpf='12233638727', 
        cep='27325170', rua='rua jose fagundes', bairro='Ns Ap', cidade='Barra Mansa', estado='RJ')
        self.assertEqual(user.estado, 'RJ')


if __name__=='__main__':
    unittest.main()