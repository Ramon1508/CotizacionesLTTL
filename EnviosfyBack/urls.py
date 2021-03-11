
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cotizacion/', include('apps.cotizacion.urls')),
    path('exceldata/', include('apps.exceldata.urls')),
]
