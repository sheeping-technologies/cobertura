from django.urls import path, include

from zonification.views import GroupsViewSet, ZonesViewSet, GetZone
from rest_framework.routers import DefaultRouter

app_name = 'fedex'

router = DefaultRouter()
router.register(r'grupos', GroupsViewSet, basename='fedex_groups')
router.register(r'zonas', ZonesViewSet, basename='fedex_zones')

urlpatterns = [
    path('detalles-zona/<str:carrier>/', GetZone.as_view(), name='get_zone'),
    path('', include(router.urls)),
]
