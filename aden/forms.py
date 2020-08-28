from django import forms
from django.utils.translation import gettext_lazy as _
class ContactForm(forms.Form):
    name = forms.CharField(label=_('Votre nom'))
    email = forms.EmailField(label=_('Votre adresse email'))
    phone = forms.CharField(label=_('Votre numero de téléphone'))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))