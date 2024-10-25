
from django.db import models
from core.models import TimeStampedModel


class State(TimeStampedModel):

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    name = models.CharField(
        max_length=75,
        verbose_name='nombre'
    )

    shipping_key = models.CharField(
        max_length=75
    )

    def __str__(self):
        return self.name
