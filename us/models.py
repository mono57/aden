from django.db import models
from aden.utils import TimeStampModel
# Create your models here.

LANGUAGE_CHOICES = (
    ('en', 'Anglaise'),
    ('fr', 'Française')
)


class StrategicComity(TimeStampModel):
    full_name = models.CharField(max_length=150, verbose_name="Nom complet")
    title = models.CharField(max_length=180, verbose_name='Titre à l\'ADEN')
    rule = models.CharField(max_length=150, verbose_name="Fonction ou Role")
    location = models.CharField(max_length=150, verbose_name="Domicile")
    promotion = models.CharField(max_length=80, verbose_name='Promotion')
    photo = models.ImageField(upload_to='photos/', verbose_name='Photo')
    grade = models.CharField(
        max_length=2,
        verbose_name='Priorité',
        choices=(
            ('1', 'Niveau 1'),
            ('2', 'Niveau 2'),
            ('3', 'Niveau 3'),
        )
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Comité Stratégique'
        verbose_name_plural = 'Comités Stratégiques'


class ActionPlan(TimeStampModel):
    year = models.DateField(verbose_name='Année d\'exécution')
    file = models.FileField(
        upload_to='actions_plan/',
        verbose_name='Fichier du plan d\'action')
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        verbose_name='Version de langue du fichier')

    class Meta:
        verbose_name = 'Plan d\'action'
        verbose_name_plural = 'Plans d\'actions'


class Status(TimeStampModel):
    file = models.FileField(
        upload_to='status/',
        verbose_name='Joindre le fichier de statut'
    )
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        verbose_name='Version de langue du fichier'
    )

    def __str__(self):
        return 'Statut Version : {}'.format(self.language)
    class Meta:
        verbose_name = 'Statut de l\'association'
        verbose_name_plural = 'Statuts de l\'association'

class InternalRegulation(TimeStampModel):
    file = models.FileField(
        upload_to='status/',
        verbose_name='Joindre le fichier'
    )
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        verbose_name='Version de langue du fichier'
    )

    class Meta:
        verbose_name = 'Règlement interieur'
        verbose_name_plural = 'Règlements interieurs'

SOCIAL_CHOICES = (
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
    ('telegram', 'Telegram'),
    ('linkedin', 'LinkedIn'),
)

class SocialNetwork(TimeStampModel):
    name = models.CharField(
        max_length=20, 
        verbose_name='Nom du réseau social')
    type = models.CharField(
        max_length=10,
        choices = SOCIAL_CHOICES,
        verbose_name='Type du réseau'
    )
    accessibility = models.CharField(
        max_length=10,
        choices = (('private', 'Membre seulement'), ('public', 'Public')),
        verbose_name='Visibilité',
        default='public'
    )
    link = models.URLField(verbose_name='Lien direct du réseau social')

    class Meta:
        verbose_name = 'Réseau Social'
        verbose_name_plural = 'Résaux sociaux'

class About(TimeStampModel):
    content = models.TextField(verbose_name='Contenu de a propos')
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        verbose_name='Version de langue du fichier'
    )

    class Meta:
        verbose_name = 'A propos'
        verbose_name_plural = 'A propos'