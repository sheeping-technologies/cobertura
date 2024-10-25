from rest_framework import viewsets
from cities.models import City
from cities.serializers import CitySerializer
from core.api_mixins import DefaultMixins


class CitiesViewSet(DefaultMixins, viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
