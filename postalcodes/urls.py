from postalcodes.views import PostalCodesViewSet
from rest_framework.routers import DefaultRouter

app_name = 'postal_codes'

router = DefaultRouter()
router.register(r'', PostalCodesViewSet)

urlpatterns = router.urls
