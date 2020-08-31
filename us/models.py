from django.db import models
from aden.utils import TimeStampModel
# Create your models here.
from cloudinary.models import CloudinaryField
from tinymce import models as tinymce_models
# from cloudinary_storage.storage import RawMediaCloudinaryStorage


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
    photo = CloudinaryField(resource_type='image', verbose_name='Photo')
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


def action_plan_file_upload(instance, filename):
    return 'missions_plan_action_{}.{}'.format(instance.language, str(filename).split('.')[1])

class Footer(TimeStampModel):
    text = models.TextField(verbose_name='Texte')

    class Meta:
        verbose_name = 'Pied de page'
        verbose_name_plural = 'Pieds de page'
class ActionPlan(TimeStampModel):
    # year = models.DateField(verbose_name='Année d\'exécution')
    content = tinymce_models.HTMLField(verbose_name='Texte régit', blank=True)
    file = models.FileField(
        # upload_to=action_plan_file_upload,
        verbose_name='Fichier du plan d\'action',
        blank=True,
        # default='missions_plan_action_fr.pdf'
        )
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        verbose_name='Version de langue du fichier')

    class Meta:
        verbose_name = 'Plan d\'action'
        verbose_name_plural = 'Plans d\'actions'


def status_file_upload(instance, filename):
    return 'statut_{}.{}'.format(instance.language, str(filename).split('.')[1])


class Status(TimeStampModel):
    content = tinymce_models.HTMLField(verbose_name='Texte régit', blank=True)
    file = models.FileField(
        # upload_to=status_file_upload,
        verbose_name='Joindre le fichier de statut', blank=True,
        # default='statut_fr.pdf'
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


def regulation_file_upload(instance, filename):
    return 'reglement_interieur_{}.{}'.format(instance.language, str(filename).split('.')[1])


class InternalRegulation(TimeStampModel):
    content = tinymce_models.HTMLField(verbose_name='Texte régit', blank=True)
    file = models.FileField(
        # upload_to='regulations/',
        verbose_name='Joindre le fichier',
        blank=True,
        # default='reglement_interieur_fr.pdf'
        # storage=RawMediaCloudinaryStorage()
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
        choices=SOCIAL_CHOICES,
        verbose_name='Type du réseau'
    )
    accessibility = models.CharField(
        max_length=10,
        choices=(('private', 'Membre seulement'), ('public', 'Public')),
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
