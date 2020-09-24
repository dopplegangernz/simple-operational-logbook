import unittest

from app.main import db
from app.main.model.blacklist import BlacklistToken
import json
from app.test.base import BaseTestCase
from app.test.helpers import register_group, register_user, login_user


class TestGroups(BaseTestCase):
    """Test for group registration"""

    def test_group_registration(self):
        with self.client:
            response = register_group(self)
            data = json.loads(response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')

    def test_get_group_information(self):
        with self.client:
            register_user(self)
            loginResp = login_user(self)
            authKey = json.loads(loginResp.data.decode())['Authorization']

            response = self.client.post(
                '/group/',
                data=json.dumps(dict(
                    name='another test group',
                    description='a second test group'
                )),
                content_type='application/json'
            )

            responseData = json.loads(response.data.decode())
            groupId = responseData['id']

            response = self.client.get(
                '/group/{}'.format(groupId),
                headers=dict(
                    Authorization=authKey
                ),
                content_type='application/json'
            )
            responseData = json.loads(response.data.decode())

            self.assertIn("id", responseData,
                          msg="response is : %s" % response)
            self.assertEquals(responseData['id'], groupId)
            self.assertEquals(responseData['name'], "another test group")
            self.assertEquals(
                responseData['description'], "a second test group")

    def test_group_update(self):
        with self.client:
            response = register_group(self)
            data = json.loads(response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')

            public_id = data['id']

            resp_register = register_user(self)

            response = self.client.get(
                '/group/',
                content_type='application/json',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        resp_register.data.decode()
                    )['Authorization']
                )
            )

            response = self.client.patch(
                '/group/',
                data=json.dumps(dict(
                    group='renamedGroup',
                    description='renamed group, yo'
                )),
                content_type='application/json',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        resp_register.data.decode()
                    )['Authorization']
                )
            )


if __name__ == '__main__':
    unittest.main()
