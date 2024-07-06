from django.urls import path, include, re_path

from .views import UserDetailAPIView

app_name = 'authentication'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    path('me/', UserDetailAPIView.as_view(), name='user_detail_view'),
]
