from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'group_name': fields.String(required=True, description='Name of user\'s group'),
        'public_id': fields.String(description='user Identifier')
    })


class GroupDto:
    api = Namespace('group', description='group related operations')
    group = api.model('group', {
        'name': fields.String(required=True, description='group name'),
        'description': fields.String(required=False, description='Description of the group'),
        'public_id': fields.String(description='group Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
