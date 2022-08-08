from django.db import models

from .actors import Actor



class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField()
    imdb = models.FloatField(null=True, max_length=2)
    genre = models.CharField(max_length=120)
    actors = models.ManyToManyField(Actor)

    def __str__(self) -> str:
        return self.name