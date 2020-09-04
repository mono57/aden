from django.contrib import admin

from network.models import *


class NetworkNewsModelAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(NetworkNews, NetworkNewsModelAdmin)


admin.site.register(Association)
admin.site.register(Convention)
# admin.site.register(AdhesionCondition)
admin.site.register(RevueInterface)
admin.site.register(Nomination)
admin.site.register(Carnet)
admin.site.register(International)