from functools import wraps
from flask import g, Response
from werkzeug.exceptions import Unauthorized


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            raise Unauthorized()

        return view(**kwargs)

    return wrapped_view
