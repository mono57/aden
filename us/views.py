from django.shortcuts import render
from django.views.generic import ListView
from us.models import *
from django.views.generic import TemplateView
# Create your views here.


class ActionPlanListView(ListView):
    template_name = 'us/action_plans.html'
    model = ActionPlan
    context_object_name = 'actions'
    paginate_by = 9

    def get_queryset(self):
        lc = self.request.LANGUAGE_CODE
        qs = super().get_queryset()
        return qs.filter(language=lc)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["obj"] = ActionPlan.objects.filter(
        #     language=self.request.LANGUAGE_CODE).last()
        context['title'] = 'Missions et Plans d\'actions annuels'
        return context


class StatusTemplateView(TemplateView):
    template_name = 'aden.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["obj"] = Status.objects.filter(
            language=self.request.LANGUAGE_CODE).last()
        context['title'] = 'Statut juridique'
        context['motif'] = 'status'
        return context


class InternalRegulationTemplateView(TemplateView):
    template_name = 'aden.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["obj"] = InternalRegulation.objects.filter(
            language=self.request.LANGUAGE_CODE).last()
        context['title'] = 'Règlement interieur'
        context['motif'] = 'regulation'
        return context

class GeneralAssemblyListView(ListView):
    model = GeneralAssembly
    template_name = 'us/ga.html'
    context_object_name = 'gassemblies'