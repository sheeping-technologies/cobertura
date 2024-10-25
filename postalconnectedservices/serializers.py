
from rest_framework import serializers
from postalconnectedservices.models import PostalConnectedService

NORMAL = 'NORMAL'
OCURRE = 'OCURRE'

class ZipCodeSerializer(serializers.Serializer):

    postal_code = serializers.CharField(
        min_length=5,
        max_length=5
    )


class PostalConnectedServiceSerializer(serializers.ModelSerializer):
    # postal_code = serializers.StringRelatedField()
    # service = serializers.StringRelatedField()

    class Meta:
        model = PostalConnectedService
        fields = '__all__'


class StateSerializer(serializers.Serializer):
    name = serializers.CharField()
    shipping_key = serializers.CharField()


class ServicesSerializer(serializers.Serializer):
    service = serializers.CharField()
    delivery_type = serializers.ChoiceField(
        choices=[
            (NORMAL, 'DOMICILIO'),
            (OCURRE, 'SUCURSAL'),
        ],
    )
    service_zone = serializers.CharField()
    coverage = serializers.BooleanField()
    extended_area =serializers.BooleanField()


class ApiCoveragesSerializer(serializers.Serializer):
    postal_code_sender = serializers.CharField()
    city_sender = serializers.CharField()
    state_sender = StateSerializer()
    postal_code_receiver = serializers.CharField()
    city_receiver =  serializers.CharField()
    state_receiver = StateSerializer()
    services = ServicesSerializer(many=True)


class GetCoveragesSerializer(serializers.Serializer):

    postal_code_sender = serializers.CharField(
        min_length=5,
        max_length=5
    )

    postal_code_receiver = serializers.CharField(
        min_length=5,
        max_length=5
    )


