
from flask import request
from flask_restx import Resource

from ..util.dto import LogEntriesDto
from ..service.logEntry_service import save_log_entry, get_entries_for_date, get_entries_by_subject, get_entries_by_searchString

import datetime

api = LogEntriesDto.api
_logentry = LogEntriesDto.log_entries


@api.route('/')
@api.response(404, 'No entries found.')
class LogEntryListForToday(Resource):
    @api.doc('log_entries_from_today')
    @api.marshal_list_with(_logentry)
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
        targetDate = datetime.datetime.fromisoformat(date)

        return get_entries_for_date(targetDate)


@ api.route('/search/subject/<subject>')
@ api.param('subject', 'The subject to search for')
@ api.response(404, 'LogEntry not found.')
class LogEntrySubjectSearch(Resource):
    @ api.doc('Get log entries with a given subject')
    @ api.marshal_with(_logentry)
    def get(self, subject):
        """Get log entries with a given subject"""
        return get_entries_by_subject(subject)


@ api.route('/search/string/<searchString>')
@ api.param('searchString', 'The subject to search for')
@ api.response(404, 'LogEntry not found.')
class LogEntryStringSearch(Resource):
    @ api.doc('Get log entries containing a given string in the subject or text')
    @ api.marshal_with(_logentry)
    def get(self, searchString):
        """Get log entries with a given string"""
        return get_entries_by_searchString(searchString)
