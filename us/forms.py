from django import forms
from us.models import About, Contact
from tinymce.widgets import TinyMCE


class AboutModelForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30})
        }



class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3})
        }