from rest_framework import serializers

from articles.models import Article


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