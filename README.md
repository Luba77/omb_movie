# Django Project

## This project is a web application based on Django Rest Framework.

### Instalation
``` bash
git clone https://github.com/Luba77/omb_movie.git
```

### Install and activate virtual env depends on your system
#### Example (windows system):
``` bash
pip install virtualenv
virtualenv venv
venv/Scripts/activate
```

### Next steps
``` bash
cd omb_movie
pip install -r requirements.txt
```

### Put secret key
in settings.py put SECRET KEY from credentials/settings.py

``` bash
python manage.py migrate
```

## Run the script:
``` bash
python parser.py
```

## Running of project
``` bash
python manage.py runserver
```

### URL Patterns
``` bash
api/movies/: Displays a list of movies and allows creating new movies.
```
``` bash
api/movies/int:pk/: Displays details of a specific movie, actors, year created.
Allows to delete, update movies, actors, directors.
```
``` bash
api/directors/: Shows a list of persons directors.
```
``` bash
api/actors/ : Shows a list of actors actors.
```


