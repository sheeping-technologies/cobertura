from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from postalcodes.models import PostalCode
from postalcodes.serializers import PostalCodeDetailSerializer
from postalconnectedservices.models import PostalConnectedService
from postalconnectedservices.serializers import (
    PostalConnectedServiceSerializer,
    ZipCodeSerializer,
    GetCoveragesSerializer
)
from zonification.models import Group, Zone
from core.api_mixins import DefaultMixins

FEDEX = 'FEDEX'
DHL = 'DHL'


class PostalConnectedServicesViewSet(DefaultMixins, viewsets.ModelViewSet):
    serializer_class = PostalConnectedServiceSerializer
    queryset = PostalConnectedService.objects.all().order_by('-created')


class ZipCodeDetails(DefaultMixins, APIView):

    def get(self, request, postal_code='', **kwargs):
        srz = ZipCodeSerializer(data={"postal_code": postal_code})
        if not srz.is_valid():
            return Response({'error': srz.errors}, status=406)
        # TODO

        return Response(

            PostalCodeDetailSerializer(PostalCode.objects.filter(postal_code=postal_code), many=True).data,
            status=200
        )


class ApiCoverages(DefaultMixins, APIView):

    def post(self, request, **kwargs):
        srz = GetCoveragesSerializer(
            data=self.request.data
        )

        if not srz.is_valid():
            return Response({'error': srz.errors, 'error_code': 'CP01'}, status=406)
        
        postal_code_sender = PostalCode.objects.filter(postal_code=self.request.data.get('postal_code_sender')).first()
        postal_code_receiver = PostalCode.objects.filter(postal_code=self.request.data.get('postal_code_receiver')).first()

        if not postal_code_sender:
            return Response({'error': {'postal_code_sender': ['El codigo postal de origen es incorrecto']}, 'error_code': 'CP02'}, status=406)

        if not postal_code_receiver:
            return Response({'error': {'postal_code_receiver': ['El codigo postal de destino es incorrecto']}, 'error_code': 'CP02'}, status=406)
        
        service_zone_fedex = get_service_zone(postal_code_sender.postal_code, postal_code_receiver.postal_code, FEDEX)
        service_zone_dhl = get_service_zone(postal_code_sender.postal_code, postal_code_receiver.postal_code, DHL)
        
        service_zone = {
            FEDEX: service_zone_fedex,
            DHL: service_zone_dhl,
        }

        coverage_services_sender = PostalConnectedService.objects.filter(postal_code__postal_code=postal_code_sender)
        coverage_services_receiver = PostalConnectedService.objects.filter(postal_code__postal_code=postal_code_receiver)
        coverage_services_match = {}
        
        for service_receiver in coverage_services_receiver:
            for service_sender in coverage_services_sender:
                if (service_receiver.service == service_sender.service) and (service_receiver.service_zone == service_sender.service_zone):
                    #TODO: CALCULATE SERVICE ZONE FEDEX, DHL, SENDEX
                    carrier_service = str(service_receiver.service).split(' ')[0]
                    if carrier_service in service_zone.keys():
                        service_receiver.service_zone = service_zone.get(F'{carrier_service}', '')
                    #END: CALCULATE SERVICE ZONE FEDEX, DHL, SENDEX    
                    
                    coverage_services_match[F'{str(service_receiver.service)}'] = {
                        'shipping_company': carrier_service,
                        'shipping_services': str(service_receiver.service),
                        'delivery_type': service_receiver.delivery_type,                        
                        'service_zone': service_receiver.service_zone,
                        'extended_area': service_sender.extended_area or service_receiver.extended_area,
                    }
        

        return Response(
            {
                'postal_code_sender': postal_code_sender.postal_code,
                'city_sender': postal_code_sender.city.name,
                'state_sender':{
                    'name': postal_code_sender.state.name,
                    'shipping_key': postal_code_sender.state.shipping_key,
                },
                'postal_code_receiver': postal_code_receiver.postal_code,
                'city_receiver': postal_code_receiver.city.name,
                'state_receiver': {
                    'name': postal_code_receiver.state.name,
                    'shipping_key': postal_code_receiver.state.shipping_key,
                },
                'services': coverage_services_match
            },
            status=200
        )


def get_service_zone(postal_code_sender, postal_code_receiver, carrier):
    group_sender = ''
    group_receiver = ''
    carrier = carrier.upper()

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

    if not sender or not receiver:
        return ""
    
    group_sender = getattr(sender, 'group')
    group_receiver = getattr(receiver, 'group')

    zone = Zone.objects.filter(carrier__name=carrier, group_sender=group_sender, group_receiver=group_receiver).first()

    if not zone:
        return ""
    
    return zone.zone