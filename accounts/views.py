from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from accounts.forms import ProfileModelForm

class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    form_class = ProfileModelForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('account_profile')
    success_message = 'Votre profile a été bien mis à jour'

    def get_initial(self):
        initial = super().get_initial()
        kwargs = self.request.user.profile.__dict__
        return {**initial, **kwargs}

    def form_valid(self, form):
        data = form.cleaned_data
        profile = self.request.user.profile
        profile.photo = data.get('photo')
        profile.birthbay = data.get('birthday')
        profile.birthbay_location = data.get('birthbay_location')
        profile.promotion = data.get('promotion')
        profile.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)