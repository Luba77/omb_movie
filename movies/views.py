from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import MovieFilter, DirectorFilter, ActorFilter
from .models import Movie, Director, Actor
from .serializers import MovieSerializer, DirectorSerializer, ActorSerializer


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter


class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DirectorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DirectorFilter


class ActorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ActorFilter
