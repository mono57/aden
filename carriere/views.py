from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.
from carriere.forms import OfferModelForm, ResumeModelForm
from carriere.models import Offer, Resume
from aden.decorators import aden_member_required


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class FindJobListView(ListView):
    template_name = 'carriere/offer-list.html'
    model = Offer
    context_object_name = 'offers'
    paginate_by = 6

    def get(self,request, *args, **kwargs):
        self.query = request.GET.get('query', '')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.get_offers_by(self.query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Trouver un poste'
        context['query'] = self.query
        return context
        

@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class OfferJobCreateView(SuccessMessageMixin, CreateView):
    template_name = 'carriere/job_offer-form.html'
    form_class = OfferModelForm
    success_url = reverse_lazy('carriere:offer')
    success_message = 'Votre proposition a été soumise avec succès !'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Proposer une offre'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')    
class ResumeCreateView(SuccessMessageMixin, CreateView):
    template_name = 'carriere/resume-form.html'
    form_class = ResumeModelForm
    success_url = reverse_lazy('carriere:resume')
    success_message = "Votre CV a été déposer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Déposer son CV'
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')  
class EnsaiRecruterListView(ListView):
    template_name = 'carriere/resume-list.html'
    model = Resume
    context_object_name = 'resumes'
    paginate_by = 6

    def get(self,request, *args, **kwargs):
        self.query = request.GET.get('query', '')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.get_resumes_by(self.query)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Recruter un ENSAI'
        context['query'] = self.query
        return context
        
