from django.urls import path
from carriere.views import *

app_name = 'carriere'

urlpatterns = [
    path(
        'find/',
        FindJobListView.as_view(),
        name='find'
    ),
    path(
        'offer/',
        OfferJobCreateView.as_view(),
        name='offer'
    ),
    path(
        'resume/',
        ResumeCreateView.as_view(),
        name='resume'
    ),
    path(
        'recruter/',
        EnsaiRecruterListView.as_view(),
        name='recruter'
    )
]
