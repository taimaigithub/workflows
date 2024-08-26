import unittest
import json
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_add_user(self):
        response = self.app.post('/add_user', json={"name": "Test User", "email": "test@example.com"})
        self.assertEqual(response.status_code, 201)
        self.assertIn('User added successfully!', str(response.data))

if __name__ == "__main__":
    unittest.main()
