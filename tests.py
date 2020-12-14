import unittest
from api import create_app


class TestHome(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        app = create_app("testing")
        self.app = app.test_client()

    def test_01_get_verify(self):
        """ Teste do servidor Flask"""
        r = self.app.get('http://127.0.0.1:5000/usuario')
        self.assertEqual(r.status_code, 200)

if __name__=='__main__':
    unittest.main()