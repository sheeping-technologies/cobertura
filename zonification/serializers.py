from rest_framework import serializers
from zonification.models import Group, Zone


class GroupSerializer(serializers.ModelSerializer):
    carrier = serializers.StringRelatedField()

    class Meta:
        model = Group
        fields = '__all__'


class ZoneSerializer(serializers.ModelSerializer):
    carrier = serializers.StringRelatedField()

    class Meta:
        model = Zone
        fields = '__all__'


class GetZoneSerializer(serializers.Serializer):

    postal_code_sender = serializers.CharField(
        min_length=5,
        max_length=5
    )

    postal_code_receiver = serializers.CharField(
        min_length=5,
        max_length=5
    )
