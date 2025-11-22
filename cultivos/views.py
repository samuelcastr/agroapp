from rest_framework import viewsets, status
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
    
    # filtros obligatorios
    filter_backends = [DjangoFilterBackend]
    filterset_class = CultivoFilter

    # ENDPOINT ADICIONAL (CÁLCULO DE PROYECCIÓN)
    @action(detail=True, methods=['get'])
    def proyeccion(self, request, pk=None):
        cultivo = self.get_object()
        dias_restantes = (cultivo.fecha_cosecha_estimada - now().date()).days
        
        return Response({
            "cultivo": cultivo.nombre,
            "dias_para_cosecha": dias_restantes
        })
