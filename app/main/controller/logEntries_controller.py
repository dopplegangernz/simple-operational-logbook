
from flask import request
from flask_restx import Resource

from ..util.dto import LogEntriesDto
from ..service.logEntry_service import save_log_entry, get_entries_for_time_range, get_entries_by_subject, get_entries_by_searchString

import datetime
import re

timestampRe = re.compile("(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)Z")

api = LogEntriesDto.api
_logentry = LogEntriesDto.log_entries


# @api.route('/')
# @api.response(404, 'No entries found.')
# class LogEntryListForToday(Resource):
#     @api.doc('log_entries_from_today')
#     @api.marshal_list_with(_logentry)
#     def get(self):
#         """List of log entries from today"""

#         return get_entries_for_date(datetime.datetime.now(datetime.timezone.utc))


@ api.route('/<fromTimestamp>/<toTimestamp>')
@ api.param('fromTimestamp', 'The start of the range we\'re interested in (UTC, formatted YYYY-MM-DDTHH:MM:SSZ e.g. 2020-09-22T12:34:54Z)')
@ api.param('toTimestamp', 'The end of the range we\'re interested in (UTC, formatted YYYY-MM-DDTHH:MM:SSZ e.g. 2020-09-22T12:34:54Z)')
@ api.response(404, 'No entries found.')
class LogEntryListForDate(Resource):
    @ api.doc('Get log entries for a date')
    @ api.marshal_with(_logentry)
    def get(self, fromTimestamp, toTimestamp):
        """get log entries for a date range"""
        fromMatch = timestampRe.match(fromTimestamp)
        toMatch = timestampRe.match(toTimestamp)

        fromDate = datetime.datetime(*[int(value)
                                       for value in fromMatch.groups()])
        toDate = datetime.datetime(*[int(value) for value in toMatch.groups()])

        return get_entries_for_time_range(fromDate, toDate)


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
