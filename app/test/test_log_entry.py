import unittest

from app.main import db
from app.main.model.logEntry import LogEntry
import json
from app.test.base import BaseTestCase

from app.test.helpers import register_user, login_user, create_log_entry


class TestLogEntry(BaseTestCase):
    def test_create_log_entry(self):
        register_user(self)
        loginResp = login_user(self)

        authKey = json.loads(loginResp.data.decode())['Authorization']

        response = create_log_entry(
            self, authKey, "Some subeject", "words, words, words")

        responseData = json.loads(response.data.decode())

        self.assertIn("status", responseData,
                      msg="response is : %s" % response)
        self.assertIn("id", responseData)
        self.assertTrue(responseData['status'] == 'success', msg="{}".format(
            response.data.decode()))

    def test_get_log_entry(self):
        register_user(self)
        loginResp = login_user(self)

        authKey = json.loads(loginResp.data.decode())['Authorization']

        response = create_log_entry(
            self, authKey, "Some subject", "words, words, words")

        responseData = json.loads(response.data.decode())

        entryId = responseData['id']

        response = self.client.get(
            '/entry/{}'.format(entryId),
            headers=dict(
                Authorization=authKey
            ),
            content_type='application/json'
        )
        responseData = json.loads(response.data.decode())

        self.assertIn("id", responseData,
                      msg="response is : %s" % response)
        self.assertEquals(responseData['id'], entryId)
        self.assertEquals(responseData['subject'], "Some subject")
        self.assertEquals(responseData['text'], "words, words, words")
        self.assertEquals(responseData['author_name'], "test username")
        self.assertEquals(responseData['group_name'], "testGroup")
