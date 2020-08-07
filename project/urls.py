from django.urls import path

from project.views import ProjectCreateView, ProjectUpdateView

app_name = 'project'

urlpatterns = [
    path('form/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/edit/', ProjectUpdateView.as_view(), name='project-update'),
]
