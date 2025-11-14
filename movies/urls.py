from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, DirectorViewSet, ActorViewSet, GenreViewSet, CountryViewSet, MovieActorViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'movie-actors', MovieActorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]