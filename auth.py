## -------------------- Emil Ferent, Sep 2024 ---------------------
# the api key must be in the heather of the requests

from functools import wraps
from flask import request, jsonify

# to do: change it to e.g. 9b16b955-29a1-4a0c-a087-5a4ea06d6221
# or any other mechanism; could even add expiration dates + un/pw key refresh
API_KEY = "your-api-key" 

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'API-Key' not in request.headers or request.headers['API-Key'] != API_KEY:
            return jsonify({"error": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return decorated_function
