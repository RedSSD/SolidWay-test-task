import factory.django

from authentication.factories import UserFactory
from .models import Article, ThirdPartyArticle


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
        django_get_or_create = ("title",)

    title = factory.Sequence(lambda n: f"Test article {n + 1}")
    author = factory.SubFactory(UserFactory)
    content = factory.Sequence(lambda n: f"Test content {n + 1}")
