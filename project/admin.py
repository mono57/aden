from django.contrib import admin
from project.models import *
# Register your models here.

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('owner', 'filiere', 'name')


admin.site.register(Project, ProjectModelAdmin)
admin.site.register(InstitutionalProject)
admin.site.register(IndustrialProject)