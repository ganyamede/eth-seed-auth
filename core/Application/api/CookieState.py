from flask import session, redirect
from functools import wraps

def isAuth(NoAuth):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'address' in session:
                return redirect(NoAuth)
            return f(*args, **kwargs)
        return decorated_function
    return decorator