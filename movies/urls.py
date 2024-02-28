from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListCreateAPIView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
    path('directors/', views.DirectorListCreateAPIView.as_view(), name='director-list'),
    path('actors/', views.ActorListCreateAPIView.as_view(), name='actor-list'),
]
