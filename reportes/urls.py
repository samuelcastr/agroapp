from django.urls import path
from .views import ReporteIndicadores, ReporteTemporada

urlpatterns = [
    path("indicadores/", ReporteIndicadores.as_view(), name="reporte_indicadores"),
    path("temporada/", ReporteTemporada.as_view(), name="reporte_temporada"),
]
