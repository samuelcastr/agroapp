from rest_framework import serializers
from .models import Cultivo, Variedad
from datetime import date

class VariedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variedad
        fields = '__all__'


class CultivoSerializer(serializers.ModelSerializer):
    variedades = VariedadSerializer(many=True, read_only=True)

    class Meta:
        model = Cultivo
        fields = '__all__'

    # VALIDACIÓN PERSONALIZADA
    def validate(self, data):
        fecha_siembra = data.get('fecha_siembra')
        fecha_cosecha_estimada = data.get('fecha_cosecha_estimada')

        if fecha_cosecha_estimada <= fecha_siembra:
            raise serializers.ValidationError(
                "La fecha de cosecha estimada debe ser mayor que la fecha de siembra."
            )

        if fecha_siembra > date.today():
            raise serializers.ValidationError(
                "La fecha de siembra no puede ser en el futuro."
            )

        return data
