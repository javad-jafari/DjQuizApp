from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from quiz.models import Question, Quizzes, Category

CREATE_USER_URL = reverse('register')
LOGIN_USER_URL = reverse('token_obtain_pair')

def create_user(**params):
    return get_user_model().objects.create(**params)


class UserApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()


    def test_user_valid_creation(self):

        payload = {
            "username":"smaple",
            "password":"sample",
            "confirm_password":"sample"
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code , status.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data)

        self.assertTrue(user.check_password(payload["password"]))


    
    def test_user_bad_req_creation(self):

        payload = {
            "username":"smaple",
            "password":"sample"
        }

        res = self.client.post(CREATE_USER_URL, payload)


        self.assertEqual(res.status_code , status.HTTP_400_BAD_REQUEST)


    def test_short_password(self):
        payload = {
            "username":"smaple",
            "password":"sam",
            "confirm_password":"sam"
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code , status.HTTP_400_BAD_REQUEST)
    

    def test_login_api(self):
        
        payload={
            "username":"smaple",
            "password":"sample"
        }

        user = get_user_model().objects.create_user(**payload)

        res = self.client.post(LOGIN_USER_URL, payload)


        self.assertEqual(res.status_code , status.HTTP_200_OK)
        self.assertIn("access", res.data)


    def test_login_failed_authorize(self):
        
        payload={
            "username":"smaple",
            "password":"sample"
        }

        user = create_user(**payload)

        res = self.client.post(LOGIN_USER_URL, payload)
        self.assertEqual(res.status_code , status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("access",res.data)
    





class PrivateUserApiTest(TestCase):

    def setUp(self) :

        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username = "username",
            password = "password"
        )
        self.client.force_authenticate(user=self.user)

    
    def test_retrive_instance_user(self):
        res = self.client.get(reverse("user-detail", args=[self.user.id]))

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_list_all_users_failed_403_permission(self):
        res = self.client.get(reverse("users"))
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_user_can_create_quiz(self):
        Category.objects.create(name="newcat")

        sample_quiz = {
            "title":"sample quiz create",
            "category":"1"
        }

        res = self.client.post(reverse("create-quizes"), sample_quiz)
        created_quiz = Quizzes.objects.get(id = res.data["id"])

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(created_quiz.creator.username, self.user.username)
        self.assertIn("title",res.data)
        self.assertNotIn("creator", res.data)

