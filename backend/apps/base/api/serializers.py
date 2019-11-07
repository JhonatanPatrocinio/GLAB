from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from apps.base.models import Laboratory


class LaboratorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    n_computers = serializers.ReadOnlyField()

    class Meta:
        model = Laboratory
        fields = (
            'id',
            'name',
            'n_computers'
        )


