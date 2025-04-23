from django import forms
from django.forms import ModelForm


from .models import Anime

class AnimeForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add to my anime list'}))

    class Meta:
        model = Anime
        fields = "__all__"


class RecomForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Anime similar to...'}))

    class Meta:
        model = Anime
        fields = "__all__"