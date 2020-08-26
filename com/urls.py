from django.urls import path
from com.views import *

app_name = 'com'

urlpatterns = [
    path(
        'posts/', 
        PostListView.as_view(), 
        name='post-list'),
    path(
        'posts/<str:slug>/detail/', 
        PostDetailView.as_view(),
        name='post-detail'),
    path(
        'news/', 
        NewsListView.as_view(), 
        name='news-list'),
    path(
        'news/<str:slug>/detail/', 
        NewsDetailView.as_view(), 
        name='news-detail'),
    path(
        'events/', 
        EventListView.as_view(), 
        name='event-list'),
    path(
        'events/<int:pk>/details/', 
        EventDetailView.as_view(), 
        name='event-detail'),
    path(
        'galeries/', 
        GaleryListView.as_view(), 
        name='galery-list'),
    path(
        'comities/', 
        ComStrategicComityListView.as_view(), 
        name='comities'),

    path(
        'comities/<int:pk>/detail/', 
        ComStrategicComityDetailView.as_view(), 
        name='comities-detail'),

    path(
        'strategic/comity/', 
        StrategicComityTempateView.as_view(), 
        name='comity'),
]
