from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class FindJob(TemplateView):
    template_name = 'carriere/carriere.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Trouver un poste'
        return context
        

class OfferJob(TemplateView):
    template_name = 'carriere/carriere.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Proposer une offre'
        return context
        
class ResumeSubmit(TemplateView):
    template_name = 'carriere/carriere.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Déposer son CV'
        return context
        
class EnsaiRecruter(TemplateView):
    template_name = 'carriere/carriere.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Recruter un ENSAI'
        return context
        