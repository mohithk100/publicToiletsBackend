from user_accounts.models import User
from .serializers import (
    UserSerializer,
    UserCreationSerializer,
    UserUpdateSerializer,
)
from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticated,
)

class ListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

class RetrieveApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAuthenticated,)


class CreateApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = (AllowAny,)

class UpdateApiView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'username'
    permission_classes = (IsAuthenticated,)

class  DestroyApiView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAdminUser,)
