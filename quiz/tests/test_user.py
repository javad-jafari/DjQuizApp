from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class AddTest(TestCase):

    def test_create_user(self):
        email = "jojo@gmail.com"
        password = "1009"
        username = "kobol"
        user = get_user_model().objects.create_user(
            email=email,
            password =password,
            username = username
        )

        self.assertEqual(user.email,email)
        self.assertEqual(user.username,username)
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_username(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,email="joj@gmail.com",password="1009")

    def test_create_superuser(self):

        user = get_user_model().objects.create_superuser(
            email="email@exp.com",
            password ="password",
            username = "username"
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)