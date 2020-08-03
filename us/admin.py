from django.contrib import admin

# Register your models here.
from us.models import StrategicComity

class StrategicComityModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title',)


admin.site.register(StrategicComity, StrategicComityModelAdmin)