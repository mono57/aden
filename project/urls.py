from django.urls import path
from django.views.generic import TemplateView
from project.views import ProjectCreateView, ProjectUpdateView

app_name = 'project'

urlpatterns = [
    path('form/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/edit/', ProjectUpdateView.as_view(), name='project-update'),
    path(
        'industrial/',
        TemplateView.as_view(template_name='project/industrial.html'),
        name='industrial'),
    path(
        'institutionnal/',
        TemplateView.as_view(template_name='project/institutional.html'),
        name='institutional'
    ),
]
