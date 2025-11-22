import django_filters
from .models import Cultivo

class CultivoFilter(django_filters.FilterSet):
    fecha_siembra_desde = django_filters.DateFilter(field_name="fecha_siembra", lookup_expr='gte')
    fecha_siembra_hasta = django_filters.DateFilter(field_name="fecha_siembra", lookup_expr='lte')
    ciclo = django_filters.CharFilter(field_name="ciclo", lookup_expr='icontains')

    class Meta:
        model = Cultivo
        fields = ['ciclo', 'fecha_siembra_desde', 'fecha_siembra_hasta']
