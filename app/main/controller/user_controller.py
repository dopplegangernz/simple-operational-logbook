from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, update_a_user
from ..service.group_service import get_a_group_by_name

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

    @api.doc('Update a user')
    @api.marshal_with(_user)
    @token_required
    def patch(self):
        """Update a user"""
        data = request.json
        user = get_a_user(data['id'])

        group = get_a_group_by_name(data['group_name'])

        if not user:
            api.abort(404, "No such user")
        elif not group:
            api.abort(404, "Not a valid group")
        else:
            if request.userData['user_id'] == user.id or request.userData['admin'] == True:
                return update_a_user(user, group, data)
            else:
                api.abort(
                    403, message="You do not have permission to update this user")


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
