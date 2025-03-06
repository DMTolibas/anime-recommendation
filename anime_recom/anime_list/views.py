from django.shortcuts import render
from django.http import HttpResponse
from .models import Anime


# Create your views here.
def index(request):

    anime = Anime.objects.all()

    context = {"animes": anime}
    return render(request, 'home.html', context)