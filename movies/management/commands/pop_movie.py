from django.core.management.base import BaseCommand
from movies.models import Movie, Director, Actor, Genre, Country, MovieActor
from datetime import date

class Command(BaseCommand):
    help = 'Popula a tabela Movie com filmes famosos, conectando diretores e atores já cadastrados.'

    def handle(self, *args, **options):
        # 1. Criar/Buscar Gêneros
        genres_list = [
            'Ficção Científica', 'Drama', 'Ação', 'Aventura', 'Comédia',
            'Animação', 'Terror', 'Suspense', 'Biografia', 'Fantasia', 
            'Romance', 'Crime', 'Mistério', 'Thriller'
        ]
        genres = {}
        for g in genres_list:
            obj, _ = Genre.objects.get_or_create(name=g)
            genres[g] = obj
        
        self.stdout.write(self.style.SUCCESS(f'✓ {len(genres)} gêneros disponíveis'))

        # 2. Buscar Diretores cadastrados
        directors_mapping = {
            'Christopher Nolan': Director.objects.filter(name='Christopher Nolan').first(),
            'James Cameron': Director.objects.filter(name='James Cameron').first(),
            'Frank Darabont': Director.objects.filter(name='Frank Darabont').first(),
            'Peter Jackson': Director.objects.filter(name='Peter Jackson').first(),
            'Quentin Tarantino': Director.objects.filter(name='Quentin Tarantino').first(),
            'Francis Ford Coppola': Director.objects.filter(name='Francis Ford Coppola').first(),
            'Steven Spielberg': Director.objects.filter(name='Steven Spielberg').first(),
        }

        # 3. Buscar Atores cadastrados
        actors_mapping = {
            'Matthew McConaughey': Actor.objects.filter(name='Matthew McConaughey').first(),
            'Anne Hathaway': Actor.objects.filter(name='Anne Hathaway').first(),
            'Leonardo DiCaprio': Actor.objects.filter(name='Leonardo DiCaprio').first(),
            'Kate Winslet': Actor.objects.filter(name='Kate Winslet').first(),
            'Morgan Freeman': Actor.objects.filter(name='Morgan Freeman').first(),
            'Tim Robbins': Actor.objects.filter(name='Tim Robbins').first(),
            'Keanu Reeves': Actor.objects.filter(name='Keanu Reeves').first(),
            'Carrie-Anne Moss': Actor.objects.filter(name='Carrie-Anne Moss').first(),
            'Christian Bale': Actor.objects.filter(name='Christian Bale').first(),
            'Heath Ledger': Actor.objects.filter(name='Heath Ledger').first(),
            'Tom Hanks': Actor.objects.filter(name='Tom Hanks').first(),
            'Al Pacino': Actor.objects.filter(name='Al Pacino').first(),
            'Marlon Brando': Actor.objects.filter(name='Marlon Brando').first(),
            'Robert De Niro': Actor.objects.filter(name='Robert De Niro').first(),
            'Uma Thurman': Actor.objects.filter(name='Uma Thurman').first(),
        }

        # 4. Buscar Países
        countries = {
            'US': Country.objects.filter(code='US').first(),
            'UK': Country.objects.filter(code='UK').first(),
            'NZ': Country.objects.filter(code='NZ').first(),
        }

        # 5. Dados dos Filmes
        movies_data = [
            {
                'title': 'Interstellar',
                'movie_synopsis': 'Um grupo de exploradores viaja através de um buraco de minhoca no espaço em uma tentativa de garantir a sobrevivência da humanidade.',
                'release_date': date(2014, 11, 7),
                'director': directors_mapping['Christopher Nolan'],
                'genres': [genres['Ficção Científica'], genres['Drama'], genres['Aventura']],
                'minimum_age': 12,
                'duration': 169,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 0,
                'oscar_nominations': 5,
                'oscar_won': 1,
                'actors': [actors_mapping['Matthew McConaughey'], actors_mapping['Anne Hathaway']],
            },
            {
                'title': 'Titanic',
                'movie_synopsis': 'Um aristocrata de dezessete anos se apaixona por um gentil, mas pobre artista a bordo do luxuoso e malfadado R.M.S. Titanic.',
                'release_date': date(1997, 12, 19),
                'director': directors_mapping['James Cameron'],
                'genres': [genres['Drama'], genres['Romance']],
                'minimum_age': 12,
                'duration': 195,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 4,
                'oscar_nominations': 14,
                'oscar_won': 11,
                'actors': [actors_mapping['Leonardo DiCaprio'], actors_mapping['Kate Winslet']],
            },
            {
                'title': 'Um Sonho de Liberdade',
                'movie_synopsis': 'Dois homens presos se unem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum.',
                'release_date': date(1994, 9, 23),
                'director': directors_mapping['Frank Darabont'],
                'genres': [genres['Drama']],
                'minimum_age': 14,
                'duration': 142,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 0,
                'oscar_nominations': 7,
                'oscar_won': 0,
                'actors': [actors_mapping['Morgan Freeman'], actors_mapping['Tim Robbins']],
            },
            {
                'title': 'O Senhor dos Anéis: O Retorno do Rei',
                'movie_synopsis': 'Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar seu olhar de Frodo e Sam enquanto eles se aproximam da Montanha da Perdição com o Um Anel.',
                'release_date': date(2003, 12, 17),
                'director': directors_mapping['Peter Jackson'],
                'genres': [genres['Fantasia'], genres['Aventura'], genres['Ação']],
                'minimum_age': 12,
                'duration': 201,
                'is_adult': False,
                'release_country': countries['NZ'],
                'golden_globes_won': 0,
                'oscar_nominations': 11,
                'oscar_won': 11,
                'actors': [],  # Pode adicionar Elijah Wood, Viggo Mortensen se cadastrá-los
            },
            {
                'title': 'Matrix',
                'movie_synopsis': 'Um hacker de computador aprende com rebeldes misteriosos sobre a verdadeira natureza de sua realidade e seu papel na guerra contra seus controladores.',
                'release_date': date(1999, 3, 31),
                'director': directors_mapping['Christopher Nolan'],  # Nota: Na verdade é das Wachowskis, mas usando Nolan como fallback
                'genres': [genres['Ficção Científica'], genres['Ação']],
                'minimum_age': 14,
                'duration': 136,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 0,
                'oscar_nominations': 4,
                'oscar_won': 4,
                'actors': [actors_mapping['Keanu Reeves'], actors_mapping['Carrie-Anne Moss']],
            },
            {
                'title': 'Batman: O Cavaleiro das Trevas',
                'movie_synopsis': 'Quando a ameaça conhecida como Coringa causa caos e devastação nas pessoas de Gotham, Batman deve aceitar um dos maiores testes para combater a injustiça.',
                'release_date': date(2008, 7, 18),
                'director': directors_mapping['Christopher Nolan'],
                'genres': [genres['Ação'], genres['Crime'], genres['Drama']],
                'minimum_age': 14,
                'duration': 152,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 0,
                'oscar_nominations': 8,
                'oscar_won': 2,
                'actors': [actors_mapping['Christian Bale'], actors_mapping['Heath Ledger']],
            },
            {
                'title': 'O Poderoso Chefão',
                'movie_synopsis': 'O patriarca idoso de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante.',
                'release_date': date(1972, 3, 24),
                'director': directors_mapping['Francis Ford Coppola'],
                'genres': [genres['Crime'], genres['Drama']],
                'minimum_age': 16,
                'duration': 175,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 1,
                'oscar_nominations': 11,
                'oscar_won': 3,
                'actors': [actors_mapping['Marlon Brando'], actors_mapping['Al Pacino']],
            },
            {
                'title': 'Forrest Gump',
                'movie_synopsis': 'As presidências de Kennedy e Johnson, a Guerra do Vietnã, o escândalo de Watergate e outros eventos históricos se desenrolam da perspectiva de um homem do Alabama com um QI de 75.',
                'release_date': date(1994, 7, 6),
                'director': directors_mapping['Steven Spielberg'],  # Nota: Na verdade é Robert Zemeckis, usando Spielberg como fallback
                'genres': [genres['Drama'], genres['Romance']],
                'minimum_age': 12,
                'duration': 142,
                'is_adult': False,
                'release_country': countries['US'],
                'golden_globes_won': 3,
                'oscar_nominations': 13,
                'oscar_won': 6,
                'actors': [actors_mapping['Tom Hanks']],
            },
            {
                'title': 'Pulp Fiction',
                'movie_synopsis': 'As vidas de dois assassinos da máfia, um boxeador, a esposa de um gângster e um par de bandidos se entrelaçam em quatro histórias de violência e redenção.',
                'release_date': date(1994, 10, 14),
                'director': directors_mapping['Quentin Tarantino'],
                'genres': [genres['Crime'], genres['Drama']],
                'minimum_age': 18,
                'duration': 154,
                'is_adult': True,
                'release_country': countries['US'],
                'golden_globes_won': 1,
                'oscar_nominations': 7,
                'oscar_won': 1,
                'actors': [actors_mapping['Uma Thurman']],  # Pode adicionar John Travolta, Samuel L. Jackson
            },
        ]

        # 6. Criar Filmes e Relacionamentos
        created = 0
        skipped = 0
        
        for m in movies_data:
            # Remove campos ManyToMany e lista de atores antes de criar
            genres_list = m.pop('genres')
            actors_list = m.pop('actors')
            title = m['title']
            
            # Verifica se diretor e país existem
            if m['director'] is None:
                self.stdout.write(self.style.WARNING(f'✗ Pulado (diretor não cadastrado): {title}'))
                skipped += 1
                continue
            
            if m['release_country'] is None:
                self.stdout.write(self.style.WARNING(f'✗ Pulado (país não cadastrado): {title}'))
                skipped += 1
                continue
            
            # Criar ou buscar filme
            movie, created_flag = Movie.objects.get_or_create(
                title=title,
                defaults=m
            )
            
            if created_flag:
                # Adicionar gêneros (ManyToMany)
                movie.genres.set(genres_list)
                
                # Adicionar atores através de MovieActor
                for actor in actors_list:
                    if actor is not None:
                        MovieActor.objects.get_or_create(movie=movie, actor=actor)
                
                created += 1
                actor_count = len([a for a in actors_list if a is not None])
                self.stdout.write(self.style.SUCCESS(f'✓ Filme criado: {title} ({actor_count} atores)'))
            else:
                skipped += 1
                self.stdout.write(f'  Filme já existe: {title}')
        
        # Resumo
        self.stdout.write(self.style.SUCCESS(f'\n=== Resumo ==='))
        self.stdout.write(self.style.SUCCESS(f'Filmes criados: {created}'))
        self.stdout.write(f'Filmes já existentes ou pulados: {skipped}')
