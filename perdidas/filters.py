import django_filters
from .models import Perdida

class PerdidaFilter(django_filters.FilterSet):
    fecha_inicio = django_filters.DateFilter(field_name="fecha", lookup_expr="gte")
    fecha_fin = django_filters.DateFilter(field_name="fecha", lookup_expr="lte")
    cultivo = django_filters.NumberFilter(field_name="cultivo__id")

    class Meta:
        model = Perdida
        fields = ["causa", "cultivo", "fecha_inicio", "fecha_fin"]
