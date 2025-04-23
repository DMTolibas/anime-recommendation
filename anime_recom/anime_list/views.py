from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

#Import lib needed to work with 
import pandas as pd
import numpy as np

from .models import Anime, AnimeImport
from .forms import AnimeForm, RecomForm

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


def recommend(request):
    form = RecomForm()

    if request.method == 'POST':
        form = RecomForm(request.POST)

        if form.is_valid():
            form.save()
    

    context = {"RecomForm": form}
    
    return render(request, 'recom.html', context)


#Deal with AnimeImport 
def AnimeRecom(request):
    #The file cleaned_anime.csv is already cleaned data using google colab
    #create Matrix 
    #make a spreadsheet wehre the index is user id and the column is the name of the anime while the values is rating
    animedf = AnimeImport.objects.all()
    anime_recom = animedf.pivot_table(index='user_id',columns='name',values='rating')

    #create model
def find_corr(df, name):
    '''
    Get the correlation of one anime with the others

    Args
        df (DataFrame):  with user_id as rows and movie titles as column and ratings as values
        name (str): Name of the anime

    Return
        DataFrame with the correlation of the anime with all others
    '''

    similar_to_movie = df.corrwith(df[name])
    similar_to_movie = pd.DataFrame(similar_to_movie,columns=['Correlation'])
    similar_to_movie = similar_to_movie.sort_values(by = 'Correlation', ascending = False)
    return similar_to_movie

