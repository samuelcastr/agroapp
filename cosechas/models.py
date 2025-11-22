from django.db import models
from cultivos.models import Cultivo  # Importar del módulo Cultivos

class Lote(models.Model):
    nombre = models.CharField(max_length=100)
    area_m2 = models.FloatField()  # área del lote

    def __str__(self):
        return self.nombre


class Cosecha(models.Model):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name="cosechas")
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name="cosechas")

    fecha_cosecha = models.DateField()
    rendimiento_kg = models.FloatField()  # rendimiento obtenido en el lote

    def __str__(self):
        return f"Cosecha de {self.cultivo.nombre} en {self.lote.nombre}"
