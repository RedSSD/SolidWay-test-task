from django.contrib import admin

from articles.models import Article, ThirdPartyArticle

admin.site.register(Article)
admin.site.register(ThirdPartyArticle)
