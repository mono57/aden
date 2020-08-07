from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from project.forms import ProjectModelForm
from project.models import Project
# Create your views here.


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


class ProjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'project/project-edit.html'
    form_class = ProjectModelForm
    model = Project
    # success_url = reverse_lazy('project:project-update')
    success_message = 'Votre projet a été bien mis à jour'

    def get_success_url(self):
        return reverse('project:project-update', kwargs={'pk': self.get_object().pk})