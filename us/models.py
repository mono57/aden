from django.db import models
from aden.utils import TimeStampModel
# Create your models here.


class StrategicComity(TimeStampModel):
    full_name = models.CharField(max_length=150, verbose_name="Nom complet")
    title = models.CharField(max_length=180, verbose_name='Titre à l\'ADEN')
    rule = models.CharField(max_length=150, verbose_name="Fonction ou Role")
    location = models.CharField(max_length=150, verbose_name="Domicile")
    promotion = models.CharField(max_length=80, verbose_name='Promotion')
    photo = models.ImageField(upload_to='photos/', verbose_name='Photo')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Comité Stratégique'
        verbose_name_plural = 'Comités Stratégiques'