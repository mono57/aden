from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from com.models import (Post, News, Event, Document, Galery, GaleryImage, RevueInterface,
                        PostCategory, StrategicComity as ComStrategicComity)
from aden.decorators import aden_member_required
from us.models import StrategicComity


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class PostListView(ListView):
    template_name = 'com/post-list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 6

@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class GaleryListView(ListView):
    model = GaleryImage
    template_name = 'com/galery-list.html'
    context_object_name = 'galeries'
    # queryset = Galery.objects.all()
    paginate_by = 9


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
    paginate_by = 6


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
    paginate_by = 6



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


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class GeleryDetailView(DetailView):
    template_name = 'com/galery-detail.html'
    model = GaleryImage
    context_object_name = 'photos'
    paginate_by = 9

    def get_querset(self):
        pk_galery = self.kwargs.get('pk')
        galery = get_object_or_404(Galery, pk=pk_galery)
        qs = super().get_queryset()
        return qs.filter(galery=galery)


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class RevueInterfaceListView(ListView):
    template_name = 'com/interface.html'
    model = RevueInterface
    context_object_name = 'interfaces'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Revue Interface'
        return context