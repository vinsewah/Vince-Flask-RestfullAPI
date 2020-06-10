from flask import jsonify
from flask import Blueprint

index = Blueprint('index', __name__)


@index.route('/', methods=["GET"])
def index():
    return jsonify("hello world")