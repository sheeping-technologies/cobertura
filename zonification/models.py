from django.db import models
from carriers.models import Carrier
from states.models import State
from core.models import TimeStampedModel


class Group(TimeStampedModel):

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    carrier = models.ForeignKey(
        Carrier,
        default=1,
        on_delete=models.CASCADE,
        verbose_name = 'Paqueteria'
    )

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        verbose_name = 'Estado'
    )

    cp_from = models.IntegerField(
        default=20000,
        verbose_name = 'Codigo Postal Desde'
    )

    cp_to = models.IntegerField(
        default=20997,
        verbose_name = 'Codigo Postal Hasta'
    )

    group = models.CharField(
        max_length=5,
        default='L',
        verbose_name = 'Grupo'
    )

    def __str__(self):
        return f' {self.cp_from} - {self.cp_to}'


class Zone(TimeStampedModel):

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    carrier = models.ForeignKey(
        Carrier,
        default=1,
        on_delete=models.CASCADE,
        verbose_name = 'Paqueteria'
    )

    group_sender = models.CharField(
        max_length=5,
        default='A',
        verbose_name = 'Grupo Origen'
    )

    group_receiver = models.CharField(
        max_length=5,
        default='A',
        verbose_name = 'Grupo Destino'
    )

    zone = models.CharField(
        max_length=5,
        default='1',
        verbose_name = 'Zona'
    )

    def __str__(self):
        return f'{self.group_sender} - {self.group_receiver}: {self.zone}'
