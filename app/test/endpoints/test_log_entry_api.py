import unittest

from app.main import db
from app.main.model.logEntry import LogEntry
import json
from app.test.base import BaseTestCase

from app.test.helpers import create_log_entry, get_nonadmin_authKey


class TestLogEntryCreate(BaseTestCase):
    def test_create_log_entry(self):
        authKey = get_nonadmin_authKey(self)

        response = create_log_entry(
            self, authKey, "Some subject", "words, words, words")

        responseData = json.loads(response.data.decode())

        self.assertIn("status", responseData,
                      msg="response is : %s" % response)
        self.assertIn("id", responseData)
        self.assertTrue(responseData['status'] == 'success', msg="{}".format(
            response.data.decode()))

    def test_create_log_entry_with_invalid_session(self):
        raise Exception()


class TestLogEntryRead(BaseTestCase):
    def test_get_log_entry(self):
        authKey = get_nonadmin_authKey(self)

        response = create_log_entry(
            self, authKey, "Some subject", "words, words, words")

        responseData = json.loads(response.data.decode())

        entryId = responseData['id']

        response = self.client.get(
            '/api/entry/{}'.format(entryId),
            headers=dict(
                Authorization=authKey
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200,
                         msg="response is : {}".format(response.data.decode()))
        self.assertIsNotNone(response.data,
                             msg="response is : {}".format(response))
        responseData = json.loads(response.data.decode())

        self.assertIn("id", responseData,
                      msg="response is : %s" % response)
        self.assertEquals(responseData['id'], entryId)
        self.assertEquals(responseData['subject'], "Some subject")
        self.assertEquals(responseData['text'], "words, words, words")
        self.assertEquals(responseData['author_name'], "steve")
        self.assertEquals(responseData['group_name'], "adminGroup")

    def test_get_log_entry_with_invalid_id(self):
        raise Exception()
