from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('delete-anime/<str:pk>', views.deleteanime, name="delete-anime"), #the str: pk get the id of the obj and send it to the f(x) in view
    path('update-anime/<str:pk>', views.updateanime, name="update-anime"), #the str: pk get the id of the obj and send it to the views.updateanime

    path('recommendation', views.AnimeRecom, name="recommendation"),
]