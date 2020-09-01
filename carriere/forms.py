from django import forms
from carriere.models import *

class OfferModelForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'

        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'profil': forms.Textarea(attrs={'rows': 3})
        }
    
class ResumeModelForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        