from django.urls import path
from .views import (
    JWTTokenObtainPairView,
    JWTTokenRefreshView,
    JWTTokenBlacklistView
)

urlpatterns = [
    path('token/login/', JWTTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', JWTTokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', JWTTokenBlacklistView.as_view(), name='token_blacklist'),
]
