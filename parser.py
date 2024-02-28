import requests
import django
django.setup()

from credentials.settings import OMB_API_KEY
from movies.models import Movie, Actor, Director



def fetch_movies_from_omdb():
    api_key = OMB_API_KEY
    url = "http://www.omdbapi.com/"

    # Define the range of IMDb IDs you want to fetch
    start_id = 1000000
    end_id = 1000300  # Adjust this to your desired end ID

    for imdb_id in range(start_id, end_id + 1):
        params = {"apikey": api_key, "i": f"tt{imdb_id}"}
        response = requests.get(url, params=params)
        data = response.json()

        # Check if the response contains valid movie data
        if 'Title' not in data:
            print(f"No movie data found for IMDb ID: tt{imdb_id}. Skipping...")
            continue

        # Process the response data for movie
        title = data['Title']
        year = data.get('Year', '')
        director_name = data.get('Director', '')
        actors_data = data.get('Actors', '').split(', ')

        # Try to get or create director
        if director_name:
            director, _ = Director.objects.get_or_create(name=director_name)
        else:
            print(f"Director name is missing for movie '{title}'. Skipping...")
            continue

        # Try to get the movie by title
        try:
            movie, created = Movie.objects.get_or_create(title=title, defaults={'year': year, 'director': director})
            if created:
                print(f"New movie '{title}' created successfully.")
            else:
                print(f"Movie '{title}' already exists.")
        except Exception as e:
            print(f"Error creating movie '{title}': {e}")

        # Process actors for the movie
        for actor_name in actors_data:
            actor, _ = Actor.objects.get_or_create(name=actor_name)
            movie.actors.add(actor)

        print(f"Actors for movie '{title}' processed successfully.")


fetch_movies_from_omdb()
print("Done.")
