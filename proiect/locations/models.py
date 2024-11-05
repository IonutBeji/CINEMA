from django.db import models


class Location(models.Model):
    movie = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    projection = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.movie
