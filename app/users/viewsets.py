from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    model = User
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.filter(is_active=True)
        else:
            return User.objects.filter(id=self.request.user.pk).all()
