from rest_framework import serializers
from states.models import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name', 'shipping_key']
