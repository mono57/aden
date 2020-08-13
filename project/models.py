from django.db import models
from aden.utils import TimeStampModel
# Create your models here.


class Project(TimeStampModel):
    owner = models.CharField(
        max_length=100,
        verbose_name='Nom(s) et Prénom(s) du porteur de projet'
    )
    filiere = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Filière'
    )
    school_out_date = models.DateField(
        blank=True,
        verbose_name='Date de sortie de l\'ENSAI'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Désignation du projet'
    )
    description = models.TextField(
        verbose_name='Résumé du projet'
    )
    estimatif_cost = models.CharField(
        max_length=250,
        verbose_name='Coût estimatif',
        help_text='Coût en FCFA'
    )
    federation = models.TextField(
        verbose_name='Particularité en terme de fédération des filères de l\'ENSAI'
    )
    selected = models.BooleanField(
        verbose_name='Souhaitez vous participer à toutes \
            les phases de mise en oeuvre de ce projet si jamais il est retenu ?'
    )

    class Meta:
        verbose_name = 'Idée de projet fédérateurs des filières ENSAI'
        verbose_name = 'Idées de projet fédérateurs des filières ENSAI'
