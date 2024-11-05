from django import forms
from django.forms import TextInput

from companies.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

        widgets = {
            'name_movie': TextInput(attrs={'placeholder': 'name_movie', 'class': 'form-class'}),
            'anul_lansarii': TextInput(attrs={'placeholder': 'anul_lansarii', 'class': 'form-class'}),
            'nominalizari': TextInput(attrs={'placeholder': 'nominalizari', 'class': 'form-class'}),
            'premii': TextInput(attrs={'placeholder': 'premii', 'class': 'form-class'}),
            'rating': TextInput(attrs={'placeholder': 'rating', 'class': 'form-class'}),
        }

    class CompanyForm(forms.ModelForm):
        class Meta:
            model = Company
            fields = ['name_movie', 'anul_lansarii', 'nominalizari', 'premii', 'rating']
