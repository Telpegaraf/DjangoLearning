from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value

# Create your views here.
from .models import Movie


def show_all_movie(request):
    #movies = Movie.objects.order_by('-rating', 'name')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('string'),
        int_field=Value(15),
        new_rating=F('rating')+10,
    )
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies
    })


def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })