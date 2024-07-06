from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveAPIView
)
from rest_framework.permissions import IsAuthenticated

from .models import Article, ThirdPartyArticle
from .serializer import (
    ArticleListSerializer,
    ArticleDetailSerializer,
    ArticleLatestSerializer,
    ThirdPartyArticleListSerializer
)
from .permissions import UserIsArticleAuthorOrReadOnly

from bot.api_interactor import bot_notify_subscribers


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class ArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = (IsAuthenticated, UserIsArticleAuthorOrReadOnly)


class ArticleLatestAPIView(RetrieveAPIView):
    serializer_class = ArticleLatestSerializer

    def get_object(self):
        return Article.objects.latest("publication_date")


class ArticleCreateAPIView(CreateAPIView):
    serializer_class = ArticleDetailSerializer
    permission_classes = (IsAuthenticated, )

    def current_user(self):
        return (
            self.request.user if self.request.user.is_authenticated else None
        )

    def perform_create(self, serializer):
        serializer.save(author=self.current_user())
        bot_notify_subscribers(serializer.data)


class ThirdPartyArticleListAPIView(ListAPIView):
    queryset = ThirdPartyArticle.objects.all()
    serializer_class = ThirdPartyArticleListSerializer
