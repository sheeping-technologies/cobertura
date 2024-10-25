from rest_framework import serializers
from carriers.models import Carrier


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = '__all__'
