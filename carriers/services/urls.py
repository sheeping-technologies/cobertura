from services.views import ServicesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ServicesViewSet)

urlpatterns = router.urls
