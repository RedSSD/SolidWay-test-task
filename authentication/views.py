import os

from django.http import FileResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from .models import CustomUser
from .permissions import UserIsProfileOwnerOrReadOnly
from .serializers import UserSerializer


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user.
    """
    parser_classes = (MultiPartParser, )
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, UserIsProfileOwnerOrReadOnly]
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        user = self.request.user
        if user.avatar:
            user.avatar.delete()
        serializer.save()


class AvatarRetrieveAPIView(APIView):

    def get(self, request, filename):
        file_path = f"avatars/{filename}"
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'))
        else:
            return Response(status=404)
