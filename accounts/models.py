from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, AbstractUser
)
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils import timezone
from cloudinary.models import CloudinaryField
from aden.utils import TimeStampModel

from accounts.managers import UserManager
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
    filiere = models.CharField(max_length=50, verbose_name='Filière')
    promo = models.CharField(max_length=50, blank=True,
                             verbose_name='Promotion')
    gender = models.CharField(max_length=10, blank=True, choices=(
        ('male', 'Masculin'), ('female', 'Feminin')),verbose_name='Sexe')
    

    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)

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
