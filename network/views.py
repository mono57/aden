from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.views import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.db.models import Q

from aden.decorators import aden_member_required
from network.models import *
from accounts.models import Profile

User = get_user_model()


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class AssociationListView(ListView):
    template_name = 'network/association.html'
    model = Association
    context_object_name = 'associations'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Association de promotions'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class InterGroupListView(ListView):
    template_name = 'network/intergroup.html'
    model = InterGroup
    context_object_name = 'intergroups'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Groupes internationaux'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class ConventionsListView(ListView):
    template_name = 'network/conventions.html'
    model = Convention
    context_object_name = 'conventions'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Conventions avec les grandes écoles'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class AnnuaireListView(ListView):
    model = User
    context_object_name = 'members'
    template_name = 'network/annuaire.html'
    paginate_by = 8

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_member=True).exclude(email='admin@ensai-alumni.cm')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Annuaire'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class NominationsListView(ListView):
    template_name = 'network/nomination.html'
    model = Nomination
    context_object_name = 'nominations'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nominations'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class CarnetListView(ListView):
    template_name = 'network/carnet.html'
    model = Carnet
    context_object_name = 'carnets'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Carnet'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class ClubsListView(ListView):
    template_name = 'network/club.html'
    model = Club
    context_object_name = 'clubs'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Clubs'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class InternationalListView(ListView):
    template_name = 'network/international.html'
    model = International
    context_object_name = 'internationals'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'International'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class NewsListView(ListView):
    model = NetworkNews
    context_object_name = 'news'
    template_name = 'network/news-list.html'
    paginate_by = 6

    # def get_queryset(self):
    #     return NetworkNews.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'News'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class PortraitAlumniListView(ListView):
    template_name = 'network/portrait-list.html'
    model = Profile
    context_object_name = 'portraits'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        print(qs)
        return self.model.objects.get_visible_portraits()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Portrait des alumnis'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class PortraitAlumniDetailView(DetailView):
    model = Profile
    context_object_name = 'portrait'
    template_name = 'network/portrait-detail.html'

    def get_object(self):
        return self.model.objects.get_visible_portraits().get(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Portrait - {}'.format(
            self.get_object().user.get_full_name())
        return context
