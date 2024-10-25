from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from services.models import Service
from carriers.serializers.services_serializers import ServiceSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated]
