from django.core.management.base import BaseCommand
from movies.models import Genre

class Command(BaseCommand):
    help = 'Populate the movies_genre table with known movie genres'

    def handle(self, *args, **kwargs):
        genres = [
            'Action',
            'Comedy',
            'Drama',
            'Fantasy',
            'Horror',
            'Romance',
            'Sci-Fi',
            'Thriller',
            'Documentary',
            'Animation',
            'Adventure',
            'Mystery',
            'Biography',
            'Family',
            'History',
            'Musical',
            'War',
            'Western',
        ]

        for genre_name in genres:
            Genre.objects.get_or_create(name=genre_name)

        self.stdout.write(self.style.SUCCESS('Successfully populated movies_genre table'))