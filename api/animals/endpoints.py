from flask import Blueprint, request, abort
from ..common.utils import json_result
from .model import Animal

animal = Blueprint("animal", __name__, url_prefix="/animals")

@animal.route("/", methods = ["GET"])
@json_result
def animals(): return "Hello animals world!"

@animal.route("/", methods = ["POST"])
@json_result
def create_animal():
    if not request.json:
        abort(400)
    data = request.get_json()
    animal_doc = Animal(**data)
    return {}

@animal.route("/<animal_id>", methods = ["PUT"])
@json_result
def update_animal(animal_id):
    return 'test'

@animal.route("/<animal_id>", methods = ["DELETE"])
@json_result
def delete_animal(animal_id):
    return {}
