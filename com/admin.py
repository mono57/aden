from django.contrib import admin
from com.models import *
from com.forms import *
# Register your models here.

class GaleryModelAdmin(admin.ModelAdmin):
    list_display = ('name', )
    form = GaleryModelForm

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)
        for file in request.FILES.getlist('files'):
            GaleryImage.objects.create(
                galery = obj,
                image = file
            )
            # print(file)

    
admin.site.register(Galery, GaleryModelAdmin)


class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_visible')
    list_filter = ('created_at', 'is_visible')
    search_fields = ('title', 'creator', 'content')
    form = NewsModelForm
    # exclude = ('creator', 'slug')  

    def save_model(self,request, obj, form, change):
        obj.creator = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(News, NewsModelAdmin)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_visible')
    list_filter = ('created_at', 'is_visible')
    search_fields = ('title', 'creator', 'content')  
    exclude = ('creator', 'slug')  
    form = PostModelForm

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Post, PostModelAdmin)

class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('created_at', )
    search_fields = ('title',)
    form = DocumentModelForm

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Document, DocumentModelAdmin)

class EventModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'start_time', 'location', 'published')
    list_filter = ('start_date', 'end_date', 'start_time', 'end_time', 'published')
    search_fields = ('title', 'description', 'location', 'location_city', )
    form = EventModelForm

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Event, EventModelAdmin)

class PostCategoryModelAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    def has_module_permission(self, request):
        return False

admin.site.register(PostCategory, PostCategoryModelAdmin)

class StrategicComityModelAdmin(admin.ModelAdmin):
    list_display = ('object', )
    form = StrategicComityModelForm

admin.site.register(StrategicComity, StrategicComityModelAdmin)

class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('question', )
    form = FaqModelForm

admin.site.register(Faq, FaqModelAdmin)