from .models import Movie, Director, Actor, Genre, Country, MovieActor
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class MovieActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieActor
        fields = '__all__'