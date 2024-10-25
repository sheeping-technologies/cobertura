from rest_framework import viewsets
from services.models import Service
from services.serializers import ServiceSerializer

from core.api_mixins import DefaultMixins


class ServicesViewSet(DefaultMixins, viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
