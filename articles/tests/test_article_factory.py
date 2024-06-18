from django.test import TestCase

from articles.factories import ArticleFactory


class TestFactories(TestCase):
    def test_user_factory(self):
        article = ArticleFactory()
        self.assertIsNotNone(article.title)
        self.assertIsNotNone(article.author)
        self.assertTrue(article.content)
