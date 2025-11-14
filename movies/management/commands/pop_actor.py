from django.core.management.base import BaseCommand
from movies.models import Actor, Country
from datetime import date

class Command(BaseCommand):
    help = 'Popula a tabela Actor com exemplos famosos de atores e atrizes.'

    def handle(self, *args, **options):
        # Busca países já existentes para usar como foreign key
        country_codes = {
            'US': 'United States',
            'UK': 'United Kingdom',
            'CA': 'Canada',
            'AU': 'Australia',
            'BR': 'Brazil',
            'FR': 'France',
            'IT': 'Italy',
            'ES': 'Spain',
        }
        countries = {}
        for code in country_codes:
            try:
                countries[code] = Country.objects.get(code=code)
            except Country.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'País com código {code} não encontrado - Ignorando atores deste país.'))
                countries[code] = None

        # Lista de atores/atrizes para popular
        actors_data = [
            {'name': 'Matthew McConaughey', 'birth_date': date(1969,11,4), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':1, 'oscar_won':1},
            {'name': 'Anne Hathaway', 'birth_date': date(1982,11,12), 'gender': 'Female', 'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':2, 'oscar_won':1},
            {'name': 'Leonardo DiCaprio', 'birth_date': date(1974,11,11), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 3, 'oscar_nominations':7, 'oscar_won':1},
            {'name': 'Kate Winslet', 'birth_date': date(1975,10,5), 'gender': 'Female', 'nationality': countries['UK'], 'golden_globes_won': 4, 'oscar_nominations':7, 'oscar_won':1},
            {'name': 'Morgan Freeman', 'birth_date': date(1937,6,1), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':5, 'oscar_won':1},
            {'name': 'Tim Robbins', 'birth_date': date(1958,10,16), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':2, 'oscar_won':1},
            {'name': 'Keanu Reeves', 'birth_date': date(1964,9,2), 'gender': 'Male', 'nationality': countries['CA'], 'golden_globes_won': 0, 'oscar_nominations':0, 'oscar_won':0},
            {'name': 'Carrie-Anne Moss', 'birth_date': date(1967,8,21), 'gender': 'Female', 'nationality': countries['CA'], 'golden_globes_won': 0, 'oscar_nominations':0, 'oscar_won':0},
            {'name': 'Christian Bale', 'birth_date': date(1974,1,30), 'gender': 'Male', 'nationality': countries['UK'], 'golden_globes_won': 2, 'oscar_nominations':4, 'oscar_won':1},
            {'name': 'Heath Ledger', 'birth_date': date(1979,4,4), 'gender': 'Male', 'nationality': countries['AU'], 'golden_globes_won': 0, 'oscar_nominations':2, 'oscar_won':1},
            {'name': 'Tom Hanks', 'birth_date': date(1956,7,9), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 4, 'oscar_nominations':6, 'oscar_won':2},
            {'name': 'Uma Thurman', 'birth_date': date(1970,4,29), 'gender': 'Female', 'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':1, 'oscar_won':0},
            {'name': 'Scarlett Johansson', 'birth_date': date(1984,11,22), 'gender': 'Female', 'nationality': countries['US'], 'golden_globes_won': 0, 'oscar_nominations':2, 'oscar_won':0},
            {'name': 'Robert Downey Jr.', 'birth_date': date(1965,4,4), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 3, 'oscar_nominations':2, 'oscar_won':0},
            {'name': 'Meryl Streep', 'birth_date': date(1949,6,22), 'gender': 'Female', 'nationality': countries['US'], 'golden_globes_won': 8, 'oscar_nominations':21, 'oscar_won':3},
            {'name': 'Denzel Washington', 'birth_date': date(1954,12,28), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 2, 'oscar_nominations':9, 'oscar_won':2},
            {'name': 'Brad Pitt', 'birth_date': date(1963,12,18), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 2, 'oscar_nominations':4, 'oscar_won':1},
            {'name': 'Jennifer Lawrence', 'birth_date': date(1990,8,15), 'gender': 'Female', 'nationality': countries['US'], 'golden_globes_won': 3, 'oscar_nominations':4, 'oscar_won':1},
            {'name': 'Al Pacino', 'birth_date': date(1940,4,25), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 4, 'oscar_nominations':9, 'oscar_won':1},
            {'name': 'Marlon Brando', 'birth_date': date(1924,4,3), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 2, 'oscar_nominations':8, 'oscar_won':2},
            {'name': 'Robert De Niro', 'birth_date': date(1943,8,17), 'gender': 'Male', 'nationality': countries['US'], 'golden_globes_won': 2, 'oscar_nominations':7, 'oscar_won':2},
            {'name': 'Cate Blanchett', 'birth_date': date(1969,5,14), 'gender': 'Female', 'nationality': countries['AU'], 'golden_globes_won': 3, 'oscar_nominations':8, 'oscar_won':2},
            {'name': 'Natalie Portman', 'birth_date': date(1981,6,9), 'gender': 'Female', 'nationality': countries['US'], 'golden_globes_won': 1, 'oscar_nominations':3, 'oscar_won':1},
        ]

        created = 0
        skipped = 0
        for a in actors_data:
            if a['nationality'] is not None:
                obj, created_flag = Actor.objects.get_or_create(
                    name=a['name'],
                    defaults={
                        'birth_date': a['birth_date'],
                        'gender': a['gender'],
                        'nationality': a['nationality'],
                        'golden_globes_won': a['golden_globes_won'],
                        'oscar_nominations': a['oscar_nominations'],
                        'oscar_won': a['oscar_won'],
                    }
                )
                if created_flag:
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f'✓ Ator criado: {a["name"]}'))
                else:
                    skipped += 1
                    self.stdout.write(f'  Ator já existe: {a["name"]}')
            else:
                skipped += 1
                self.stdout.write(self.style.WARNING(f'✗ Pulado (país não existe): {a["name"]}'))
        
        self.stdout.write(self.style.SUCCESS(f'\n=== Resumo ==='))
        self.stdout.write(self.style.SUCCESS(f'Atores criados: {created}'))
        self.stdout.write(f'Atores já existentes ou pulados: {skipped}')
