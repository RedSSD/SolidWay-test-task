from rest_framework import status
from rest_framework.test import APITestCase

from authentication.factories import UserFactory
from articles.factories import ArticleFactory


class TestArticleAPITest(APITestCase):
    def setUp(self) -> None:
        self.test_person_just_user = UserFactory(email="test1@test.com")
        self.test_person_not_article_owner = UserFactory(email="test2@test.com")
        self.test_article = ArticleFactory(
            id=2,
            title="Article 1",
            content="Article 1 content",
            author=self.test_person_just_user
        )

    def test_get_all_articles_unauthorized(self):
        response = self.client.get("/api/v1/articles/")
        self.assertEqual(200, response.status_code)

    def test_get_article_unauthorized(self):
        response = self.client.get("/api/v1/articles/2/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_article_authorized(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.get("/api/v1/articles/2/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.test_article.title)

    def test_post_article_unauthorized(self):
        response = self.client.post("/api/v1/articles/create/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            {
                "detail": "Authentication credentials were not provided."
            },
            response.json()
        )

    def test_post_article_no_data_authorized(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.post("/api/v1/articles/create/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {
                "title": [
                    "This field is required."
                ],
                "content": [
                    "This field is required."
                ]
            },
            response.json()
        )

    def test_post_article_authorized(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.post(
            path="/api/v1/articles/create/",
            data={
                "title": "Test",
                "content": "Test12345",
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_article_unauthorized(self):
        response = self.client.post("/api/v1/articles/2/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            {
                "detail": "Authentication credentials were not provided."
            },
            response.json()
        )

    def test_patch_article_not_owner_authorized(self):
        self.client.force_authenticate(self.test_person_not_article_owner)
        response = self.client.patch("/api/v1/articles/2/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_article_no_data_owner_authorized(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.patch("/api/v1/articles/2/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_article_owner_authorized(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.patch(
            path="/api/v1/articles/2/",
            data={
                "title": "New test title"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("New test title", response.data["title"])

    def test_delete_article_unauthorized(self):
        response = self.client.delete("/api/v1/articles/2/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_article_not_owner_authorized(self):
        self.client.force_authenticate(self.test_person_not_article_owner)
        response = self.client.delete("/api/v1/articles/2/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_article_owner_authorized(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.delete("/api/v1/articles/2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
