
from flask import request
from flask_restx import Resource

from ..util.dto import LogEntryDto
from ..service.logEntry_service import save_log_entry, get_entries_for_date

from app.main.util.decorator import token_required

import datetime

api = LogEntryDto.api
_logentry = LogEntryDto.log_entry


@api.route('/')
class LogEntryList(Resource):
    @api.response(201, 'LogEntry successfully created.')
    @api.doc('create a new logentry')
    @token_required
    @api.expect(_logentry, validate=True)
    def post(self):
        """Creates a new LogEntry """
        data = request.json

        data['author_id'] = 1234

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
