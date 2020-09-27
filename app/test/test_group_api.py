import unittest

from app.main import db
from app.main.model.blacklist import BlacklistToken
import json
from app.test.base import BaseTestCase
from app.test.helpers import create_admin_user, create_nonadmin_user


class TestGroupCreate(BaseTestCase):
    """Tests for group creation"""

    def test_group_create_with_valid_info(self):
        authKey = create_admin_user(self)['authKey']
        with self.client:
            response = self.client.post(
                '/api/group/',
                data=json.dumps(dict(
                    name='testGroup',
                    description='A group for testing'
                )),
                headers=dict(
                    Authorization=authKey
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['status'] == 'success',
                            msg="data is : %s" % data)
            self.assertTrue(data['message'] == 'Successfully registered.')

    def test_group_create_with_duplicate_info(self):
        authKey = create_admin_user(self)['authKey']
        with self.client:
            response = self.client.post(
                '/api/group/',
                data=json.dumps(dict(
                    name='adminGroup',
                    description='A group for bootstrapping testing'
                )),
                headers=dict(
                    Authorization=authKey
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['status'] == 'fail',
                            msg="data is : %s" % data)
            self.assertTrue(data['message'] == 'Group already exists.')

    def test_group_create_without_valid_login(self):
        authKey = create_admin_user(self)['authKey']
        with self.client:
            response = self.client.post(
                '/api/group/',
                data=json.dumps(dict(
                    name='testGroup',
                    description='A group for testing'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['status'] == 'fail',
                            msg="data is : %s" % data)
            self.assertTrue(data['message'] ==
                            'You must be logged in to do that.')

    def test_group_create_with_nonadmin_user(self):
        authKey = create_nonadmin_user(self)['authKey']
        with self.client:
            response = self.client.post(
                '/api/group/',
                data=json.dumps(dict(
                    name='testGroup',
                    description='A group for testing'
                )),
                headers=dict(
                    Authorization=authKey
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['status'] == 'fail',
                            msg="data is : %s" % data)
            self.assertTrue(
                data['message'] == 'You must be logged in as an admin to do that', msg="data is : %s" % data)


class TestGroupRead(BaseTestCase):
    def test_group_read(self):
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
                headers=dict(
                    Authorization=authKey
                ),
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

    def test_group_read_without_valid_auth(self):
        raise Exception()


class TestGroupUpdate(BaseTestCase):
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


class TestGroupsRead(BaseTestCase):
    def test_groups_read(self):
        raise Exception()


if __name__ == '__main__':
    unittest.main()
