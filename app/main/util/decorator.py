from functools import wraps

from flask import request

from app.main.service.auth_helper import Auth


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        userData = data.get('data')

        if not userData:
            return data, status

        request.userData = userData

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        userData = data.get('data')

        if not userData:
            return data, status

        admin = userData.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        request.userData = userData

        return f(*args, **kwargs)

    return decorated
