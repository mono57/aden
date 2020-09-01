from django.db import models
from aden.utils import TimeStampModel
from carriere.managers import OfferManager, ResumeManager
# Create your models here.


class Offer(TimeStampModel):
    entreprise = models.CharField(
        max_length=100, verbose_name='Nom de l\'entreprise')
    label = models.CharField(
        max_length=150, verbose_name='Intitulé de l\'offre')
    description = models.TextField(verbose_name='Description de l\'offre')
    profil = models.TextField(verbose_name='Profil reherché',
                              help_text='Listez les profils separés par des virgules')

    objects = OfferManager()

    def get_profils(self):
        return self.profil.split(',')

    class Meta:
        verbose_name = 'Offre d\'emploi'
        verbose_name_plural = 'Offres d\'emploi'

    def __str__(self):
        return self.label


class Resume(TimeStampModel):
    full_name = models.CharField(
        max_length=150, verbose_name='Nom(s) et Prénom(s)')
    filiere = models.CharField(max_length=100, verbose_name='Filière')
    promotion = models.CharField(max_length=50, verbose_name='Promotion')
    file = models.FileField(verbose_name='Fichier de CV')

    objects = ResumeManager()

    class Meta:
        verbose_name = 'Curriculum Vitae'      
        verbose_name_plural = 'Curriculums Vitaes'      

    def __str__(self):
        return self.full_name