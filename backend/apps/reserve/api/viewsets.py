from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


from .serializers import ReserveSerializer
from apps.reserve.models import Reserve


class ReserveViewSet(ModelViewSet):
    serializer_class = ReserveSerializer
    model = Reserve
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        return Reserve.objects.all()
