from django.urls import path
from network.views import *

app_name = 'network'

urlpatterns = [
    path(
        'promotions/',
        AssociationListView.as_view(),
        name='promotions'
    ),
    path(
        'inter_group/',
        InterGroupListView.as_view(),
        name='inter_group'
    ),
    path(
        'annuaire/',
        AnnuaireListView.as_view(),
        name='annuaire'
    ),
    path(
        'conventions/',
        ConventionsListView.as_view(),name='conventions'
    ),
    path(
        'nominations/',
        NominationsListView.as_view(),
        name='nominations'
    ),
    path(
        'carnet/',
        CarnetListView.as_view(),
        name='carnet'
    ),
    path(
        'clubs/',
        ClubsListView.as_view(),
        name='clubs'
    ),
    path(
        'international/',
        InternationalListView.as_view(),
        name='international'
    ),
    path(
        'news/',
        NewsListView.as_view(),
        name='news'
    ),
    path(
        'portrait/',
        PortraitAlumniListView.as_view(),
        name='portrait'
    ),
    path(
        'portrait/<int:pk>/detail/',
        PortraitAlumniDetailView.as_view(), 
        name='portrait-detail')
]
