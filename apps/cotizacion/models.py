from django.db import models


class Cotizacion(models.Model):
    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
    NIT = models.CharField(max_length=11, unique=False)
    NombreEmpresa = models.CharField(max_length=255, unique=False)
    NombreSolicitante = models.CharField(max_length=255, unique=False)
    Cargo = models.CharField(max_length=255, unique=False)
    Direccion = models.CharField(max_length=255, unique=False)
    Email = models.CharField(max_length=255, unique=False)
    Telefono = models.CharField(max_length=10, unique=False)
    Origen = models.CharField(max_length=255, unique=False)
    Destino = models.CharField(max_length=255, unique=False)
    TipoOperacion = models.CharField(max_length=255, unique=False)
    TipoContenedor = models.CharField(max_length=255, unique=False)
    #Peso = models.FloatField(blank=True, default=0)
    Cotizacion = models.DecimalField(max_digits=22, decimal_places=2)
    Fecha = models.DateTimeField(auto_now_add=True, blank=True)
