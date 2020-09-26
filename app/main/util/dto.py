from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'group': fields.String(attribute='group.name', required=True, description='Name of user\'s default group'),
        'public_id': fields.String(description='user Identifier'),
        'isAdmin': fields.String(attribute='admin', description='Is the user and admin?'),
    })


class GroupDto:
    api = Namespace('group', description='group related operations')
    group = api.model('group', {
        'name': fields.String(required=True, description='group name'),
        'description': fields.String(required=False, description='Description of the group'),
        'id': fields.String(attribute='public_id', description='group Identifier')
    })


class LogEntryDto:
    api = Namespace('logEntry', description='log entry related operations')
    log_entry = api.model('logEntry', {
        'id': fields.String(attribute='public_id', description='entry Identifier'),
        'subject': fields.String(required=True, description='The subject of the log entry'),
        'text': fields.String(required=True, description='The content of the entry'),
        'timeStamp': fields.DateTime(description='when the entry was created'),
        'author_name': fields.String(attribute='author.username', description='the user id of the person who creted the entry'),
        'group_name': fields.String(attribute='group.name', required=True, description='Name of the group the entry is relevant to'),
    })


class LogEntriesDto:
    api = Namespace(
        'logEntries', description='log entry set related operations')
    log_entries = api.model('logEntry', {
        'id': fields.String(attribute='public_id', description='entry Identifier'),
        'subject': fields.String(required=True, description='The subject of the log entry'),
        'text': fields.String(required=True, description='The content of the entry'),
        'timestamp': fields.DateTime(description='when the entry was created'),
        'author_name': fields.String(attribute='author.username', description='the user id of the person who creted the entry'),
        'group_name': fields.String(attribute='group.name', required=True, description='Name of the group the entry is relevant to'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
