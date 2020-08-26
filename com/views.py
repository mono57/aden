from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from com.models import Post, News, Event, Document, Galery, PostCategory, StrategicComity as ComStrategicComity
from aden.decorators import aden_member_required
from us.models import StrategicComity


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class PostListView(ListView):
    template_name = 'com/post-list.html'
    model = Post
    context_object_name = 'posts'


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class GaleryListView(ListView):
    model = Galery
    template_name = 'com/galery-list.html'
    context_object_name = 'galeries'


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class PostDetailView(DetailView):
    template_name = 'com/post-detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recent_posts'] = self.model.objects.exclude(
            slug=self.kwargs.get('slug'))[:3]
        return ctx


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class NewsListView(ListView):
    template_name = 'com/news-list.html'
    model = News
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PostCategory.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class NewsDetailView(DetailView):
    model = News
    template_name = 'com/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recent_posts'] = self.model.objects.exclude(
            slug=self.kwargs.get('slug'))[:3]
        return ctx


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class EventListView(ListView):
    template_name = 'com/event-list.html'
    model = Event
    context_object_name = 'events'


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class EventDetailView(DetailView):
    template_name = 'com/event-detail.html'
    context_object_name = 'event'
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.exclude(pk=self.get_object().pk)
        return context


class StrategicComityTempateView(TemplateView):
    template_name = 'us/comity.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_grade'] = StrategicComity.objects.filter(
            grade=1).first()
        context['second_grades'] = StrategicComity.objects.filter(grade=2)
        context['third_grades'] = StrategicComity.objects.filter(grade=3)
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class ComStrategicComityListView(ListView):
    template_name = 'com/strategic_comity-list.html'
    model = ComStrategicComity
    context_object_name = 'comities'


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class ComStrategicComityDetailView(DetailView):
    template_name = 'com/strategic_comity-detail.html'
    model = ComStrategicComity
    context_object_name = 'comity'