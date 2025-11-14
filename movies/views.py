from django.shortcuts import render
from .models import Movie, Director, Actor, Genre, Country, MovieActor
from .serializers import MovieActorSerializer, MovieSerializer, DirectorSerializer, ActorSerializer, GenreSerializer, CountrySerializer
from rest_framework import viewsets, filters

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