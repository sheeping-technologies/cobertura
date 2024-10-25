from rest_framework import serializers
from neighborhoods.models import Neighborhood


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'
