from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Avg
from datetime import date

from cultivos.models import Cultivo
from cosechas.models import Cosecha
from perdidas.models import Perdida


class ReporteIndicadores(APIView):

    def get(self, request):
        inicio = request.GET.get("inicio")
        fin = request.GET.get("fin")

        if not inicio or not fin:
            return Response({"error": "Debe enviar parámetros inicio y fin."}, status=400)

        cosechas = Cosecha.objects.filter(fecha__range=[inicio, fin])
        perdidas = Perdida.objects.filter(fecha__range=[inicio, fin])

        rendimiento_total = cosechas.aggregate(total=Sum("rendimiento"))["total"] or 0
        perdida_total = perdidas.aggregate(total=Avg("porcentaje"))["total"] or 0

        rendimiento_neto = rendimiento_total * ((100 - perdida_total) / 100)

        return Response({
            "fecha_inicio": inicio,
            "fecha_fin": fin,
            "rendimiento_total_kg": rendimiento_total,
            "promedio_perdida_%": round(perdida_total, 2),
            "rendimiento_neto_estimado_kg": round(rendimiento_neto, 2)
        })
    
class ReporteTemporada(APIView):

    def get(self, request):
        anio = int(request.GET.get("anio", date.today().year))
        temporada = request.GET.get("temporada")

        if temporada not in ["primavera", "verano", "otoño", "invierno"]:
            return Response({"error": "Temporada inválida."}, status=400)

        # Rangos de meses por temporada
        temporadas = {
            "primavera": (9, 11),
            "verano": (12, 2),
            "otoño": (3, 5),
            "invierno": (6, 8)
        }

        inicio, fin = temporadas[temporada]

        cosechas = Cosecha.objects.filter(
            fecha__year=anio,
            fecha__month__gte=inicio,
            fecha__month__lte=fin
        )

        total = cosechas.aggregate(total=Sum("rendimiento"))["total"] or 0

        return Response({
            "anio": anio,
            "temporada": temporada,
            "rendimiento_total": total
        })