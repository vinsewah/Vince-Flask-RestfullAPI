import sqlite3

from flask_restful import Api
from flask import Flask
from flask import g

from app.resources.index import index
from app.resources.movies import get_all_movies, get_movies

app = Flask(__name__)
api = Api(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE_NAME'])
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.errorhandler(404)
def not_found(e):
    return '', 404