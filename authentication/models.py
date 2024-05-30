from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CoreModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    create_at = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="created"
    )
    update_at = models.DateTimeField(auto_now=True, verbose_name="updated")

    class Meta:
        abstract = True


class CustomUser(AbstractUser, CoreModel):
    full_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True)
    avatar = models.ImageField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
