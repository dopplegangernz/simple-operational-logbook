
from flask import request
from flask_restx import Resource

from ..util.dto import LogEntryDto
from ..service.logEntry_service import save_log_entry, get_entries_for_date

import datetime

api = LogEntryDto.api
_logentry = LogEntryDto.log_entry


@api.route('/')
class LogEntryList(Resource):
    @api.doc('log_entries_from_today')
    @api.marshal_list_with(_logentry, envelope='data')
    def get(self):
        """List of log entries from today"""
        return get_entries_for_date(datetime.datetime.now(datetime.timezone.utc))

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


@api.route('/date/<date>')
@api.param('date', 'The date to provide entries for')
@api.response(404, 'No entries found.')
class LogEntry(Resource):
    @api.doc('get log entries for a date')
    @api.marshal_with(_logentry)
    def get(self, date):
        """get log engries for a date"""
        return get_entries_for_date(date)
