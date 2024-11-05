from django import forms
from django.forms import TextInput

from .models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['movie', 'type', 'projection', 'price', 'time']

        widgets = {
            'movie': TextInput(attrs={'class': 'form-control', 'placeholder': 'movie'}),
            'type': TextInput(attrs={'class': 'form-control', 'placeholder': 'type'}),
            'projection': TextInput(attrs={'class': 'form-control', 'placeholder': 'projection'}),
            'price': TextInput(attrs={'class': 'form-control', 'placeholder': 'price'}),
            'time': TextInput(attrs={'class': 'form-control', 'placeholder': 'time'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        movie_value = self.cleaned_data.get('movie')
        if self.pk:
            if Location.objects.filter(movie=movie_value).exclude(id=self.pk).exists():
                self._errors['movie'] = self.error_class(['Filmul exista deja'])
        if Location.objects.filter(movie=movie_value).exists():
            self._errors['movie'] = self.error_class(['Filmul exista deja'])
        return self.cleaned_data
