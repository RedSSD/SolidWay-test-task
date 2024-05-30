from typing import List, Optional
from annoying.functions import get_object_or_None
from .models import CustomUser


class UserService:
    """Service layer to work with user domain logic"""

    def get_all_users(self) -> List[CustomUser]:
        """Get all users"""
        return CustomUser.objects.all()

    def get_user_by_email(self, email: str) -> Optional[CustomUser]:
        """Get user by email"""
        return get_object_or_None(CustomUser, email=email)

    def create_user(self, user_dto: CustomUserDTO) -> CreatedCustomUserDTO:
        """Create new user"""
        if self.repository.get_user_by_email(user_dto.email):
            raise UserAlreadyExistsError()

        self._validate_password(user_dto.password)
        self._validate_email(user_dto.email)
        return self.repository.create(user_dto)
