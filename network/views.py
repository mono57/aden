from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.views import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.db.models import Q

from aden.decorators import aden_member_required
from network.models import NetworkNews


User = get_user_model()


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class PromotionsTemplateView(TemplateView):
    template_name = 'network.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Promotions'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class InterGroupTemplateView(TemplateView):
    template_name = 'network.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Groupes internationaux'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class ConventionsTemplateView(TemplateView):
    template_name = 'network.html'

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
        return qs.filter(Q(is_member=True) & Q(email='admin@ensai-alumni.cm'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Annuaire'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class NominationsTemplateView(TemplateView):
    template_name = 'network.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nominations'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class CarnetTemplateView(TemplateView):
    template_name = 'network.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Carnet'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class ClubsTemplateView(TemplateView):
    template_name = 'network.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Clubs'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class InternationalTemplateView(TemplateView):
    template_name = 'network.html'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'News'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class PortraitAlumniListView(ListView):
    template_name = 'network/portrait-list.html'
    model = User
    context_object_name = 'portraits'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_member=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Portrait des alumnis'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class PortraitAlumniDetailView(DetailView):
    model = User
    context_object_name = 'portrait'
    template_name = 'network/portrait-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Portrait - {}'.format(
            self.get_object().get_full_name())
        return context
