from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('recommendation', views.recommend, name="recommendation"),
]