from rest_framework.response import Response
from rest_framework import viewsets
from zonification.models import Group, Zone
from zonification.serializers import GroupSerializer, ZoneSerializer, GetZoneSerializer
from core.api_mixins import DefaultMixins
from rest_framework.views import APIView


class GroupsViewSet(DefaultMixins, viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class ZonesViewSet(DefaultMixins, viewsets.ModelViewSet):
    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()


class GetZone(DefaultMixins, APIView):

    def post(self, request, carrier='', **kwargs):
        group_sender = ''
        group_receiver = ''
        carrier = carrier.upper()

        srz = GetZoneSerializer(
            data=self.request.data
        )

        if not srz.is_valid():
            return Response({'error': srz.errors}, status=406)

        postal_code_sender = srz.data.get('postal_code_sender', 0)
        postal_code_receiver = srz.data.get('postal_code_receiver', 0)

        sender = Group.objects.filter(
            carrier__name=carrier,
            cp_from__lte=postal_code_sender,
            cp_to__gte=postal_code_sender
        ).first()

        receiver = Group.objects.filter(
            carrier__name=carrier,
            cp_from__lte=postal_code_receiver,
            cp_to__gte=postal_code_receiver
        ).first()

        if sender and receiver:
            group_sender = getattr(sender, 'group')
            group_receiver = getattr(receiver, 'group')

        zone = Zone.objects.filter(carrier__name=carrier, group_sender=group_sender, group_receiver=group_receiver)

        return Response(ZoneSerializer(zone, many=True).data, status=200)
