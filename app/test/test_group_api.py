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
                    description='A group for testing',
                    public_id='123456'
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
            bootstrap = create_nonadmin_user(self)

            response = self.client.get(
                '/api/group/{}/'.format(bootstrap['groupPublicId']),
                headers=dict(
                    Authorization=bootstrap['authKey']
                ),
                content_type='application/json'
            )

            self.assertEqual(response.status_code, 200,
                             msg="response is : {}".format(response.data.decode()))
            self.assertIsNotNone(response.data,
                                 msg="response is : {}".format(response))
            responseData = json.loads(response.data.decode())
            self.assertIn("id", responseData,
                          msg="response is : {}".format(response))
            self.assertEquals(responseData['id'], bootstrap['groupPublicId'])
            self.assertEquals(responseData['name'], "adminGroup")
            self.assertEquals(
                responseData['description'], "A group for bootstrapping testing")

    def test_group_read_without_valid_auth(self):
        with self.client:
            bootstrap = create_nonadmin_user(self)

            response = self.client.get(
                '/api/group/{}/'.format(bootstrap['groupPublicId']),
                content_type='application/json'
            )

            self.assertEqual(response.status_code, 200,
                             msg="response is : {}".format(response.data.decode()))
            self.assertIsNotNone(response.data,
                                 msg="response is : {}".format(response))
            responseData = json.loads(response.data.decode())
            self.assertIn("id", responseData,
                          msg="response is : {}".format(response))
            self.assertEquals(responseData['id'], bootstrap['groupPublicId'])
            self.assertEquals(responseData['name'], "adminGroup")
            self.assertEquals(
                responseData['description'], "A group for bootstrapping testing")


class TestGroupUpdate(BaseTestCase):
    def test_group_update(self):
        with self.client:
            bootstrap = create_admin_user(self)

            public_id = bootstrap['groupPublicId']

            response = self.client.patch(
                '/api/group/{}/'.format(bootstrap['groupPublicId']),
                data=json.dumps(dict(
                    name='renamedGroup',
                    description='renamed group, yo'
                )),
                content_type='application/json',
                headers=dict(
                    Authorization=bootstrap['authKey']
                )
            )
            self.assertEqual(response.status_code, 200,
                             msg="response is : {}".format(response.data.decode()))
            self.assertIsNotNone(response.data,
                                 msg="response is : {}".format(response))
            responseData = json.loads(response.data.decode())
            self.assertIn("id", responseData,
                          msg="response is : {}".format(response))
            self.assertEquals(responseData['id'], bootstrap['groupPublicId'])
            self.assertEquals(responseData['name'], "renamedGroup")
            self.assertEquals(
                responseData['description'], "renamed group, yo")

    def test_group_update_by_nonadmin(self):
        with self.client:
            bootstrap = create_nonadmin_user(self)

            public_id = bootstrap['groupPublicId']

            response = self.client.patch(
                '/api/group/{}/'.format(bootstrap['groupPublicId']),
                data=json.dumps(dict(
                    name='renamedGroup',
                    description='renamed group, yo'
                )),
                content_type='application/json',
                headers=dict(
                    Authorization=bootstrap['authKey']
                )
            )
            self.assertEqual(response.status_code, 401,
                             msg="response is : {}".format(response.data.decode()))
            self.assertIsNotNone(response.data,
                                 msg="response is : {}".format(response))
            responseData = json.loads(response.data.decode())
            self.assertEquals(responseData['status'], 'fail')
            self.assertEquals(
                responseData['message'], "You must be logged in as an admin to do that")

    def test_group_update_with_bad_id(self):
        with self.client:
            bootstrap = create_admin_user(self)

            public_id = bootstrap['groupPublicId']

            response = self.client.patch(
                '/api/group/someBadId/',
                data=json.dumps(dict(
                    name='renamedGroup',
                    description='renamed group, yo'
                )),
                content_type='application/json',
                headers=dict(
                    Authorization=bootstrap['authKey']
                )
            )
            self.assertEqual(response.status_code, 404,
                             msg="response is : {}".format(response.data.decode()))
            self.assertIsNotNone(response.data,
                                 msg="response is : {}".format(response))
            responseData = json.loads(response.data.decode())
            self.assertEquals(
                responseData['message'], "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again. You have requested this URI [/api/group/someBadId/] but did you mean /api/group/<public_id>/ or /api/group/ ?")


class TestGroupsRead(BaseTestCase):
    def test_groups_read(self):
        authKey = create_admin_user(self)['authKey']
        with self.client:
            self.client.post(
                '/api/group/',
                data=json.dumps(dict(
                    name='group1',
                    description='A group for testing',
                    public_id='123456'
                )),
                headers=dict(
                    Authorization=authKey
                ),
                content_type='application/json'
            )
            self.client.post(
                '/api/group/',
                data=json.dumps(dict(
                    name='group2',
                    description='Another group for testing',
                    public_id='34566'
                )),
                headers=dict(
                    Authorization=authKey
                ),
                content_type='application/json'
            )
            self.client.post(
                '/api/group/',
                data=json.dumps(dict(
                    name='group3',
                    description='yet another group for testing',
                    public_id='12234563456'
                )),
                headers=dict(
                    Authorization=authKey
                ),
                content_type='application/json'
            )
            response = self.client.get(
                '/api/group/',
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200,
                             msg="response is : {}".format(response.data.decode()))
            self.assertIsNotNone(response.data,
                                 msg="response is : {}".format(response))
            responseData = json.loads(response.data.decode())
            # There was the admin group in there before we added two more
            self.assertEqual(len(responseData), 4)
            group2 = responseData[2]
            self.assertEqual(group2['name'], "group2")
            self.assertEqual(group2['description'],
                             "Another group for testing")


if __name__ == '__main__':
    unittest.main()
