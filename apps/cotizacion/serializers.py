from rest_framework import serializers
from apps.cotizacion.models import Cotizacion
class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = '__all__'





