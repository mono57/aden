from aden.utils import TimeStampModel
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField

User = get_user_model()

visible_on_site = _('Visible sur le site ?')
cover_image = _('Image de couverture')

class Galery(TimeStampModel):
    name = models.CharField(max_length=250, verbose_name=_('Nom de l\'album'))
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, verbose_name='Description')
    is_visible = models.BooleanField(
        default=True, verbose_name=visible_on_site)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()

    class Meta:
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')


class GaleryImage(TimeStampModel):
    image = CloudinaryField('image')

    galery = models.ForeignKey(
        Galery, on_delete=models.CASCADE, verbose_name=_('Album'), related_name='images')


class PostCategory(TimeStampModel):
    name = models.CharField(max_length=100, verbose_name=_('Nom'))
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()


class News(TimeStampModel):
    title = models.CharField(
        max_length=255, verbose_name=_('Titre de l\'actualité'))
    slug = models.SlugField(blank=True)
    image = CloudinaryField(resource_type='image',
                                   verbose_name=cover_image, blank=True)
    content = models.TextField(verbose_name=_('Contenu de l\'article'))
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(
        PostCategory, blank=True, related_name='news')
    is_visible = models.BooleanField(
        default=True, verbose_name=visible_on_site)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def get_absolute_url(self):
        return reverse('com:news-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Actualité'
        verbose_name_plural = 'Actualités'


class Post(TimeStampModel):
    title = models.CharField(
        max_length=255, verbose_name=_('Titre de l\'article'))
    slug = models.SlugField(blank=True)
    content = models.TextField(verbose_name=_('Contenu de l\'article'))
    category = models.ManyToManyField(
        PostCategory, related_name='posts', blank=True, verbose_name=_('Categories d\'article'))
    image = CloudinaryField(resource_type='image',
                                   verbose_name=cover_image, blank=True)
    is_visible = models.BooleanField(
        default=True, verbose_name=visible_on_site)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def get_absolute_url(self):
        return reverse("com:post-detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = _('Article de blog')
        verbose_name_plural = _('Articles de blog')


class Document(TimeStampModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Nom du document'), blank=True)
    file = models.FileField(upload_to='documents/', verbose_name=_('Fichier'))
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Propriétaire'))

    def __str__(self):
        return self.title


class Event(TimeStampModel):
    title = models.CharField(max_length=100, verbose_name=_('Titre'))
    slug = models.SlugField(blank=True)
    start_date = models.DateField(verbose_name=_('Date de debut'))
    end_date = models.DateField(verbose_name=_('Date de fin'))
    start_time = models.TimeField(verbose_name=_('Heure de debut'))
    end_time = models.TimeField(verbose_name=_('Heure de Fin'))
    description = models.TextField(verbose_name='Description')
    location = models.CharField(max_length=50, verbose_name=_('Lieu'))
    location_city = models.CharField(
        max_length=50, verbose_name=_('Ville'), default='Yaoundé')
    # event_type = models.CharField(
    #     max_length=10,
    #     choices=(('online', 'Online'), ('outline', 'Outline')),
    #     verbose_name = 'Type de L\'événement'
    # )
    expired = models.BooleanField(default=False, verbose_name=_('Expiré'))
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='events')
    image = CloudinaryField(
        resource_type='image', blank=True, null=True, verbose_name=cover_image)
    published = models.BooleanField(default=True, verbose_name=_('Publier'))
    # organizer = models.ManyToManyField(User)
    registration = models.ManyToManyField(
        User, blank=True, related_name='register_events', verbose_name=_('Inscris'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('com:event-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'


class StrategicComity(TimeStampModel):
    object = models.CharField(max_length=100, verbose_name='Objet')
    content = models.TextField(verbose_name='Message')

    def get_absolute_url(self):
        return reverse('com:comities-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _('Communiqué Comité Stratégique')
        verbose_name_plural = _('Communiqué(s) Comité Stratégique')


class Faq(TimeStampModel):
    question = models.CharField(max_length=200, verbose_name='Question')
    response = models.TextField(verbose_name='Reponse')

    def __str__(self):
        return self.question