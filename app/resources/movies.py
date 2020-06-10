from app import app
from app.services.movies import get_all_movies
from flask import jsonify


@app.route('/movies', methods=["GET"])
def get_movies():
    result = get_all_movies()
    return jsonify(result)