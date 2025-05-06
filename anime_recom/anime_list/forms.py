from django import forms
from django.forms import ModelForm


from .models import Anime, AnimeImport

class AnimeForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add to my anime list'}))

    class Meta:
        model = Anime
        fields = "__all__"


#searching on database
class RecomForm(forms.Form):
    name = forms.CharField(
        label= 'name',
        max_length=500,
        widget=forms.TextInput(attrs={'placeholder': 'Anime similar to...'}))

'''
Searching/filtering data	---- forms.Form
Creating/editing database row ---- forms.ModelForm

In RecomForm class we did not use model = AnimeImport because we do not need to save data to AnimeImport database but we just need to search through it.
'''