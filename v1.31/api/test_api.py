import unittest

from application import create_app, db
from application.config import TestConfig


class APITestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config_class = TestConfig)
        self.client = self.app.test_client(self)

        with self.app.app_context():
            # db.init_app(self.app)
            db.create_all()

    def test_signup(self):
        signup_response = self.client.post("/signup",
                            json = {
                                "username" : "testuser",
                                "email" : "testuser@gmail.com",
                                "phone" : "0812345678",
                                "password" : "password",
                                "first_name" : "test",
                                "last_name" : "user",
                                "role" : 0
                            })
        status_code = signup_response.status_code
        self.assertEqual(status_code, 201)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()