from django.db import models
from postalcodes.models import PostalCode
from services.models import Service

from core.models import TimeStampedModel

NORMAL = 'NORMAL'
OCURRE = 'OCURRE'


class PostalConnectedService(TimeStampedModel):
    class Meta:
        verbose_name = 'Cobertura'
        verbose_name_plural = 'Coberturas'

    postal_code = models.ForeignKey(
        PostalCode,
        related_name='services',
        on_delete=models.CASCADE,
        verbose_name = 'Codigo Postal',
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        verbose_name = 'Servicio',
    )

    delivery_type = models.CharField(
        default='NORMAL',
        choices=[
            (NORMAL, 'DOMICILIO'),
            (OCURRE, 'SUCURSAL'),
        ],
        max_length=75,
        verbose_name = 'Tipo De Entrega',
    )

    service_zone = models.CharField(
        blank=True,
        default='',
        max_length=75,
        verbose_name = 'Zona',
    )

    coverage = models.BooleanField(
        default=False,
        verbose_name = 'Cobertura',
    )

    extended_area = models.BooleanField(
        default=False,
        verbose_name = 'Zona Extendida',
    )

    def __str__(self):
        return F'{self.postal_code.postal_code} - {self.service.name}'
