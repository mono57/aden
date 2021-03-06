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
    school_out_date = models.CharField(
        max_length=8,
        blank=True,
        verbose_name='Date de sortie de l\'ENSAI',
        help_text='Exemple: 2014'
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

class BaseProject(TimeStampModel):
    content = models.TextField(verbose_name='Petite description du projet')
    file = models.FileField(verbose_name='Joindre un document de projet')

    def __str__(self):
        return self.content[:20]

    class Meta:
        abstract = True
    

class InstitutionalProject(BaseProject):
    class Meta:
        verbose_name = 'Projet institutionel'
        verbose_name_plural = 'Projets institutionels'


class IndustrialProject(BaseProject):
    class Meta:
        verbose_name = 'Projet industriel'
        verbose_name_plural = 'Projets industriels'