from django import forms
from .models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        labels = {'name': ''}
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'input form-control rounded-pill', 'placeholder': 'Check what\'s the weather like for your city...'})}
