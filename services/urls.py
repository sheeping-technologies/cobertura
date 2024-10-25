from services.views import ServicesViewSet
from rest_framework.routers import DefaultRouter

app_name = 'services'

router = DefaultRouter()
router.register(r'', ServicesViewSet)

urlpatterns = router.urls
