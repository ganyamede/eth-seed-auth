from flask import jsonify
from flask_jwt_extended import get_jwt_identity


def HelloWorld():
    return jsonify('Hello World!')