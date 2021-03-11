from rest_framework.routers import SimpleRouter
from apps.exceldata.views import ExcelDataViewSet
router = SimpleRouter()
router.register('exceldatas', ExcelDataViewSet)
app_name = 'exceldata'
urlpatterns = []
urlpatterns += router.urls
