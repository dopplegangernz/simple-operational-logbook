
from flask import request
from flask_restx import Resource

from ..util.dto import LogEntriesDto
from ..service.logEntry_service import save_log_entry, get_entries_for_date

import datetime

api = LogEntriesDto.api
_logentry = LogEntriesDto.log_entries


@api.route('/')
@api.response(404, 'No entries found.')
class LogEntryListForToday(Resource):
    @api.doc('log_entries_from_today')
    @api.marshal_list_with(_logentry, envelope='data')
    def get(self):
        """List of log entries from today"""

        return get_entries_for_date(datetime.datetime.now(datetime.timezone.utc))


@ api.route('/<date>')
@ api.param('date', 'The date to provide entries for (ISO8601 extended format: 2020-01-01)')
@ api.response(404, 'No entries found.')
class LogEntryListForDate(Resource):
    @ api.doc('Get log entries for a date')
    @ api.marshal_with(_logentry)
    def get(self, date):
        """get log engries for a date"""
        targetDate = datetime.date.fromisoformat(date)

        return get_entries_for_date(targetDate)


@ api.route('/search/subject/<subject>')
@ api.param('subject', 'The subject to search for')
@ api.response(404, 'LogEntry not found.')
class LogEntrySubjectSearch(Resource):
    @ api.doc('Get log entries with a given subject')
    @ api.marshal_with(_logentry)
    def get(self, public_id):
        pass
        """get a logentry given its identifier"""
        # logentry = get_a_logentry(public_id)
        # if not logentry:
        #     api.abort(404)
        # else:
        #     return logentry
