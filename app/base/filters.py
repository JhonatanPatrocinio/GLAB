import django_filters
from base.models import Place


class PlaceFilter(django_filters.FilterSet):
    type = django_filters.NumberFilter(field_name='type', lookup_expr='id')

    class Meta:
        model = Place
