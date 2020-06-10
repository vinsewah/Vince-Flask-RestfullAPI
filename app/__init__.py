import sqlite3

from flask_restful import Api
from flask import Flask
from flask import g


app = Flask(__name__)

api = Api(app)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.errorhandler(404)
def not_found(e):
    return '', 404


from app.resources.index import index
from app.resources.movies import get_every_movie
