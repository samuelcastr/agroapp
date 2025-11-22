from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now

from .models import Cultivo
from .serializers import CultivoSerializer
from .filters import CultivoFilter
from django_filters.rest_framework import DjangoFilterBackend


class CultivoViewSet(viewsets.ModelViewSet):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer
    
    # Filtros obligatorios
    filter_backends = [DjangoFilterBackend]
    filterset_class = CultivoFilter

    # ENDPOINT ADICIONAL (CÁLCULO DE PROYECCIÓN)
    @action(detail=True, methods=['get'])
    def proyeccion(self, request, pk=None):
        cultivo = self.get_object()

        dias_restantes = (cultivo.fecha_cosecha_estimada - now().date()).days
        dias_totales = (cultivo.fecha_cosecha_estimada - cultivo.fecha_siembra).days
        dias_transcurridos = (now().date() - cultivo.fecha_siembra).days

        avance = max(0, min(100, int((dias_transcurridos / dias_totales) * 100)))

        return Response({
            "cultivo": cultivo.nombre,
            "dias_restantes": dias_restantes,
            "avance_porcentaje": avance
        })
