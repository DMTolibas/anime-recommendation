from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist


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


#The corr funt
def find_corr(AnimeImport, name):    
#Get the correlation of one anime with the others
    #The file cleaned_anime.csv is already cleaned data using google colab

    queryset = AnimeImport.objects.all().values('user_id', 'name', 'rating') #get all the data from AnimeImport. this is query set only

    AnimeImportdf = pd.DataFrame.from_records(queryset) #convert query set to dataframe

    #create Matrix 
    #make a spreadsheet wehre the index is user id and the column is the name of the anime while the values is rating
    # Create pivot table: users as rows, anime names as columns, ratings as values
    pivot_df = AnimeImportdf.pivot_table(index='user_id', columns='name', values='rating')

    correlation_series = pivot_df.corrwith(pivot_df[name])  #the correlation function

    # Convert to DataFrame and sort
    result = pd.DataFrame(correlation_series, columns=['Correlation'])
    result = result.sort_values(by='Correlation', ascending=False)
    return result



#Deal with AnimeImport 
def AnimeRecom(request):
    '''
    TODO:
        -initiate form
        -get data from form
        -search that anime within the AnimeImport database; give the info if exist otherwise redirect
        -set it as input data to the model
        -show the recommend anime according to the model
    '''

    form = RecomForm() # removing it remove the placeholder since this initiate the form obj

    #get the object's id in placeholder
    #selected_anime = get_object_or_404(AnimeImport, id=pk) #get the obj. (the whole row including the id, name, genre and other info) // Search also if anime is on the data
    #The code below act simialr to get_object_or_404 but the response is custom. Redirect to home and custom msg

    if request.method == 'POST':
        form = RecomForm(request.POST) #“Create a RecomForm object and fill it with the user’s submitted data.”

        #validate data
        if form.is_valid():
            name = form.cleaned_data['name'] # this just not clean the data but retrieve the data that the user input. E.g: User: Input = Another;  this variable is the Another 

            try:
                anime_queryset = AnimeImport.objects.filter(name=name) # use filter instead of get

                if anime_queryset.exists():
                    result = find_corr(AnimeImport, name)
                    result_html = result.to_html()

                    context = {
                        "RecomForm": form,
                        "anime_info": result_html 
                    }
                    
                    return render(request, 'recom.html', context)

            except ObjectDoesNotExist:
                print("Anime does not Exist")
                return redirect('home')
    
        else:
            print("Form is not Valid")
            print(form)

    #Why there is 2 context var becoz the one below is when we need to pass the empty form when we first access the web page while the context above is when we get info from user.
    context = {"RecomForm": form}

    return render(request, 'recom.html', context)


   

