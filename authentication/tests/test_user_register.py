from rest_framework import status
from rest_framework.test import APITestCase

from authentication.factories import UserFactory


class UserRegistrationAPITests(APITestCase):
    def setUp(self):
        self.user = UserFactory(email="test@test.com")

    def test_register_user_successful(self):
        response = self.client.post(
            path="/api/v1/auth/users/",
            data={
                "email": "jane@test.com",
                "password": "Test_app1234",
                "fullname": "Jane",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_email_incorrect(self):
        response = self.client.post(
            path="/api/v1/auth/users/",
            data={
                "email": "jane@testcom",
                "password": "Test1234",
                "fullname": "Jane",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {"email": ["Enter a valid email address."]},
            response.json(),
        )

    def test_register_user_email_exists(self):
        response = self.client.post(
            path="/api/v1/auth/users/",
            data={
                "email": "test@test.com",
                "password": "Test1234",
                "re_password": "Test1234",
                "fullname": "Test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {"email": ['custom user with this email already exists.']},
            response.json(),
        )

    def test_register_user_password_incorrect(self):
        response = self.client.post(
            path="/api/v1/auth/users/",
            data={
                "email": "jane@test.com",
                "password": "test",
                "fullname": "Jane"
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {
                "password":
                    ['The password is too similar to the email.',
                    'This password is too short. It must contain at least 8 '
                    'characters.',
                    'This password is too common.'
                ]
            },
            response.json(),
        )
