from django.shortcuts import render
from .models import Movie


def index_page(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def player_page(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movies/player.html', {'movie': movie})
