from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateField(
        auto_now=False, auto_now_add=True, verbose_name='Date de création')
    updated_at = models.DateField(
        auto_now=True, auto_now_add=False, verbose_name='Date de la dernière modification')

    class Meta:
        abstract = True
