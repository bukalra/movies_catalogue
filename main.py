from crypt import methods
from flask import Flask, render_template, request, url_for, redirect, flash
import tmdb_client
app = Flask(__name__)
FAVORITES = set()
a = []
app.secret_key = b'my-secret'

@app.route("/favorites/add", methods=['POST'])
def add_to_favorites():
    data = request.form
    movie_id = data.get('movie_id')
    movie_title = data.get('movie_title')
    if movie_id and movie_title:
        FAVORITES.add(movie_id)
        flash(f'Dodano film {movie_title} do ulubionych!')
    return redirect(url_for('homepage'))

@app.route("/favorites")
def show_favorites():
    if FAVORITES:
        movies = []
        for movie_id in FAVORITES:
            movie_details = tmdb_client.get_single_movie(movie_id)
            movies.append(movie_details)
    else:
        movies = []
    return render_template("homepage.html", movies=movies)

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    movies = tmdb_client.get_movies_list(list_type=selected_list)["results"][:8]
    return render_template("homepage.html", movies=movies, list_to_choose = tmdb_client.list_to_choose, selected_list = selected_list)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
   cast = tmdb_client.get_single_movie_cast(movie_id)
   return render_template("movie_details.html", movie=details, cast=cast)

@app.route("/search")
def search():
    search_query = request.args.get("query", "")
    movies = tmdb_client.get_searched_movies(search_query=search_query)['results'][:8]
    return render_template("search.html", movies=movies, search_query=search_query)

@app.route("/search_series")
def search_series():
    search_query = request.args.get("query", "")
    series = tmdb_client.get_searched_series()['results'][:8]
    return render_template("search_series.html", series=series, search_query=search_query)