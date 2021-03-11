from rest_framework import serializers
from apps.exceldata.models import ExcelData
class ExcelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelData
        fields = '__all__'





