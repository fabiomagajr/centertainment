from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor, Genre, Country, MovieActor
from .serializers import MovieActorSerializer, MovieSerializer, DirectorSerializer, ActorSerializer, GenreSerializer, CountrySerializer
from rest_framework import viewsets, filters
from django.db.models import Count, Q

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'director__name', 'genres__name']
    ordering_fields = ['release_date', 'title']

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'nationality__name']
    ordering_fields = ['name', 'birth_date']
    
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'nationality__name']
    ordering_fields = ['name', 'birth_date', 'golden_globes_won', 'oscar_nominations', 'oscar_won']
    
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class MovieActorViewSet(viewsets.ModelViewSet):
    queryset = MovieActor.objects.all()
    serializer_class = MovieActorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie__title', 'actor__name']
    ordering_fields = ['movie__title', 'actor__name']

def home_view(request):
    # Obter estatísticas para a homepage
    context = {
        'pagina': 'home',
        'total_movies': Movie.objects.count(),
        'total_directors': Director.objects.count(),
        'total_actors': Actor.objects.count(),
        'total_genres': Genre.objects.count(),
        # Filmes recentes (últimos 6)
        'recent_movies': Movie.objects.all().order_by('-id')[:6],
    }
    return render(request, 'home.html', context)

def movie_detail_view(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    context = {
        'pagina': 'movie_detail',
        'movie': movie,
    }
    return render(request, 'movie_detail.html', context)


def search_movie_view(request):
    query = request.GET.get('q', '')
    
    print(f"Query recebida: '{query}'")
    
    results = Movie.objects.none()
    
    if query:
        results = Movie.objects.filter(
            Q(title__icontains=query) |
            Q(director__name__icontains=query) |
            Q(movieactor__actor__name__icontains=query) |  
            Q(genres__name__icontains=query)
        ).distinct()
        
        print(f"Resultados encontrados: {results.count()}")
    
    context = {
        'query': query,
        'results': results,
        'pagina': 'search'
    }
    return render(request, 'search_results.html', context)
