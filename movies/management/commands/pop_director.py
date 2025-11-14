from django.core.management.base import BaseCommand
from movies.models import Director, Country
from datetime import date

class Command(BaseCommand):
    help = 'Popula a tabela de Diretores com dados famosos (sem inserir países)'

    def handle(self, *args, **options):
        country_codes = {
            'UK': 'United Kingdom',
            'CA': 'Canada',
            'FR': 'France',
            'US': 'United States',
            'NZ': 'New Zealand',
        }
        countries = {}
        for code in country_codes:
            try:
                countries[code] = Country.objects.get(code=code)
            except Country.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'País código {code} não encontrado. Diretores desse país NÃO serão criados.'))
                countries[code] = None

        # Dados de diretores
        directors_data = [
            {'name': 'Christopher Nolan', 'birth_date': date(1970,7,30), 'gender':'Male', 'nationality': countries['UK']},
            {'name': 'James Cameron', 'birth_date': date(1954,8,16), 'gender':'Male', 'nationality': countries['CA']},
            {'name': 'Frank Darabont', 'birth_date': date(1959,1,28), 'gender':'Male', 'nationality': countries['FR']},
            {'name': 'Francis Ford Coppola', 'birth_date': date(1939,4,7), 'gender':'Male', 'nationality': countries['US']},
            {'name': 'Quentin Tarantino', 'birth_date': date(1963,3,27), 'gender':'Male', 'nationality': countries['US']},
            {'name': 'Steven Spielberg', 'birth_date': date(1946,12,18), 'gender':'Male', 'nationality': countries['US']},
            {'name': 'Peter Jackson', 'birth_date': date(1961,10,31), 'gender':'Male', 'nationality': countries['NZ']},
        ]

        created = 0
        for d in directors_data:
            if d['nationality'] is not None:
                obj, created_flag = Director.objects.get_or_create(
                    name=d['name'],
                    defaults={
                        'birth_date': d['birth_date'],
                        'gender': d['gender'],
                        'nationality': d['nationality'],
                    }
                )
                if created_flag:
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f'Diretor criado: {d["name"]}'))
                else:
                    self.stdout.write(f'Diretor já existe: {d["name"]}')
            else:
                self.stdout.write(
                    self.style.WARNING(f'Pulei {d["name"]}: país não existe no banco.')
                )
        self.stdout.write(self.style.SUCCESS(f'Total de diretores criados: {created}'))
