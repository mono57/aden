from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.views import login_required
from django.contrib.messages.views import SuccessMessageMixin
from project.forms import ProjectModelForm
from project.models import Project, IndustrialProject, InstitutionalProject

from aden.decorators import aden_member_required
# Create your views here.


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class ProjectCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project/project-edit.html'
    form_class = ProjectModelForm
    # success_url = reverse_lazy('project:project-update')
    success_message = 'Votre project a été soumis avec succès'

    def form_valid(self, form, **kwargs):
        obj = form.save()
        self.kwargs['pk'] = obj.pk
        return super().form_valid(form, **kwargs)

    def get_success_url(self):
        return reverse('project:project-update', kwargs={'pk': self.kwargs.get('pk')})


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class ProjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'project/project-edit.html'
    form_class = ProjectModelForm
    model = Project
    # success_url = reverse_lazy('project:project-update')
    success_message = 'Votre projet a été bien mis à jour'

    def get_success_url(self):
        return reverse('project:project-update', kwargs={'pk': self.get_object().pk})



@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class IndustrialProjectListView(ListView):
    template_name = 'project/industrial.html'
    model = IndustrialProject
    context_object_name = 'projects'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Projets industriels'
        return context

    
@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class InstitutionallProjectListView(ListView):
    template_name = 'project/institutional.html'
    model = IndustrialProject
    context_object_name = 'projects'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Projets institutionels'
        return context