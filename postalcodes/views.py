from rest_framework import viewsets
from postalcodes.models import PostalCode
from postalcodes.serializers import PostalCodeSerializer
from core.api_mixins import DefaultMixins


class PostalCodesViewSet(DefaultMixins, viewsets.ModelViewSet):
    serializer_class = PostalCodeSerializer
    queryset = PostalCode.objects.all()
