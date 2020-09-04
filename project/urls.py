from django.urls import path
from django.views.generic import TemplateView
from project.views import *

app_name = 'project'

urlpatterns = [
    path('form/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/edit/', ProjectUpdateView.as_view(), name='project-update'),
    path(
        'industrial/',
        IndustrialProjectListView.as_view(),
        name='industrial'),
    path(
        'institutionnal/',
        InstitutionallProjectListView.as_view(),
        name='institutional'
    ),
]
