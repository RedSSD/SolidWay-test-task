from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from .models import CustomUser
from .permissions import UserIsProfileOwnerOrReadOnly
from .serializers import UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user.
    """
    parser_classes = (MultiPartParser, )
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, UserIsProfileOwnerOrReadOnly]
    serializer_class = UserSerializer


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
