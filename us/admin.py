from django.contrib import admin
import cloudinary
# Register your models here.
from us.models import *
from us.forms import AboutModelForm
class StrategicComityModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title',)

admin.site.register(StrategicComity, StrategicComityModelAdmin)

class StatusModelAdmin(admin.ModelAdmin):
    list_display = ('language', 'created_at',)

    # def save_model(self, request, obj, form, change):
    #     upload_info = cloudinary.uploader.upload(form.cleaned_data.get('file'))
    #     # res = cloudinary.api.resource(upload_info.get('original_filename'), pages = True)
    #     print(upload_info)
        

admin.site.register(Status, StatusModelAdmin)


class ActionPlanModelAdmin(admin.ModelAdmin):
    list_display = ('language','created_at', 'updated_at')

admin.site.register(ActionPlan, ActionPlanModelAdmin)

class InternalRegulationModelAdmin(admin.ModelAdmin):
    list_display = ('language', 'created_at', 'updated_at')

admin.site.register(InternalRegulation, InternalRegulationModelAdmin)


class SocialNetworkModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'accessibility')

admin.site.register(SocialNetwork, SocialNetworkModelAdmin)


class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('language',)
    form = AboutModelForm

admin.site.register(About, AboutModelAdmin)