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


class I18NModel(TimeStampModel):
    language = models.CharField(max_length=3, verbose_name='Version de langue')

    class Meta:
        abstract = True


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
    # content = tinymce_models.HTMLField(verbose_name='Texte régit', blank=True)
    title = models.CharField(
        max_length=200, verbose_name='Intitulé ou petite description', blank=True,
        help_text='Ce champs est facultatif, à defaut le nom du fichier sera utilisé commme Intitulé')
    file = models.FileField(
        # upload_to=action_plan_file_upload,
        verbose_name='Fichier du plan d\'action',
        # default='missions_plan_action_fr.pdf'

    )
    file_name = models.CharField(max_length=100, blank=True)
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        verbose_name='Version de langue du fichier')

    def get_title(self):
        return self.title if self.title else self.file_name

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
    ('whatsapp', 'Whatsapp'),
    ('telegram', 'Telegram'),
    ('linkedin', 'LinkedIn'),
    ('envelope', 'Gmail'),
    
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
    file = models.FileField(blank=True, verbose_name='Joindre un fichier')

    class Meta:
        verbose_name = 'A propos'
        verbose_name_plural = 'A propos'


class GeneralAssembly(TimeStampModel):
    description = models.TextField(verbose_name='Description du contenu')
    date = models.DateField(verbose_name='Assemblée générale du', blank=True)
    version = models.CharField(choices=LANGUAGE_CHOICES, max_length=3,
                               verbose_name='Version de langue du fichier')
    file = models.FileField(
        verbose_name='Fichier joint')

    class Meta:
        verbose_name = 'Assemblée Générale'
        verbose_name_plural = 'Assemblées Générales'

    def __str__(self):
        return self.description[:15] + '...'


class AdhesionCondition(TimeStampModel):
    content = models.TextField(verbose_name='Liste des conditions d\'adhésion',
                               help_text='Lister les conditions séparées par des virgules(,) exceptée la dernière !')
    file = models.FileField(verbose_name='Joindre un fichier', blank=True)

    language = models.CharField(
        max_length=3, verbose_name='Version de langue',  choices=LANGUAGE_CHOICES)

    def get_conditions_list(self):
        return self.content.split(';')

    def __str__(self):
        return self.get_conditions_list()[0] + '...'

    class Meta:
        verbose_name = 'Condition d\'adhésion'
        verbose_name_plural = 'Conditions d\'adhésion'


class InstitutionalPresentation(TimeStampModel):
    content = tinymce_models.HTMLField(verbose_name='Contenu')
    language = models.CharField(
        max_length=3,
        verbose_name='Version de langue du fichier',
        choices=LANGUAGE_CHOICES)

    file = models.FileField(verbose_name='Fichier joint', blank=True)

    both_fr_en = models.BooleanField(verbose_name='Pour les deux langues ?')

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Présentation institutionelle'
        verbose_name_plural = 'Présentation institutionelles'


class Coord(TimeStampModel):
    content = tinymce_models.HTMLField(verbose_name='Contenu')
    language = models.CharField(
        max_length=3, verbose_name='Version de langue', choices=LANGUAGE_CHOICES)

    def __str__(self):
        return str(self.language)

    class Meta:
        verbose_name = 'Coordonnée'
        verbose_name_plural = 'Coordonnées'


class Filiere(TimeStampModel):
    content = tinymce_models.HTMLField(verbose_name='Contenu')
    language = models.CharField(
        max_length=3,
        verbose_name='Version de langue du fichier',
        choices=LANGUAGE_CHOICES)

    file = models.FileField(verbose_name='Fichier joint', blank=True)

    both_fr_en = models.BooleanField(verbose_name='Pour les deux langues ?')

    class Meta:
        verbose_name = 'Filière et Formation'
        verbose_name_plural = 'Filières et Formations'

