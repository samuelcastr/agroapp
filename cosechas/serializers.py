from rest_framework import serializers
from .models import Cosecha, Lote
from datetime import date

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'


class CosechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosecha
        fields = '__all__'

    # VALIDACIÓN PERSONALIZADA
    def validate(self, data):
        fecha = data.get("fecha_cosecha", getattr(self.instance, "fecha_cosecha", None))
        rendimiento = data.get("rendimiento_kg", getattr(self.instance, "rendimiento_kg", None))

        if fecha and fecha > date.today():
            raise serializers.ValidationError("La fecha de cosecha no puede estar en el futuro.")

        if rendimiento is not None and rendimiento <= 0:
            raise serializers.ValidationError("El rendimiento debe ser mayor que 0 kg.")

        return data
