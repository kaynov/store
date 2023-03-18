from django_filters import rest_framework as dj_filters

from .models import Product


class ProductFilterSet(dj_filters.FilterSet):
    title = dj_filters.CharFilter(field_name="name", lookup_expr="icontains")

    order_by_field = "ordering"

    class Meta:
        model = Product
        fields = [
            "name",
        ]
