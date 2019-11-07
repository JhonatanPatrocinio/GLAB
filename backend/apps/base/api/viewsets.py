from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import permissions

from .serializers import LaboratorySerializer
from apps.base.models import Laboratory


class LaboratoryViewSet(ReadOnlyModelViewSet):
    serializer_class = LaboratorySerializer
    model = Laboratory
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        return Laboratory.objects.all()


