from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars')

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [
        'fullname',
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
