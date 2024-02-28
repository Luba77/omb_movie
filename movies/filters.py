import django_filters
from .models import Movie, Director, Actor


class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = {
            'year': ['exact', 'gte', 'lte'],
            'director__name': ['exact'],
            'actors__name': ['exact']
        }


class DirectorFilter(django_filters.FilterSet):
    class Meta:
        model = Director
        fields = {
            'name': ['exact']
        }


class ActorFilter(django_filters.FilterSet):
    class Meta:
        model = Actor
        fields = {
            'name': ['exact']
        }
