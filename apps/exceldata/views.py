from django.shortcuts import render
from rest_framework import viewsets
from apps.exceldata.serializers import ExcelDataSerializer
from apps.exceldata.models import ExcelData


class ExcelDataViewSet(viewsets.ModelViewSet):
    serializer_class = ExcelDataSerializer
    queryset = ExcelData.objects.all()
