from collections import defaultdict

from django.core.exceptions import ValidationError
from djoser.serializers import UserCreatePasswordRetypeSerializer

from rest_framework import serializers

from .models import CustomUser
from .validation import validate_password


class UserRegistrationSerializer(UserCreatePasswordRetypeSerializer):
    email = serializers.EmailField(
        write_only=True,
    )
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        model = CustomUser
        fields = ("email", "password", "fullname")

    def validate(self, attrs):
        custom_errors = defaultdict(list)
        email = attrs.get('email').lower()
        password = attrs.get('password')
        re_password = attrs.pop('re_password')

        if CustomUser.objects.filter(email=email).exists():
            custom_errors['email'].append('Email already registered')
        else:
            attrs['email'] = email

        if re_password != password:
            custom_errors['password'].append('Passwords do not match')

        try:
            validate_password(password)
        except ValidationError as error:
            custom_errors['password'].append(error.message)

        print(attrs)

        if custom_errors:
            print(custom_errors)
            raise ValidationError(custom_errors)
        else:
            return attrs


class UserSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()

    class Meta:
        model = CustomUser
        fields = ('email', 'fullname', 'avatar')
        read_only_fields = ('email',)
