
from flask import request
from flask_restx import Resource

from ..util.dto import LogEntryDto
from ..service.logentry_service import save_log_entry

api = LogEntryDto.api
_logentry = LogEntryDto.log_entry


@api.route('/')
class LogEntryList(Resource):
    @api.doc('list_of_registered_logentries')
    @api.marshal_list_with(_logentry, envelope='data')
    def get(self):
        """List all registered logentries"""
        # return get_all_logentries()

    @api.response(201, 'LogEntry successfully created.')
    @api.doc('create a new logentry')
    @api.expect(_logentry, validate=True)
    def post(self):
        """Creates a new LogEntry """
        data = request.json
        return save_log_entry(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The LogEntry identifier')
@api.response(404, 'LogEntry not found.')
class LogEntry(Resource):
    @api.doc('get a logentry')
    @api.marshal_with(_logentry)
    def get(self, public_id):
        pass
        """get a logentry given its identifier"""
        # logentry = get_a_logentry(public_id)
        # if not logentry:
        #     api.abort(404)
        # else:
        #     return logentry
