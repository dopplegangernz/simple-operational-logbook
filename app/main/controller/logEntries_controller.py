
from flask import request
from flask_restx import Resource

from ..util.dto import LogEntriesDto
from ..service.logEntry_service import save_log_entry, get_entries_for_time_range, get_entries_by_subject, get_entries_by_searchString, get_entries_by_author

import datetime
import re

timestampRe = re.compile("(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)Z")

api = LogEntriesDto.api
_logentry = LogEntriesDto.log_entries


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


@ api.route('/search/author/<author_name>/<limit>')
@ api.param('author_name', 'The author whose entries we want')
@ api.param('limit', 'The max number of entries to return')
@ api.response(404, 'LogEntry not found.')
class LogEntryAuthorSearchWithLimit(Resource):
    @ api.doc('Get log entries with a given author')
    @ api.marshal_with(_logentry)
    def get(self, author_name, limit):
        """Get log entries with a given author"""
        return get_entries_by_author(author_name, limit)


@ api.route('/search/author/<author_name>/')
@ api.param('author_name', 'The author whose entries we want')
@ api.response(404, 'LogEntry not found.')
class LogEntryAuthorSearch(Resource):
    @ api.doc('Get the last 50 log entries with a given author')
    @ api.marshal_with(_logentry)
    def get(self, author_name):
        """Get log entries with a given author"""
        return get_entries_by_author(author_name, 100)


@ api.route('/search/string/<searchString>')
@ api.param('searchString', 'The subject to search for')
@ api.response(404, 'LogEntry not found.')
class LogEntryStringSearch(Resource):
    @ api.doc('Get log entries containing a given string in the subject or text')
    @ api.marshal_with(_logentry)
    def get(self, searchString):
        """Get log entries with a given string"""
        return get_entries_by_searchString(searchString)
