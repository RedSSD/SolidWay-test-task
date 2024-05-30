from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, GenericAPIView
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from .serializers import (
    JWTTokenObtainPairSerializer,
    JWTTokenBlacklistSerializer
)

from authentication.exceptions import (
    UserNotFoundError,
    WrongPasswordError,
    UserNotActivatedError
)


class AuthenticationBaseView:
    def _create_response_for_exception(self, exception):
        return Response(
            {"status": "failed", "message": str(exception)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def _create_response_not_valid_token(self, exception):
        return Response(
            {"status": "failed", "message": exception.detail["detail"]},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def _create_response_not_valid_user_credentials_and_serializers(self, exceptions):
        return Response(
            {"status": "failed", "message": exceptions.detail["non_field_errors"][0]},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @staticmethod
    def _create_response_for_successful_request(data=None):
        return Response(
            {
                "data": data
            },
            status=status.HTTP_200_OK,
        )


class JWTTokenObtainPairView(TokenObtainPairView, AuthenticationBaseView):
    serializer_class = JWTTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as exception:
            return self._create_response_not_valid_user_credentials_and_serializers(
                exception
            )
        except (
                UserNotActivatedError,
                UserNotFoundError,
                WrongPasswordError,
        ) as exception:
            return self._create_response_for_exception(exception)
        return self._create_response_for_successful_request(data=serializer.validated_data)


class JWTTokenRefreshView(TokenRefreshView, AuthenticationBaseView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)

        except serializers.ValidationError as exception:
            return self._create_response_not_valid_user_credentials_and_serializers(
                exception
            )

        except TokenError as exception:
            return self._create_response_not_valid_token(
                InvalidToken(exception.args[0])
            )

        return self._create_response_for_successful_request(
            serializer.validated_data
        )


class JWTTokenBlacklistView(GenericAPIView, AuthenticationBaseView):
    serializer_class = JWTTokenBlacklistSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as exception:
            return self._create_response_not_valid_token(
                InvalidToken(exception.args[0])
            )
        serializer.save()
        return self._create_response_for_successful_logout()

    @staticmethod
    def _create_response_for_successful_logout():
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class CustomUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # serializer_class =

    def retrieve(self, request, *args, **kwargs):
        pass

    def perform_update(self, request, *args, **kwargs):
        pass

    def perform_destroy(self, request, *args, **kwargs):
        pass


class CustomUserCreateAPIView(CreateAPIView):
    # serializer_class =

    def perform_create(self, request, *args, **kwargs):
        pass
