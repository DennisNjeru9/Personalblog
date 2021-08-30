import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User(password = 'perfectblog')
        self.new_user_2 = User(password = 'perfectblog')


    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('perfectblog'))

    def test_password_salts_are_random(self):
        self.assertTrue(self.new_user.pass_secure != self.new_user_2.pass_secure)