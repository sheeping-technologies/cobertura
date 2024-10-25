from rest_framework import viewsets

from carriers.models import Carrier

from carriers.serializers import CarrierSerializer

from core.api_mixins import DefaultMixins


class CarriersViewSet(DefaultMixins, viewsets.ModelViewSet):
    serializer_class = CarrierSerializer
    queryset = Carrier.objects.all()
