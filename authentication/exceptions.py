from django.core.exceptions import ValidationError


class UserNotFoundError(ValidationError):
    def __init__(self, message="User not found", *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class WrongPasswordError(ValidationError):
    def __init__(self, message="Wrong password", *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class UserNotActivatedError(ValidationError):
    def __init__(self, message="User is not activated", *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class UserNotActivatedError(ValidationError):
    def __init__(self, message="User is not activated", *args, **kwargs):
        super().__init__(message, *args, **kwargs)
