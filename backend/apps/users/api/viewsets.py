from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import permissions


from .serializers import UserAppSerializer, UserSerializer
from apps.users.models import UserApp


class UserAppViewSet(ModelViewSet):
    serializer_class = UserAppSerializer
    model = UserApp
    permission_classes = [
        permissions.AllowAny,
    ]

    def get_queryset(self):
        return UserApp.objects.filter(user__is_active=True)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    model = User
    permission_classes = [
        permissions.AllowAny,
    ]

    def get_queryset(self):
        return User.objects.filter(is_active=True)
