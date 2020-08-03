from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView
from aden.forms import ContactForm
from aden.decorators import aden_member_required

class ContactFormView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Votre message a été bien envoyé, merci de patienter !'

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class NetworkTemplateView(TemplateView):
    template_name = 'network.html'
    