from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from accounts.models import Profile

User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_('Mot de passe'), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_('Mot de passe confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', )

    def clean_passsword2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                _('Les mots de passe ne correspondent pas'))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        return self.initial['password']

class CustomDateInput(forms.DateInput):
    input_type = 'date'

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','portrait_visible' )
        widgets = {
            'birthday': CustomDateInput(),
            'postes': forms.Textarea(attrs={'rows':3}),
            'waiting': forms.Textarea(attrs={'rows':3}),
            'contribution': forms.Textarea(attrs={'rows':3}),
        }

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name')