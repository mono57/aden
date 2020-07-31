from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)

from com.models import Post, News, Event, Document, Galery


class PostListView(ListView):
    template_name = 'com/post-list.html'
    model = Post
    context_object_name = 'posts'

class GaleryListView(ListView):
    model = Galery
    template_name = 'com/galery-list.html'
    context_object_name = 'galeries'


class PostDetailView(DetailView):
    template_name = 'com/post-detail.html'
    model = Post
    context_object_name = 'post'
    

class NewsListView(ListView):
    template_name = 'com/news-list.html'
    model = News
    context_object_name = 'news'


class EventListView(ListView):
    template_name = 'com/event-list.html'
    model = Event
    context_object_name = 'events'