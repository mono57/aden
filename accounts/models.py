from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, AbstractUser
)
from django.db.models.signals import post_save
from django.utils import timezone
from cloudinary.models import CloudinaryField
from aden.utils import TimeStampModel

from accounts.managers import UserManager
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Adresse email',
        max_length=255,
        unique=True,
    )

    first_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Prenom'
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Nom'
    )
    date_joined = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name='Date d\'inscription'
    )
    last_login = models.DateTimeField(
        default=timezone.now,
        verbose_name='Dernière connexion'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False, verbose_name='Membre')
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
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"



class Profile(TimeStampModel):
    photo = CloudinaryField(resource_type='image', blank=True, verbose_name="Photo de profile")
    birthday = models.DateField(blank=True, null=True, verbose_name="Date de naissance")
    birth_location = models.CharField(
        max_length=100, blank=True, verbose_name='Lieu de naissance')
    promo = models.CharField(max_length=50, blank=True,
                             verbose_name='Promotion')

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
                user = instance
            )

post_save.connect(post_save_user_create_profile, sender=User)