from django.core.management.base import BaseCommand
from movies.models import Country, Genre, Actor, Director, Movie, MovieActor
from datetime import date

class Command(BaseCommand):
    help = 'Popula o banco com dados de países, gêneros, atores, diretores, filmes e elencos.'

    def handle(self, *args, **options):
        # 1. Países
        countries_data = [
            {'name': 'Estados Unidos', 'code': 'US'},
            {'name': 'Reino Unido', 'code': 'UK'},
            {'name': 'Canadá', 'code': 'CA'},
            {'name': 'França', 'code': 'FR'},
            {'name': 'Alemanha', 'code': 'DE'},
            {'name': 'Brasil', 'code': 'BR'},
            {'name': 'Nova Zelândia', 'code': 'NZ'},
            {'name': 'Austrália', 'code': 'AU'},
            {'name': 'Itália', 'code': 'IT'},
            {'name': 'Japão', 'code': 'JP'},
        ]
        countries = {}
        for c in countries_data:
            obj, _ = Country.objects.get_or_create(name=c['name'], code=c['code'])
            countries[c['code']] = obj
        
        # 2. Gêneros
        genres_list = ['Ficção Científica', 'Drama', 'Ação', 'Aventura', 'Comédia', 'Animação', 'Terror', 'Suspense', 'Biografia', 'Fantasia']
        genres = {}
        for g in genres_list:
            obj, _ = Genre.objects.get_or_create(name=g)
            genres[g] = obj

        # 3. Atores (exemplos famosos)
        actors_data = [
            {'name': 'Matthew McConaughey',   'birth_date': date(1969,11,4),   'gender': 'Male',   'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':1, 'oscar_won':1},
            {'name': 'Anne Hathaway',         'birth_date': date(1982,11,12),  'gender': 'Female', 'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':2, 'oscar_won':1},
            {'name': 'Leonardo DiCaprio',     'birth_date': date(1974,11,11),  'gender': 'Male',   'nationality': countries['US'], 'golden_globes_won': 3, 'oscar_nominations':7, 'oscar_won':1},
            {'name': 'Kate Winslet',          'birth_date': date(1975,10,5),   'gender': 'Female', 'nationality': countries['UK'], 'golden_globes_won': 4, 'oscar_nominations':7, 'oscar_won':1},
            {'name': 'Morgan Freeman',        'birth_date': date(1937,6,1),    'gender': 'Male',   'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':5, 'oscar_won':1},
            {'name': 'Tim Robbins',           'birth_date': date(1958,10,16),  'gender': 'Male',   'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':2, 'oscar_won':1},
            {'name': 'Keanu Reeves',          'birth_date': date(1964,9,2),    'gender': 'Male',   'nationality': countries['CA'], 'golden_globes_won': 0, 'oscar_nominations':0, 'oscar_won':0},
            {'name': 'Laurence Fishburne',    'birth_date': date(1961,7,30),   'gender': 'Male',   'nationality': countries['US'], 'golden_globes_won': 0, 'oscar_nominations':1, 'oscar_won':0},
            {'name': 'Carrie-Anne Moss',      'birth_date': date(1967,8,21),   'gender': 'Female', 'nationality': countries['CA'], 'golden_globes_won': 0, 'oscar_nominations':0, 'oscar_won':0},
            {'name': 'Christian Bale',        'birth_date': date(1974,1,30),   'gender': 'Male',   'nationality': countries['UK'], 'golden_globes_won': 2, 'oscar_nominations':4, 'oscar_won':1},
            {'name': 'Heath Ledger',          'birth_date': date(1979,4,4),    'gender': 'Male',   'nationality': countries['AU'], 'golden_globes_won': 0, 'oscar_nominations':2, 'oscar_won':1},
            {'name': 'Marlon Brando',         'birth_date': date(1924,4,3),    'gender': 'Male',   'nationality': countries['US'], 'golden_globes_won': 2, 'oscar_nominations':8, 'oscar_won':2},
            {'name': 'Al Pacino',             'birth_date': date(1940,4,25),   'gender': 'Male',   'nationality': countries['US'], 'golden_globes_won': 4, 'oscar_nominations':9, 'oscar_won':1},
            {'name': 'Tom Hanks',             'birth_date': date(1956,7,9),    'gender': 'Male',   'nationality': countries['US'], 'golden_globes_won': 4, 'oscar_nominations':6, 'oscar_won':2},
            {'name': 'Robert De Niro',        'birth_date': date(1943,8,17),   'gender': 'Male',   'nationality': countries['US'], 'golden_globes_won': 2, 'oscar_nominations':7, 'oscar_won':2},
            {'name': 'Uma Thurman',           'birth_date': date(1970,4,29),   'gender': 'Female', 'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':1, 'oscar_won':0},
        ]
        actors_objs = {}
        for a in actors_data:
            obj, _ = Actor.objects.get_or_create(name=a['name'], defaults=a)
            actors_objs[a['name']] = obj
        
        # 4. Diretores
        directors_data = [
            {'name': 'Christopher Nolan', 'birth_date': date(1970,7,30), 'gender':'Male', 'nationality': countries['UK']},
            {'name': 'James Cameron',     'birth_date': date(1954,8,16), 'gender':'Male', 'nationality': countries['CA']},
            {'name': 'Frank Darabont',    'birth_date': date(1959,1,28), 'gender':'Male', 'nationality': countries['FR']},
            {'name': 'Francis Ford Coppola', 'birth_date': date(1939,4,7), 'gender':'Male', 'nationality': countries['US']},
            {'name': 'Quentin Tarantino', 'birth_date': date(1963,3,27), 'gender':'Male', 'nationality': countries['US']},
            {'name': 'Steven Spielberg',  'birth_date': date(1946,12,18), 'gender':'Male', 'nationality': countries['US']},
            {'name': 'Peter Jackson',     'birth_date': date(1961,10,31), 'gender':'Male', 'nationality': countries['NZ']},
        ]
        directors_objs = {}
        for d in directors_data:
            obj, _ = Director.objects.get_or_create(name=d['name'], defaults=d)
            directors_objs[d['name']] = obj

        # 5. Filmes
        movies_data = [
            {
                'title': 'Interstellar',
                'movie_synopsis': 'Num futuro distópico, a Terra está acabando. Um grupo viaja por um buraco de minhoca em busca de novo lar para a humanidade.',
                'release_date': date(2014, 11, 7),
                'director': directors_objs['Christopher Nolan'],
                'genres': [genres['Ficção Científica'], genres['Drama'], genres['Aventura']],
                'minimum_age': 12,
                'duration': 169,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 0,
                'oscar_nominations': 5,
                'oscar_won': 1,
                'actors': [actors_objs['Matthew McConaughey'], actors_objs['Anne Hathaway']]
            },
            {
                'title': 'Titanic',
                'movie_synopsis': 'Amor proibido a bordo do navio Titanic, que colide com um iceberg.',
                'release_date': date(1997, 12, 19),
                'director': directors_objs['James Cameron'],
                'genres': [genres['Drama'], genres['Romance']] if 'Romance' in genres else [genres['Drama']],
                'minimum_age': 12,
                'duration': 195,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 4,
                'oscar_nominations': 14,
                'oscar_won': 11,
                'actors': [actors_objs['Leonardo DiCaprio'], actors_objs['Kate Winslet']]
            },
            {
                'title': 'O Senhor dos Anéis: O Retorno do Rei',
                'movie_synopsis': 'Final épico da saga de Frodo e Sam para destruir o Um Anel.',
                'release_date': date(2003, 12, 17),
                'director': directors_objs['Peter Jackson'],
                'genres': [genres['Fantasia'], genres['Aventura'], genres['Ação']],
                'minimum_age': 12,
                'duration': 201,
                'is_adult': False,
                'release_country': countries['NZ'],
                'golden_globes_won': 0,
                'oscar_nominations': 11,
                'oscar_won': 11,
                'actors': []
            },
            {
                'title': 'Matrix',
                'movie_synopsis': 'Um programador descobre que o mundo real é uma simulação controlada por máquinas.',
                'release_date': date(1999, 3, 31),
                'director': directors_objs['Lana Wachowski'] if 'Lana Wachowski' in directors_objs else directors_objs['Christopher Nolan'],
                'genres': [genres['Ficção Científica'], genres['Ação']],
                'minimum_age': 14,
                'duration': 136,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 0,
                'oscar_nominations': 4,
                'oscar_won': 4,
                'actors': [actors_objs['Keanu Reeves'], actors_objs['Laurence Fishburne'], actors_objs['Carrie-Anne Moss']]
            },
            {
                'title': 'Forrest Gump',
                'movie_synopsis': 'Forrest navega momentos históricos dos EUA com inocência e amor por Jenny.',
                'release_date': date(1994, 7, 6),
                'director': directors_objs['Robert Zemeckis'] if 'Robert Zemeckis' in directors_objs else directors_objs['Frank Darabont'],
                'genres': [genres['Drama'], genres['Comédia']],
                'minimum_age': 12,
                'duration': 142,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 3,
                'oscar_nominations': 13,
                'oscar_won': 6,
                'actors': [actors_objs['Tom Hanks']]
            },
            {
                'title': 'Clube da Luta',
                'movie_synopsis': 'Narrador insone conhece Tyler Durden e juntos fundam um clube secreto de lutas.',
                'release_date': date(1999, 10, 15),
                'director': directors_objs['David Fincher'] if 'David Fincher' in directors_objs else directors_objs['Frank Darabont'],
                'genres': [genres['Drama'], genres['Ação'], genres['Suspense']],
                'minimum_age': 18,
                'duration': 139,
                'is_adult': True,
                'release_country': countries['US'],
                'golden_globes_won': 0,
                'oscar_nominations': 1,
                'oscar_won': 0,
                'actors': []
            },
        ]
        movies_objs = {}
        for m in movies_data:
            # Remove 'genres'/'actors' do dict principal
            genres_list = m.pop('genres')
            actors_list = m.pop('actors')
            title = m['title']
            movie, created = Movie.objects.get_or_create(title=title, defaults=m)
            if created:
                # M2M precisa ser feito depois do save
                movie.genres.set(genres_list)
            movies_objs[title] = movie
            # Elenco (MovieActor)
            for actor in actors_list:
                MovieActor.objects.get_or_create(movie=movie, actor=actor)
        
        self.stdout.write(self.style.SUCCESS('Tabelas populadas com sucesso!'))
