from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Anime
from .forms import AnimeForm

# Create your views here.
def index(request):

    form = AnimeForm()

    anime = Anime.objects.all()

    if request.method == 'POST':
        form = AnimeForm(request.POST)

        if form.is_valid():
            form.save()
    

    context = {"animes": anime, "AnimeForm": form}
    
    return render(request, 'home.html', context)


def recommend(request):
    return render(request,'recom.html')