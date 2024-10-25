from django.urls import path, include

from postalconnectedservices.views import PostalConnectedServicesViewSet, ZipCodeDetails, ApiCoverages
from rest_framework.routers import DefaultRouter

app_name = 'postal_connected_services'

router = DefaultRouter()
router.register(r'', PostalConnectedServicesViewSet, basename='postal_connected_services')

urlpatterns = [
    path('api/', ApiCoverages.as_view(), name='postal_code_api'),
    path('detalles-codigo-postal/', ZipCodeDetails.as_view(), name='postal_code_details_empty'),
    path('detalles-codigo-postal/<str:postal_code>/', ZipCodeDetails.as_view(), name='postal_code_details'),
    path('', include(router.urls)),
]
