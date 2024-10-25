from states.views import StatesViewSet
from rest_framework.routers import DefaultRouter

app_name = 'states'

router = DefaultRouter()
router.register(r'', StatesViewSet)

urlpatterns = router.urls
