from django_filters import rest_framework as dj_filters
from .models import List


class ListFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели статей."""

    title = dj_filters.CharFilter(field_name="name", lookup_expr="icontains")
    is_active = dj_filters.CharFilter(field_name="is_done", exclude=True)

    order_by_field = "ordering"

    class Meta:
        model = List
        fields = ["name", "is_done"]
