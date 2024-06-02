from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializer import ArticleListSerializer, ArticleDetailSerializer
from .permissions import UserIsArticleAuthorOrReadOnly


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class ArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = (IsAuthenticated, UserIsArticleAuthorOrReadOnly)


class ArticleCreateAPIView(CreateAPIView):
    serializer_class = ArticleDetailSerializer
    permission_classes = (IsAuthenticated, )

    def current_user(self):
        return (
            self.request.user if self.request.user.is_authenticated else None
        )

    def perform_create(self, serializer):
        serializer.save(author=self.current_user())
