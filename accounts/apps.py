from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AccountConfig(AppConfig):
    name = 'accounts'
    verbose_name = _('Membres, Profils et Visiteurs')
