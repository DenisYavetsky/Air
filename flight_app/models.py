from django.db import models
from django.shortcuts import reverse


class Airport(models.Model):
    name = models.TextField(max_length=100)
    icao_code = models.CharField(max_length=10, unique=True)
    town = models.TextField(max_length=100)

    def get_icao_code(self):
        return reverse('AirportInfo', kwargs={'icao_code': self.icao_code})

    def __str__(self):
        return f'{self.name}, {self.town}, {self.icao_code}'


class Flight(models.Model):
    arrivalCity = models.TextField(max_length=100)
    departmentCity = models.TextField(max_length=100)
    number = models.TextField(max_length=20)
    status = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.number} {self.status}'
