import unittest

from app.main import db
from app.main.model.logEntry import LogEntry
import json
from app.test.base import BaseTestCase

import datetime

from app.test.helpers import get_nonadmin_authKey, create_log_entry


class TestLogEntriesRead(BaseTestCase):
    def test_get_log_entries_by_date(self):
        authKey = get_nonadmin_authKey(self)

        create_log_entry(self, authKey, "Just some subject", "words, words")
        create_log_entry(self, authKey, "Some subject",
                         "blib blib blib")

        response = self.client.get(
            '/api/entries/{}/{}'.format(_getAnHourAgoUTC(),
                                        _getAnHoursTimeUTC()),
            headers=dict(
                Authorization=authKey
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data,
                             msg="response is : %s" % response)

        responseData = json.loads(response.data.decode())

        self.assertIsInstance(responseData, list)
        self.assertEqual(len(responseData), 2,
                         msg="data: {}".format(responseData))

        firstEntry = responseData[0]

        self.assertIn("id", firstEntry)
        self.assertEquals(firstEntry['subject'], "Some subject")
        self.assertEquals(firstEntry['text'], "blib blib blib")
        self.assertEquals(firstEntry['author_name'],
                          "steve", msg="data: {}".format(responseData))
        self.assertEquals(firstEntry['group_name'], "adminGroup")

    def test_get_log_entries_by_author_without_limit(self):
        authKey = get_nonadmin_authKey(self)

        create_log_entry(self, authKey, "Just some subject", "words, words")
        create_log_entry(self, authKey, "Some subject",
                         "blib blib blib")

        response = self.client.get(
            '/api/entries/search/author/steve/',
            headers=dict(
                Authorization=authKey
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data,
                             msg="response is : %s" % response)

        responseData = json.loads(response.data.decode())

        self.assertIsInstance(responseData, list)
        self.assertEqual(len(responseData), 2,
                         msg="data: {}".format(responseData))

        firstEntry = responseData[0]

        self.assertIn("id", firstEntry)
        self.assertEquals(firstEntry['subject'], "Some subject")
        self.assertEquals(firstEntry['text'], "blib blib blib")
        self.assertEquals(firstEntry['author_name'],
                          "steve", msg="data: {}".format(responseData))
        self.assertEquals(firstEntry['group_name'], "adminGroup")

    def test_get_log_entries_by_author_with_limit(self):
        authKey = get_nonadmin_authKey(self)

        create_log_entry(self, authKey, "Just some subject", "words, words")
        create_log_entry(self, authKey, "Some subject",
                         "blib blib blib")

        response = self.client.get(
            '/api/entries/search/author/steve/1',
            headers=dict(
                Authorization=authKey
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data,
                             msg="response is : %s" % response)

        responseData = json.loads(response.data.decode())

        self.assertIsInstance(responseData, list)
        self.assertEqual(len(responseData), 1,
                         msg="data: {}".format(responseData))

        firstEntry = responseData[0]

        self.assertIn("id", firstEntry)
        self.assertEquals(firstEntry['subject'], "Some subject")
        self.assertEquals(firstEntry['text'], "blib blib blib")
        self.assertEquals(firstEntry['author_name'],
                          "steve", msg="data: {}".format(responseData))
        self.assertEquals(firstEntry['group_name'], "adminGroup")

    def test_get_log_entries_by_subject(self):
        authKey = get_nonadmin_authKey(self)

        create_log_entry(self, authKey, "Just some subject", "words, words")
        create_log_entry(self, authKey, "Some subject",
                         "blib blib blib")

        response = self.client.get(
            '/api/entries/search/subject/Just some subject',
            headers=dict(
                Authorization=authKey
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data,
                             msg="response is : %s" % response)

        responseData = json.loads(response.data.decode())

        self.assertIsInstance(responseData, list)
        self.assertEqual(len(responseData), 1,
                         msg="data: {}".format(responseData))

        firstEntry = responseData[0]

        self.assertIn("id", firstEntry)
        self.assertEquals(firstEntry['subject'], "Just some subject")
        self.assertEquals(firstEntry['text'], "words, words")
        self.assertEquals(firstEntry['author_name'],
                          "steve", msg="data: {}".format(responseData))
        self.assertEquals(firstEntry['group_name'], "adminGroup")


def _getAnHourAgoUTC():
    targetTime = datetime.datetime.utcnow() - datetime.timedelta(hours=1)

    return targetTime.strftime("%Y-%m-%dT%H:%M:%SZ")


def _getAnHoursTimeUTC():
    targetTime = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    return targetTime.strftime("%Y-%m-%dT%H:%M:%SZ")
