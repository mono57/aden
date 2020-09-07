from django.contrib import admin
from project.models import *
# Register your models here.

class ProjectModelAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'title', 'filiere',)
    list_display = ('name', 'filiere', 'owner', )
    list_filter = ('school_out_date', 'created_at')


admin.site.register(Project, ProjectModelAdmin)
admin.site.register(InstitutionalProject)
admin.site.register(IndustrialProject)