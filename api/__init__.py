from flask import Flask, jsonify
from flask_cors import CORS
from mongoengine import connect

import settings
from api.animals.endpoints import ANIMAL
from .common.exceptions import InvalidInput


connect(host=settings.MONGODB_URI)


def handle_invalid_input(error):
    """Trata exceções do tipo InvalidInput,
    retornando o dicionário de mensagens e
    o status 400 BAD REQUEST"""
    response = jsonify(error.errors)
    response.status_code = error.status_code
    return response


def create_app():
    app = Flask(__name__)

    CORS(app)

    app.register_blueprint(ANIMAL)
    app.register_error_handler(InvalidInput, handle_invalid_input)

    return app
