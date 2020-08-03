from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from accounts.views import ProfileUpdateView
from aden.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('aden/', TemplateView.as_view(template_name='aden.html'), name='aden'),
    path('ensai/', TemplateView.as_view(template_name='ensai.html'), name='ensai'),
    path('network/', NetworkTemplateView.as_view(template_name='network.html'), name='network'),
    path('adhesion/conditions/', TemplateView.as_view(template_name='conditions.html'), name='conditions'),
    path('permissions/', TemplateView.as_view(template_name='not_allowed.html'), name='not_allowed'),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/profile/', ProfileUpdateView.as_view(), name='account_profile'),
    path('com/', include('com.urls', namespace='com')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
