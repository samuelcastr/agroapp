from rest_framework import serializers
from .models import Perdida, CausaPerdida
from datetime import date


class CausaPerdidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CausaPerdida
        fields = '__all__'


class PerdidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perdida
        fields = '__all__'

    # VALIDACIONES PERSONALIZADAS
    def validate(self, data):
        porcentaje = data.get("porcentaje")
        fecha = data.get("fecha")
        cultivo = data.get("cultivo")

        if porcentaje <= 0 or porcentaje > 100:
            raise serializers.ValidationError(
                "El porcentaje debe ser mayor a 0 y menor o igual a 100."
            )

        if fecha > date.today():
            raise serializers.ValidationError(
                "La fecha de pérdida no puede ser futura."
            )

        # Validar que la pérdida sea después de la siembra
        if cultivo and fecha < cultivo.fecha_siembra:
            raise serializers.ValidationError(
                "La fecha de pérdida no puede ser antes de la fecha de siembra del cultivo."
            )

        return data
