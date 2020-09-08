from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, AbstractUser
)
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils import timezone
from cloudinary.models import CloudinaryField
from aden.utils import TimeStampModel

from accounts.managers import UserManager, ProfileManager
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('Adresse email'),
        max_length=255,
        unique=True,
    )

    first_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Prenom')
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Nom')
    )
    date_joined = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name=_('Date d\'inscription')
    )
    last_login = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Dernière connexion')
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False, verbose_name=_('Membre'))
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        if self.is_admin:
            return 'Admin'
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    class Meta:
        verbose_name = _("Utilisateur")
        verbose_name_plural = _("Utilisateurs")


class Profile(TimeStampModel):
    photo = CloudinaryField(resource_type='image',
                            blank=True, verbose_name=_("Photo de profile"))
    birthday = models.DateField(
        blank=True, null=True, verbose_name=_("Date de naissance"))
    birth_location = models.CharField(
        max_length=100, blank=True, verbose_name=_('Lieu de naissance'))
    filiere = models.CharField(max_length=50, verbose_name='Filière', blank=True)
    promo = models.CharField(max_length=50, blank=True,
                             verbose_name='Promotion')
    gender = models.CharField(max_length=10, blank=True, choices=(
        ('male', 'Masculin'), ('female', 'Feminin')), verbose_name='Sexe')

    degree = models.CharField(
        max_length=100, blank=True, verbose_name='Intitulé du Diplome')
    in_ensai_year = models.CharField(
        max_length=10,
        help_text='Exemple: 2002',
        verbose_name='Année d\'entrée à l\'ENSAI', blank=True,null=True)
    out_ensai_year = models.CharField(
        max_length=10,
        help_text='Exemple: 2005',
        verbose_name='Année de sortie', blank=True, null=True)
    situation = models.CharField(
        max_length=100, blank=True, verbose_name='Situation actuelle')
    entreprise = models.CharField(
        max_length=100, blank=True, verbose_name='Nom de l\'entreprise qui vous emploi')
    poste = models.CharField(max_length=100, blank=True,
                             verbose_name='Poste occupé')
    postes = models.TextField(
        verbose_name='Les postes precédements occupés et les entreprises respectives', 
        help_text='Renseigner sous le format (post, entreprise) séparer par un point-virgule(;)',
        blank=True)
    phone = models.CharField(max_length=20, blank=True,
                             verbose_name='Numéro de téléphone')
    waiting = models.TextField(
        blank=True, verbose_name='Quelles sont vos attentes du groupe ALUMNI ENSAI?')

    contribution = models.TextField(
        blank=True, verbose_name='Que pouvez vous apporter comme contribution pour que vos attentes soient comblées?')

    region = models.CharField(max_length=50, blank=True, verbose_name='Région')

    portrait_visible = models.BooleanField(verbose_name='Portrait visible', default=True)

    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)

    objects = ProfileManager()

    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    def get_postes(self):
        return self.postes.split(';')

    def __str__(self):
        return str(self.user.email)


def post_save_user_create_profile(sender, instance, created, **kwargs):
    if created:
        try:
            instance = instance.profile
        except:
            Profile.objects.create(
                user=instance
            )


post_save.connect(post_save_user_create_profile, sender=User)
