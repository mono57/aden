from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from us.models import *
from us.forms import ContactModelForm
from django.urls import reverse_lazy
# Create your views here.


class StrategicComityTempateView(TemplateView):
    template_name = 'us/comity.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_grade'] = StrategicComity.objects.filter(
            grade=1).first()
        context['second_grades'] = StrategicComity.objects.filter(grade=2)
        context['third_grades'] = StrategicComity.objects.filter(grade=3)
        return context



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


class CoordTemplateView(TemplateView):
    template_name = 'us/coords.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coord'] = Coord.objects.last()
        context['title'] = 'Coordonnées'
        return context

class ContactCreateView(SuccessMessageMixin, CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = reverse_lazy('aden:contact')
    success_message = 'Votre message a été envoyé avec succès !'