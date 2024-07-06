from rest_framework import serializers

from core.settings import BASE_API_URL
from articles.models import Article, ThirdPartyArticle


class ArticleListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ("pk", "title", "author", "publication_date")

    def get_author(self, obj):
        return obj.author.fullname


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"

    def get_author(self, obj):
        return obj.author.fullname


class ArticleLatestSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    article_url = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ("title", "author", "article_url")

    def get_author(self, obj):
        return obj.author.fullname

    def get_article_url(self, obj):
        return BASE_API_URL + f"articles/{obj.pk}/"


class ThirdPartyArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdPartyArticle
        fields = "__all__"
