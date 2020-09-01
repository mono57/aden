from django.urls import path
from carriere.views import *

app_name = 'carriere'

urlpatterns = [
    path(
        'find/',
        FindJob.as_view(),
        name='find'
    ),
    path(
        'offer/',
        OfferJob.as_view(),
        name='offer'
    ),
    path(
        'resume/',
        ResumeSubmit.as_view(),
        name='resume'
    ),
    path(
        'recruter/',
        EnsaiRecruter.as_view(),
        name='recruter'
    )
]
