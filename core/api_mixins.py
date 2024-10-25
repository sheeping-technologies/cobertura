
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAcceptable


class DefaultMixins(object):

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    )

    permission_classes = (IsAuthenticated,)


class APIValidators(object):

    @staticmethod
    def valid_value(value, message_error):
        if not value:
            raise NotAcceptable(detail=message_error)

    @staticmethod
    def valid_method_name(class_obj, method_name):
        if not hasattr(class_obj, method_name):
            raise NotAcceptable(detail=f'Metodo {method_name} no esta definido')
