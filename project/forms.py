from django import forms

from project.models import Project


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Project.objects.filter(name=name)

        if qs.exists():
            raise forms.ValidationError(
                'Ce projet existe déjà! Merci de soumettre un autre')
        return name