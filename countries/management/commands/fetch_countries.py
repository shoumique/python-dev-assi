import requests
from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    help = 'Fetches data from the restcountries.com API and stores it in the database'

    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)
        countries = response.json()
        
        for country_data in countries:
            # Extract relevant data
            country, created = Country.objects.update_or_create(
                cca2=country_data.get('cca2'),
                defaults={
                    'name_common': country_data['name']['common'],
                    'name_official': country_data['name']['official'],
                    'cca3': country_data.get('cca3'),
                    'ccn3': country_data.get('ccn3', ''),
                    'cioc': country_data.get('cioc', ''),
                    'flag': country_data.get('flags', {}).get('svg'),
                    'capital': country_data.get('capital', [''])[0],
                    'area': country_data.get('area', 0),
                    'population': country_data.get('population', 0),
                    'region': country_data.get('region', ''),
                    'subregion': country_data.get('subregion', ''),
                    'languages': country_data.get('languages', {}),
                    'latlng': country_data.get('latlng', []),
                    'landlocked': country_data.get('landlocked', False),
                    'borders': country_data.get('borders', []),
                    'currency': country_data.get('currencies', {}),
                    'timezones': country_data.get('timezones', []),
                    'fifa': country_data.get('fifa', ''),
                    'gini': country_data.get('gini', {}),
                    'coat_of_arms': country_data.get('coatOfArms', {}).get('svg', ''),
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added {country.name_common}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Updated {country.name_common}"))
