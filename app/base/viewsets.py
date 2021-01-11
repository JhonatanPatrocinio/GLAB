from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Laboratory
from .serializers import LaboratorySerializer


class LaboratoryViewSet(ReadOnlyModelViewSet):
    serializer_class = LaboratorySerializer
    model = Laboratory
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        return Laboratory.objects.all()


