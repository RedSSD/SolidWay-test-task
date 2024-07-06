from django.db import models

from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = HTMLField()
    publication_date = models.DateTimeField(auto_now_add=True, null=False)
    author = models.ForeignKey(to="authentication.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ThirdPartyArticle(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    publication_date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title


class NotificationSubscriber(models.Model):
    telegram_chat_id = models.CharField(max_length=12, blank=False, null=False)

    def __str__(self):
        return self.telegram_chat_id
