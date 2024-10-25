from rest_framework import viewsets
from neighborhoods.models import Neighborhood
from neighborhoods.serializers import NeighborhoodSerializer

from core.api_mixins import DefaultMixins


class NeighborhoodsViewSet(DefaultMixins, viewsets.ModelViewSet):
    serializer_class = NeighborhoodSerializer
    queryset = Neighborhood.objects.all()
