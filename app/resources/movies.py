from app.services.movies import get_all_movies
from flask import jsonify
from flask import Blueprint

movies = Blueprint('movies', __name__)


@movies.route('/movies', methods=["GET"])
def get_movies():
    result = get_all_movies()
    return jsonify(result)