from  django import forms
from tinymce.widgets import TinyMCE

from com.models import (
    News,
    Galery,
    Post, 
    Document,
    Event
)

class GaleryModelForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Galery
        fields = ('name', 'description')

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')

    #     qs = Galery.objects.filter(name=name)

    #     if qs.exists():
    #         error_msg = 'Un album avec le même nom existe'
    #         raise forms.ValidationError(error_msg)

    #     return name



class NewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('creator', 'slug')
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30})
        }
    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     qs = News.objects.filter(title = title)

    #     if qs.exists():
    #         raise forms.ValidationError('Une actualité de même nom existe')

    #     return title


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('creator', 'slug')
        widgets = {
            'content': TinyMCE(attrs={'rows': 30, 'cols': 80})
        }
    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     qs = Post.objects.filter(title = title)

    #     if qs.exists():
    #         raise forms.ValidationError('Un article de même nom existe')

    #     return title


class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('creator', 'slug', 'registration', 'expired')

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     qs = Event.objects.get(title=title)
    #     if qs.exists():
    #         raise forms.ValidationError('Un évenement existe avec le même nom')
    #     return title

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')

        if start_date > end_date:
            raise forms.ValidationError('La date de fin ne peut être anterieure à celle du debut')
        return end_date

class DocumentModelForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ('creator', 'title')
