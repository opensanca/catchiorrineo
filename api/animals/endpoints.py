from flask import Blueprint, request, abort
from api.common.utils import json_result

animal = Blueprint("animal", __name__, url_prefix="/animals")

@animal.route("/", methods = ["GET"])
@json_result
def animals(): return "Hello animals world!"

@animal.route("/", methods = ["POST"])
@json_result
def create_animal():
    if not request.json:
        abort(400)
    return {}