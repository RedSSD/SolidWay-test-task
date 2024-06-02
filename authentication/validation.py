import re
from django.core.exceptions import ValidationError


def validate_password(password_value: str):
    password = re.match(
        pattern=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
        string=password_value
    )
    if not password:
        raise ValidationError(
            'Password must contain: eight characters, at least one letter and one number'
        )
