from django.db import models

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_siembra = models.DateField()
    fecha_cosecha_estimada = models.DateField()
    ciclo = models.CharField(max_length=50)  # Ej: corto, medio, largo

    def __str__(self):
        return self.nombre


class Variedad(models.Model):
    cultivo = models.ForeignKey(Cultivo, related_name="variedades", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.cultivo.nombre}"
