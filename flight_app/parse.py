import json
from .models import Airport
import requests


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


def call_API(icao):
    url = "https://aerodatabox.p.rapidapi.com/flights/airports/icao/" + icao + "/2020-12-31T00:00/2020-12-31T12:00"
    querystring = {"withLeg": "true", "withCancelled": "true", "withCodeshared": "true", "withCargo": "true",
                   "withPrivate": "true"}
    headers = {
        'x-rapidapi-key': "e7a6cb63c7mshfdb062b9871fb3ap1ddd61jsn96253092e22e",
        'x-rapidapi-host': "aerodatabox.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()



