from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Perdida, CausaPerdida
from .serializers import PerdidaSerializer, CausaPerdidaSerializer
from .filters import PerdidaFilter

class PerdidaViewSet(viewsets.ModelViewSet):
    queryset = Perdida.objects.all()
    serializer_class = PerdidaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PerdidaFilter

    # ENDPOINT ADICIONAL (estadística)
    @action(detail=False, methods=['get'])
    def estadistica(self, request):
        total = Perdida.objects.count()
        if total == 0:
            return Response({"mensaje": "No hay pérdidas registradas."})

        promedio = sum(p.porcentaje for p in Perdida.objects.all()) / total

        return Response({
            "total_registros": total,
            "promedio_porcentaje_perdida": round(promedio, 2)
        })


class CausaPerdidaViewSet(viewsets.ModelViewSet):
    queryset = CausaPerdida.objects.all()
    serializer_class = CausaPerdidaSerializer
