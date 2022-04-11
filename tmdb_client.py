import json
from ssl import ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE
import requests

list_to_choose = [{'popular':'Popular'}, {'upcoming':'Upcoming'}, {'now_playing': 'Now Playing'}, {'top_rated':'Top Rated'}]

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNWE0ODAwNjAyYWNhZmQyOTk1NzQyNTUyNjQwNjUxYyIsInN1YiI6IjYyNGRiMDM2MTg4NjRiMDBhMTcwMjdmMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eD3iQwps65PMH2kf7ua8KbqWpFVXabq8zgZ5jY4KoUU"


def get_popular_movies():
    url = 'https://api.themoviedb.org/3/movie/popular'
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_movies_list(list_type='popular'):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    for list in list_to_choose:
        if list_type in list.keys():
            return response.json()
        return get_popular_movies()            
            

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


