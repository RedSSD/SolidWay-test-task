from annoying.functions import get_object_or_None
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import CustomUser
from authentication.exceptions import (
    UserNotFoundError,
    WrongPasswordError,
    UserNotActivatedError
)


class JWTTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        user = get_object_or_None(CustomUser, email=attrs[self.username_field])
        if not user:
            raise UserNotFoundError
        if not check_password(attrs["password"], user.password):
            raise WrongPasswordError
        if not user.is_active:
            raise UserNotActivatedError
        self.user = authenticate(
            **{
                self.username_field: attrs[self.username_field],
                "password": attrs["password"],
            }
        )
        if not self.user:
            raise serializers.ValidationError(
                "Not found account with the given credentials",
                code="authentication",
            )

        refresh = self.get_token(self.user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return data

    @classmethod
    def get_token(cls, user):
        token = RefreshToken.for_user(user)
        return token


class JWTTokenBlacklistSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        "invalid_token": "Token is expired or invalid.",
    }

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("invalid_token")
