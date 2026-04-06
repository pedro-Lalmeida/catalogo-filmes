from django.shortcuts import render
from core.models import Filme

# Create your views here.

def Lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista.html', {'filmes': filmes})