from django.urls import path

from .views import ArticleListAPIView, ArticleDetailAPIView, ArticleCreateAPIView, ArticleLatestAPIView

app_name = 'articles'

urlpatterns = [
    path('articles/', ArticleListAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('articles/latest/', ArticleLatestAPIView.as_view(), name='article-latest'),
    path('articles/create/', ArticleCreateAPIView.as_view(), name='article-create'),
]
