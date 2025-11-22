from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg

from .models import Cosecha, Lote
from .serializers import CosechaSerializer, LoteSerializer
from .filters import CosechaFilter


class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer


class CosechaViewSet(viewsets.ModelViewSet):
    queryset = Cosecha.objects.all()
    serializer_class = CosechaSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = CosechaFilter

    # ENDPOINT ADICIONAL
    @action(detail=False, methods=['get'])
    def promedio_rendimiento(self, request):
        promedio = Cosecha.objects.aggregate(avg=Avg("rendimiento_kg"))["avg"]

        return Response({
            "promedio_general_rendimiento_kg": promedio or 0
        })
