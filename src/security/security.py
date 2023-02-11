import json
from functools import wraps

from flask import request, jsonify


def token_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        with open('src/credentials/api_key.json', 'r') as file:
            api_file= json.load(file)
            key = api_file.get('X-Api-Key')
        headers = request.headers
        auth = headers.get("X-Api-Key")
        if auth and auth == key:
            return func(*args, **kwargs)
        else:
            return jsonify({"message": "ERROR: Unauthorized"}), 401
    return decorator