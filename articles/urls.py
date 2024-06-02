from django.urls import path

from .views import ArticleListAPIView, ArticleDetailAPIView, ArticleCreateAPIView

app_name = 'articles'

urlpatterns = [
    path('articles/', ArticleListAPIView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article_detail'),
    path('articles/create/', ArticleCreateAPIView.as_view(), name='article_create'),
]
