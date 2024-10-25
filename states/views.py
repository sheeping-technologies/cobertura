from rest_framework import viewsets
from states.models import State
from states.serializers import StateSerializer
from core.api_mixins import DefaultMixins


class StatesViewSet(DefaultMixins, viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
