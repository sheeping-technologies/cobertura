from cities.views import CitiesViewSet
from rest_framework.routers import DefaultRouter

app_name = 'cities'

router = DefaultRouter()
router.register(r'', CitiesViewSet)

urlpatterns = router.urls
