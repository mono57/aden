from django.contrib import admin
from carriere.models import *
# Register your models here.

class OfferModelAdmin(admin.ModelAdmin):
    list_display = ('label', 'entreprise')

admin.site.register(Offer, OfferModelAdmin)

class ResumerModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'filiere', 'promotion')

admin.site.register(Resume, ResumerModelAdmin)