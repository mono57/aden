from django.shortcuts import render
from django.views.generic import ListView
from us.models import *
from django.views.generic import TemplateView
# Create your views here.


class ActionPlanTemplateView(TemplateView):
    template_name = 'aden.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["obj"] = ActionPlan.objects.filter(
            language=self.request.LANGUAGE_CODE).last()
        context['title'] = 'Plan d\'action'
        return context


class StatusTemplateView(TemplateView):
    template_name = 'aden.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["obj"] = Status.objects.filter(
            language=self.request.LANGUAGE_CODE).last()
        context['title'] = 'Statut juridique'
        return context


class InternalRegulationTemplateView(TemplateView):
    template_name = 'aden.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["obj"] = InternalRegulation.objects.filter(
            language=self.request.LANGUAGE_CODE).last()
        context['title'] = 'Règlement interieur'
        return context
