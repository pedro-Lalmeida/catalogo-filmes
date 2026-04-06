from django.urls import path
from . import views

urlpatterns = [
    path('', views.Lista_filmes, name='lista_filmes'),
]