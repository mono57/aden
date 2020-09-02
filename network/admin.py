from django.contrib import admin

from network.models import *


class NetworkNewsModelAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(NetworkNews, NetworkNewsModelAdmin)