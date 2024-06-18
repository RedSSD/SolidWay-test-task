from rest_framework import status
from rest_framework.test import APITestCase
from time import sleep

from authentication.factories import UserFactory


class UserLoginAPITests(APITestCase):
    def setUp(self):
        self.user = UserFactory(email="test@test.com")

    def test_login_successful(self):
        self.user.set_password("Test1234")
        self.user.save()
        sleep(6)
        response = self.client.post(
            path="/api/v1/auth/token/login/",
            data={
                "email": "test@test.com",
                "password": "Test1234",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "auth_token")

    def test_login_email_incorrect(self):
        self.user.set_password("Test1234")
        self.user.save()

        response = self.client.post(
            path="/api/v1/auth/token/login/",
            data={
                "email": "tost@test.com",
                "password": "Test1234",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {
                "non_field_errors": [
                    "Unable to log in with provided credentials."
                ]
            },
            response.json(),
        )

    def test_login_password_incorrect(self):
        self.user.set_password("Test1234")
        self.user.save()

        response = self.client.post(
            path="/api/v1/auth/token/login/",
            data={
                "email": "test@test.com",
                "password": "Test5678",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {
                "non_field_errors": [
                    "Unable to log in with provided credentials."
                ]
            },
            response.json(),
        )
