import django_filters
from .models import Cosecha

class CosechaFilter(django_filters.FilterSet):
    fecha_cosecha = django_filters.DateFromToRangeFilter()
    rendimiento_kg = django_filters.NumericRangeFilter()

    class Meta:
        model = Cosecha
        fields = ['fecha_cosecha', 'rendimiento_kg', 'cultivo', 'lote']
