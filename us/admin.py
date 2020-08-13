from django.contrib import admin

# Register your models here.
from us.models import *
from us.forms import AboutModelForm
class StrategicComityModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title',)

admin.site.register(StrategicComity, StrategicComityModelAdmin)

class StatusModelAdmin(admin.ModelAdmin):
    list_display = ('created_at',)

admin.site.register(Status, StatusModelAdmin)


class ActionPlanModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')

admin.site.register(ActionPlan, ActionPlanModelAdmin)

class InternalRegulationModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')

admin.site.register(InternalRegulation, InternalRegulationModelAdmin)


class SocialNetworkModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'accessibility')

admin.site.register(SocialNetwork, SocialNetworkModelAdmin)


class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('language',)
    form = AboutModelForm

admin.site.register(About, AboutModelAdmin)