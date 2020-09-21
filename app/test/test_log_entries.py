import unittest

from app.main import db
from app.main.model.logEntry import LogEntry
import json
from app.test.base import BaseTestCase

import datetime

from app.test.helpers import register_user, login_user, create_log_entry


class TestLogEntries(BaseTestCase):
    def test_get_log_entries(self):
        register_user(self)
        loginResp = login_user(self)

        authKey = json.loads(loginResp.data.decode())['Authorization']

        create_log_entry(self, authKey, "Some subject", "words, words, words")
        create_log_entry(self, authKey, "Some other subject",
                         "more, different, and betterer words")

        response = self.client.get(
            '/entries/',
            headers=dict(
                Authorization=authKey
            ),
            content_type='application/json'
        )
        self.assertIsNotNone(response.data,
                             msg="response is : %s" % response)

        responseData = json.loads(response.data.decode())

        self.assertIsInstance(responseData, list)
        self.assertEqual(len(responseData), 2)

        firstEntry = responseData[0]

        self.assertIn("id", firstEntry)
        self.assertEquals(firstEntry['subject'], "Some other subject")
        self.assertEquals(firstEntry['text'],
                          "more, different, and betterer words")
        self.assertEquals(firstEntry['author_name'], "test username")
        self.assertEquals(firstEntry['group_name'], "testGroup")

    def test_get_log_entries_by_date(self):
        register_user(self)
        loginResp = login_user(self)

        authKey = json.loads(loginResp.data.decode())['Authorization']

        create_log_entry(self, authKey, "Just some subject", "words, words")
        create_log_entry(self, authKey, "Some subject",
                         "blib blib blib")

        response = self.client.get(
            '/entries/{}'.format(datetime.date.today().isoformat()),
            headers=dict(
                Authorization=authKey
            ),
            content_type='application/json'
        )
        self.assertIsNotNone(response.data,
                             msg="response is : %s" % response)

        responseData = json.loads(response.data.decode())

        self.assertIsInstance(responseData, list)
        self.assertEqual(len(responseData), 2)

        firstEntry = responseData[0]

        self.assertIn("id", firstEntry)
        self.assertEquals(firstEntry['subject'], "Some subject")
        self.assertEquals(firstEntry['text'], "blib blib blib")
        self.assertEquals(firstEntry['author_name'], "test username")
        self.assertEquals(firstEntry['group_name'], "testGroup")
