from django.db import models

from locations.models import Location


class Company(models.Model):
    rating_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]

    name_movie = models.CharField(max_length=100)
    anul_lansarii = models.CharField(max_length=100)
    nominalizari = models.CharField(max_length=100)
    premii = models.CharField(max_length=100)
    rating = models.CharField(max_length=2, choices=rating_choices)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_movie} {self.anul_lansarii} {self.nominalizari} {self.premii} {self.rating}"
