import unittest

from app.main import db
from app.main.model.logEntry import LogEntry
import json
from app.test.base import BaseTestCase

from app.test.helpers import register_user, login_user


class TestLogEntryModel(BaseTestCase):
    def test_create_log_entry(self):
        register_user(self)
        loginResp = login_user(self)

        authKey = json.loads(loginResp.data.decode())['Authorization']

        response = self.client.post(
            '/entry/',
            headers=dict(
                Authorization=authKey
            ),
            data=json.dumps(dict(
                subject='test subject',
                text='A test log entry. kaloo kalay',
                group_name="testGroup"
            )),
            content_type='application/json'
        )

        responseData = json.loads(response.data.decode())

        self.assertIn("status", responseData,
                      msg="response is : %s" % response)
        self.assertTrue(responseData['status'] == 'success', msg="{}".format(
            response.data.decode()))
