from neighborhoods.views import NeighborhoodsViewSet
from rest_framework.routers import DefaultRouter

app_name = 'neighborhoods'

router = DefaultRouter()
router.register(r'', NeighborhoodsViewSet)

urlpatterns = router.urls
