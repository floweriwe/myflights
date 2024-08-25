from django.core.management.base import BaseCommand
import requests
from flights.models import Airport  # или другие модели
import yaml


class Command(BaseCommand):
    help = 'Fetch data from Aviasales API and store it in the database'

    def handle(self, *args, **kwargs):
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
            api_key = config['api_key_aviasales']

        # Запрос к API для получения аэропортов
        response = requests.get(f'http://api.travelpayouts.com/data/ru/airports.json?token={api_key}')
        airports = response.json()

        for airport in airports:
            iata_code = airport.get('code')
            name = airport.get('name')
            city_code = airport.get('city_code')
            country_code = airport.get('country_code')

            # Проверка наличия имени аэропорта
            if not name:
                print(f"Skipping airport {iata_code} due to missing name.")
                continue

            # Обновление или создание записи в базе данных
            Airport.objects.update_or_create(
                iata_code=iata_code,
                defaults={
                    'name': name,
                    'city': city_code,
                    'country': country_code,
                }
            )

        self.stdout.write(self.style.SUCCESS('Data from Aviasales API has been fetched and stored in the database'))
