from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, FormView
from django.urls import reverse_lazy
from accounts.forms import ProfileModelForm

class ProfileUpdateView(LoginRequiredMixin, FormView):
    form_class = ProfileModelForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('account_profile')
    success_message = 'Votre profile a été bien mis à jour'