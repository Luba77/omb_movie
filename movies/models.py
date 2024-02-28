from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=9)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='directed_movies')
    actors = models.ManyToManyField(Actor, related_name='actor_movies')

    def __str__(self):
        return self.title

