from rest_framework.routers import SimpleRouter
from apps.cotizacion.views import CotizacionViewSet
router = SimpleRouter()
router.register('cotizaciones', CotizacionViewSet)
app_name = 'cotizacion'
urlpatterns = []
urlpatterns += router.urls
