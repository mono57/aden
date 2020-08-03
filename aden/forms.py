from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Votre nom')
    email = forms.EmailField(label='Votre adresse email')
    phone = forms.CharField(label='Votre numero de téléphone')
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))