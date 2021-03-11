from django.shortcuts import render
from rest_framework import viewsets
from apps.cotizacion.serializers import CotizacionSerializer
from apps.cotizacion.models import Cotizacion
from django.core.mail import EmailMessage
from django.conf import settings
import datetime
import locale

class CotizacionViewSet(viewsets.ModelViewSet):
    serializer_class = CotizacionSerializer
    queryset = Cotizacion.objects.all()
    def create(self, request, *args, **kwargs):
        locale.setlocale(locale.LC_ALL, '')
        subject = 'Cotización de parte de LTTL a nombre de ' + request.data.get('NombreSolicitante')
        html_message = request.data.get('CorreoAEnviar')
        to = request.data.get('Email')
        email = EmailMessage(subject, html_message, to=[to], from_email=settings.EMAIL_HOST_USER)
        email.content_subtype = "html"
        email.send()
        return super().create(request, *args, **kwargs)
