from aden.utils import TimeStampModel
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Galery(TimeStampModel):
    name = models.CharField(max_length=250, verbose_name='Nom de l\'album')
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, verbose_name='Description')
    is_visible = models.BooleanField(
        default=True, verbose_name='Visible sur le site ?')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'


class GaleryImage(TimeStampModel):
    image = models.FileField(upload_to='gallery/')

    galery = models.ForeignKey(
        Galery, on_delete=models.CASCADE, verbose_name='Album', related_name='images')


class News(TimeStampModel):
    title = models.CharField(
        max_length=255, verbose_name='Titre de l\'actualité')
    slug = models.SlugField(blank=True)
    image = models.ImageField(
        verbose_name='Image de couverture', blank=True, upload_to='news/')
    content = models.TextField(verbose_name='Contenu de l\'article')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_visible = models.BooleanField(
        default=True, verbose_name='Visible sur le site ?')

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    class Meta:
        verbose_name = 'Actualité'
        verbose_name_plural = 'Actualités'


class Post(TimeStampModel):
    title = models.CharField(
        max_length=255, verbose_name='Titre de l\'article')
    slug = models.SlugField(blank=True)
    content = models.TextField(verbose_name='Contenu de l\'article')
    image = models.ImageField(
        verbose_name='Image de couverture', blank=True, upload_to='posts/')
    is_visible = models.BooleanField(
        default=True, verbose_name='Visible sur le site ?')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    class Meta:
        verbose_name = 'Article de blog'
        verbose_name_plural = 'Articles de blog'


class Document(TimeStampModel):
    title = models.CharField(
        max_length=100, verbose_name='Nom du document', blank=True)
    file = models.FileField(upload_to='documents/', verbose_name='Fichier')
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Propriétaire')

    def __str__(self):
        return self.title


class Event(TimeStampModel):
    title = models.CharField(max_length=100, verbose_name='Titre')
    slug = models.SlugField(blank=True)
    start_date = models.DateField(verbose_name='Date de debut')
    end_date = models.DateField(verbose_name='Date de fin')
    start_time = models.TimeField(verbose_name='Heure de debut')
    end_time = models.TimeField(verbose_name='Heure de Fin')
    description = models.TextField(verbose_name='Description')
    location = models.CharField(max_length=50, verbose_name='Lieu')
    location_city = models.CharField(
        max_length=50, verbose_name='Ville', default='Yaoundé')
    # event_type = models.CharField(
    #     max_length=10,
    #     choices=(('online', 'Online'), ('outline', 'Outline')),
    #     verbose_name = 'Type de L\'événement'
    # )
    expired = models.BooleanField(default=False, verbose_name='Expiré')
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='events')
    image_description = models.ImageField(
        upload_to='events/%Y/%m/%d', blank=True, null=True, verbose_name='Image de description')
    published = models.BooleanField(default=True, verbose_name='Publier')
    # organizer = models.ManyToManyField(User)
    registration = models.ManyToManyField(
        User, blank=True, related_name='register_events', verbose_name='Inscris')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'