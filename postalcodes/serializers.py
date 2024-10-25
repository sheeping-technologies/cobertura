from rest_framework import serializers
from postalcodes.models import PostalCode
from postalconnectedservices.serializers import PostalConnectedServiceSerializer
from states.serializers import StateSerializer


class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalCode
        fields = '__all__'


class PostalCodeDetailSerializer(serializers.ModelSerializer):
    neighborhoods = serializers.StringRelatedField(many=True)
    city = serializers.StringRelatedField()
    state = StateSerializer()
    services = PostalConnectedServiceSerializer(many=True)

    class Meta:
        model = PostalCode
        fields = ['postal_code', 'neighborhoods', 'city', 'state', 'services']
