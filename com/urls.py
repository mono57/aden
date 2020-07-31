from django.urls import path
from com.views import *

app_name = 'com'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<str:slug>/detail/', PostDetailView.as_view(),name='post-detail'),
    path('news/', NewsListView.as_view(), name='news-list'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('galeries/', GaleryListView.as_view(), name='galery-list'),
]
