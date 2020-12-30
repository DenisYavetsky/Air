import json
from .models import Airport

# пустой список аэропортов
airport = []


def read_file():
    with open('source/air.json', 'r', encoding='UTF-8') as jsonfile:
        airports = json.load(jsonfile)


    for a in airports:
        air = Airport()
        air.icao_code = a['icao_code']
        air.name = a['name_rus']
        air.town = a['city_rus']
        air.save()


