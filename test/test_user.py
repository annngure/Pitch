import unittest
from .models import User,Post,Comment,Upvote,Downvote
from app import db

class UserModelTest(unittest.TestCase):
    def setUp(self)
    self.new_user = User(password = "fun")

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_secure is not None)

    def text_no_acess_password(self):
        with self.assertRaise(AttributeError):
            self.new_user.password


    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('fun'))
        