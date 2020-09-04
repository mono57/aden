from django.db import models
from django.contrib.auth import get_user_model
from aden.utils import TimeStampModel
from cloudinary.models import CloudinaryField

User = get_user_model()


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


class BaseGroup(TimeStampModel):
    name = models.CharField(
        max_length=100, verbose_name='Nom de l\'association')
    filiere_promo = models.CharField(
        max_length=100, verbose_name='Filière(s) - Promotion(s)')

    
    # members_count = models.IntegerField(verbose_name='Nombre de membre')
    siege = models.CharField(max_length=100, verbose_name='Siège')
    contact = models.CharField(max_length=50, verbose_name='Contact')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Association(BaseGroup):
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                              verbose_name='Répresentant', related_name='association')
    members = models.ManyToManyField(
        User, related_name='associations', blank=True, verbose_name='Membres')
    class Meta:
        verbose_name = 'Association'
        verbose_name_plural = 'Associations'


class InterGroup(BaseGroup):
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                              verbose_name='Nom du président', related_name='intergroup')
    members = models.ManyToManyField(
        User, related_name='intergroups', blank=True, verbose_name='Membres')
    class Meta:
        verbose_name = 'Groupe international'
        verbose_name_plural = 'Groupes internationaux'


class Convention(TimeStampModel):
    label = models.CharField(
        max_length=150, verbose_name='Intitulé de la convention')
    file = models.FileField(verbose_name='Fichier joint')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Convention'
        verbose_name_plural = 'Conventions'


class Nomination(TimeStampModel):
    photo = CloudinaryField(resource_type='image', verbose_name='Photo')
    title = models.CharField(max_length=100, verbose_name='Texte')
    file = models.FileField(verbose_name='Fichier joint')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Nomination'
        verbose_name_plural = 'Nominations'


class Carnet(TimeStampModel):
    title = models.CharField(max_length=100, verbose_name='Texte')
    file = models.FileField(verbose_name='Fichier joint')
    
    def __str__(self):
        return self.title

class Club(TimeStampModel):
    photo = CloudinaryField(resource_type='image', verbose_name='Photo')
    content = models.TextField(verbose_name='Contenu')
    file = models.FileField(verbose_name='Fichier joint')

    def __str__(self):
        return self.content[:20]


class International(TimeStampModel):
    name = models.CharField(
        max_length=50, verbose_name='Nom du groupe international')
    link = models.URLField(verbose_name='Lien vers le groupe international')

    def __str__(self):
        return self.name

