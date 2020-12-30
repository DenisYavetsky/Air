from django.db import models


class Airport(models.Model):
    name = models.TextField(max_length=100)
    icao_code = models.CharField(max_length=10, unique=True)
    town = models.TextField(max_length=100)

    def __str__(self):
        return self.name, self.town


