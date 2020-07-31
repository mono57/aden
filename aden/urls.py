from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from accounts.views import ProfileUpdateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', ProfileUpdateView.as_view(), name='account_profile'),
    path('com/', include('com.urls', namespace='com')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
