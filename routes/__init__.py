import uuid
from functools import wraps

from flask import (
    session,
    request,
    abort,
)

from models.user import User
from utils import log

def current_user():
    uid = session.get('user_id', '')
    u = User.one(id=uid)
    return u

csrf_tokens = dict()


def csrf_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        u = current_user()
        log('token ', token)
        log('csrf_tokens ', csrf_tokens)

        if token in csrf_tokens and csrf_tokens[token] == u.id:
            csrf_tokens.pop(token)
            return f(*args, **kwargs)
        else:
            abort(401)

    return wrapper


def new_csrf_token():
    u = current_user()
    token = str(uuid.uuid4())
    csrf_tokens[token] = u.id
    return token