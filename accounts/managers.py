from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Q


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(
                _('Les utilisateurs doivent avoir une adresse email'))

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):

        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(
            email,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.admin = True
        user.is_member = True
        user.save(using=self._db)
        return user


class ProfileManager(models.Manager):
    def get_visible_portraits(self):
        qs = self.get_queryset()
        print(qs)
        return qs.filter(Q(user__is_member=True) &
                         Q(portrait_visible=True))
