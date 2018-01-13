import json
from functools import wraps

def json_result(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        response = fn(*args, **kwargs)
        return json.dumps(response)
    return wrapper
