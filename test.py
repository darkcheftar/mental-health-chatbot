import unittest
from main import app

class TestStringMethods(unittest.TestCase):

    def test_landing(self):
        client = app.test_client()
        rv = client.get('/')
        self.assertTrue(b'Landing Page' in rv.data, True)
    def test_login(self):
        client = app.test_client()
        rv = client.get('/login')
        self.assertTrue(b'Login Form' in rv.data, True)
    def test_register(self):
        client = app.test_client()
        rv = client.get('/register')
        self.assertTrue(b'Registration Form' in rv.data, True)


if __name__ == '__main__':
    unittest.main()