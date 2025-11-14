from django.contrib import admin
from django.urls import path, include
from movies.views import home_view, movie_detail_view, search_movie_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movies/', include('movies.urls')),
    path('', home_view, name='home'),
    path('movies/<int:pk>/', movie_detail_view, name='movie_detail'),
    path('search/', search_movie_view, name='movie-search'),
]
