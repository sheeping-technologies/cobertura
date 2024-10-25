
from django.db import models

from core.models import TimeStampedModel

from states.models import State
from cities.models import City


class PostalCode(TimeStampedModel):

    class Meta:
        verbose_name = 'Codigo Postal'
        verbose_name_plural = 'Codigos Postales'

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        verbose_name = 'Estado'
    )

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name = 'Ciudad'
    )

    postal_code = models.CharField(
        max_length=75,
        verbose_name = 'Codigo Postal'
    )

    def __str__(self):
        return self.postal_code
