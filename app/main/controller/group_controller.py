from flask import request
from flask_restplus import Resource

from ..util.dto import GroupDto
from ..service.group_service import save_new_group, get_all_groups, get_a_group

api = GroupDto.api
_group = GroupDto.group


@api.route('/')
class GroupList(Resource):
    @api.doc('list_of_registered_groups')
    @api.marshal_list_with(_group, envelope='data')
    def get(self):
        """List all registered groups"""
        return get_all_groups()

    @api.response(201, 'Group successfully created.')
    @api.doc('create a new group')
    @api.expect(_group, validate=True)
    def post(self):
        """Creates a new Group """
        data = request.json
        return save_new_group(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Group identifier')
@api.response(404, 'Group not found.')
class Group(Resource):
    @api.doc('get a group')
    @api.marshal_with(_group)
    def get(self, public_id):
        """get a group given its identifier"""
        group = get_a_group(public_id)
        if not group:
            api.abort(404)
        else:
            return group
