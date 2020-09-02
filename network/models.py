from django.db import models

from aden.utils import TimeStampModel


class NetworkNews(TimeStampModel):
    title = models.CharField(
        max_length=150,
        verbose_name='Titre'
    )
    description = models.TextField(verbose_name='Description', blank=True)
    link = models.URLField(verbose_name='Lien de vers le details', blank=True)
    file = models.FileField(verbose_name='Fichier', blank=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
    
