from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class PromotionsTemplateView(TemplateView):
    template_name = 'network.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Promotions'
        return context


class InterGroupTemplateView(TemplateView):
    template_name = 'network.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Groupes internationaux'
        return context


class ConventionsTemplateView(TemplateView):
    template_name = 'network.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Conventions avec les grandes écoles'
        return context


class AnnuaireTemplateView(TemplateView):
    template_name = 'network.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Annuaire'
        return context
    

class NominationsTemplateView(TemplateView):
    template_name = 'network.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nominations'
        return context


class CarnetTemplateView(TemplateView):
    template_name = 'network.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Carnet'
        return context


class ClubsTemplateView(TemplateView):
    template_name = 'network.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Clubs'
        return context


class InternationalTemplateView(TemplateView):
    template_name = 'network.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'International'
        return context
    

class NewsTemplateView(TemplateView):
    template_name = 'network.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'News'
        return context


class PortraitAlumniTemplateView(TemplateView):
    template_name = 'network.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Portrait des alumnis'
        return context