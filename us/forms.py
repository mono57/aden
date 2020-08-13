from django import forms
from us.models import About
from tinymce.widgets import TinyMCE


class AboutModelForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30})
        }
