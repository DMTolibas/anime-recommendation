from django.shortcuts import render, redirect, get_object_or_404
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

def deleteanime(request, pk):
    anime = get_object_or_404(Anime, id=pk)      # get the object that the user is req, but if not found, show 404 error
    # anime = Anime.objects.get(id=pk) // you can also try this one
    if request.method == 'POST':
        anime.delete()

        return redirect('home')

    context = {'anime': anime}
    return render(request, 'delete-anime.html', context) 


def updateanime(request, pk):
    anime = get_object_or_404(Anime, id=pk) #get the obj.

    form = AnimeForm(instance=anime)   #This code set the data that we request as the place holder//instance = whatever data we get/request

    if request.method == 'POST':

        form = AnimeForm(request.POST, instance=anime) #change the current data into new data

        if form.is_valid():

            form.save()
        
            return redirect('home')
        
    context = {'AnimeForm': form}

    return render(request, 'update-anime.html', context)
