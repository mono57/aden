from django.urls import path
from network.views import *

app_name = 'network'

urlpatterns = [
    path(
        'promotions/',
        PromotionsTemplateView.as_view(),
        name='promotions'
    ),
    path(
        'inter_group/',
        InterGroupTemplateView.as_view(),
        name='inter_group'
    ),
    path(
        'annuaire/',
        AnnuaireTemplateView.as_view(),
        name='annuaire'
    ),
    path(
        'conventions/',
        ConventionsTemplateView.as_view(),name='conventions'
    ),
    path(
        'nomintations/',
        NominationsTemplateView.as_view(),
        name='nominations'
    ),
    path(
        'carnet/',
        CarnetTemplateView.as_view(),
        name='carnet'
    ),
    path(
        'clubs/',
        ClubsTemplateView.as_view(),
        name='clubs'
    ),
    path(
        'international/',
        InternationalTemplateView.as_view(),
        name='international'
    ),
    path(
        'news/',
        NewsTemplateView.as_view(),
        name='news'
    ),
    path(
        'portrait/',
        PortraitAlumniTemplateView.as_view(),
        name='portrait'
    )
]
