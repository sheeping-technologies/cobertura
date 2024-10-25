from carriers.views import CarriersViewSet
from rest_framework.routers import DefaultRouter

app_name = 'carriers'

router = DefaultRouter()
router.register(r'', CarriersViewSet)

urlpatterns = router.urls
