from django import forms
from .models import Location, News, Brews


class LocationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Location
        fields = ['description']


class NewsForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = News
        fields = ['description']


class BrewForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Brews
        fields = ['description']

