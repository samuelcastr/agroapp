from django.db import models
from cultivos.models import Cultivo  # Importar el módulo de cultivos

class CausaPerdida(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Perdida(models.Model):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name="perdidas")
    causa = models.ForeignKey(CausaPerdida, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)  # Ej: 12.5%
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.porcentaje}% - {self.cultivo.nombre}"
