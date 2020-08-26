from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Les utilisateurs doivent avoir une adresse email'))

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
