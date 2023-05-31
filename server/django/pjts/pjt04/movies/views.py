from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request,'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    objects = list(movie.genres.all())
    genres = []
    for genre in objects:
        genres.append(genre.name)
    context = {
        'movie': movie,
        'genres': genres,
    }
    return render(request,'movies/detail.html', context)


@require_safe
def recommended(request):
    movies = Movie.objects.order_by('?')[:10]
    context = {
        'movies': movies,
    }
    return render(request,'movies/recommended.html', context)
