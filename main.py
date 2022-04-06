from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    movies = ["Forest Gump", "Troy", "Castaway", "Matrix"]
    return render_template("homepage.html", movies=movies)