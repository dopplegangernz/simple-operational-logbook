import unittest

from app.main import db
from app.main.model.blacklist import BlacklistToken
import json
from app.test.base import BaseTestCase
from app.test.helpers import create_group, create_admin_user, create_nonadmin_user


class TestUserCreate(BaseTestCase):
    def test_user_create(self):
        """ Test for user registration """
        bootstrap = create_admin_user(self)
        with self.client:
            response = self.client.post(
                '/api/user/',
                data=json.dumps(dict(
                    email='joe@example.com',
                    username='test username',
                    group='adminGroup',
                    password='123456'
                )),
                headers=dict(
                    Authorization=bootstrap['authKey']
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertIn("status", data,
                          msg="response is : {}".format(response))
            self.assertTrue(data['status'] == 'success',
                            msg="data is : {}".format(data))
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_user_create_with_nonexistent_group(self):
        """ Test for user registration """
        # This should be failing, but is succeeding, as sqllite3 doesn't enforce foreign key constraints unles you tell it to every time
        # And I haven't worked out how to do that.
        bootstrap = create_admin_user(self)
        with self.client:
            response = self.client.post(
                '/api/user/',
                data=json.dumps(dict(
                    email='joe@example.com',
                    username='test username',
                    group='nonexistentgroup',
                    password='123456'
                )),
                headers=dict(
                    Authorization=bootstrap['authKey']
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertIn("status", data,
                          msg="response is : {}".format(data))
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] ==
                            'nonexistentgroup is not a valid group name', msg="data is : {}".format(data))
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

    def test_user_create_with_already_registered_user(self):
        """ Test registration with already registered email"""
        bootstrap = create_admin_user(self)
        with self.client:
            response = self.client.post(
                '/api/user/',
                data=json.dumps(dict(
                    email='admin@example.com',
                    username='admin',
                    group='adminGroup',
                    password='admin'
                )),
                headers=dict(
                    Authorization=bootstrap['authKey']
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'User already exists. Please Log in.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

    def test_user_create_without_valid_authKey(self):
        """ Test registration with already registered email"""
        bootstrap = create_admin_user(self)
        with self.client:
            response = self.client.post(
                '/api/user/',
                data=json.dumps(dict(
                    email='joe@example.com',
                    username='test username',
                    group='adminGroup',
                    password='123456'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'You must be logged in to do that.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)


class TestUserRead(BaseTestCase):
    def test_user_read(self):
        admin = create_admin_user(self)
        with self.client:
            response = self.client.get(
                '/api/user/{}'.format(admin['user'].id),
                headers=dict(
                    Authorization=admin['authKey']
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertIn('username', data, msg="data is : {}".format(data))
            self.assertIsNone(data['password'],
                              msg="We'd better not be leaking passwords")
            self.assertEqual(data['email'], 'admin@example.com')
            self.assertEqual(data['username'], 'admin',
                             msg="data is : {}".format(data))
            self.assertEqual(data['group'], 'adminGroup')
            self.assertEqual(data['isAdmin'], 'True')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_user_read_with_invalid_id(self):
        bootstrap = create_admin_user(self)
        with self.client:
            response = self.client.get(
                '/api/user/somebadid',
                headers=dict(
                    Authorization=bootstrap['authKey']
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404,
                             msg="response is : {}".format(response))
            self.assertEqual(
                data['message'], 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again. You have requested this URI [/api/user/somebadid] but did you mean /api/user/<public_id> ?', msg="data is : {}".format(data))
            self.assertTrue(response.content_type == 'application/json')

    def test_user_read_without_valid_authKey(self):
        admin = create_admin_user(self)
        with self.client:
            response = self.client.get(
                '/api/user/{}'.format(admin['user'].id),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401,
                             msg="response is : {}".format(response))

            self.assertIn('message', data, msg="data is : {}".format(data))
            self.assertEqual(
                data['message'], "You must be logged in to do that.")
            self.assertTrue(response.content_type == 'application/json')


class TestUserUpdate(BaseTestCase):
    def test_admin_user_update_self(self):
        admin = create_admin_user(self)
        with self.client:
            response = self.client.get(
                '/api/user/{}'.format(admin['user'].id),
                headers=dict(
                    Authorization=admin['authKey']
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('username', data, msg="data is : {}".format(data))
            self.assertEqual(data['email'], 'admin@example.com')
            self.assertEqual(data['username'], 'admin',
                             msg="data is : {}".format(data))
            self.assertEqual(data['group'], 'adminGroup')
            self.assertEqual(data['isAdmin'], 'True')
            self.assertTrue(response.content_type == 'application/json')

            patchResponse = self.client.patch(
                '/api/user/',
                headers={
                    'Authorization': admin['authKey']
                },
                data=json.dumps({
                    'id': admin['user'].id,
                    'username': "bob",
                    'email': "bob@bob.com",
                    'group': 'adminGroup',
                    'isAdmin': 'True',
                    'password': "newpassword"
                }),
                content_type='application/json'
            )
            data = json.loads(patchResponse.data.decode())
            self.assertEqual(patchResponse.status_code, 200,
                             msg="data is : {}".format(data))
            self.assertIn('username', data, msg="data is : {}".format(data))
            self.assertEqual(data['email'], 'bob@bob.com')
            self.assertEqual(data['username'], 'bob',
                             msg="data is : {}".format(data))
            self.assertEqual(data['group'], 'adminGroup')
            self.assertEqual(data['isAdmin'], 'True')
            self.assertIsNone(data['password'])
            self.assertTrue(response.content_type == 'application/json')

    def test_nonadmin_user_update_self(self):
        nonAdmin = create_nonadmin_user(self)
        with self.client:
            response = self.client.get(
                '/api/user/{}'.format(nonAdmin['user'].public_id),
                headers=dict(
                    Authorization=nonAdmin['authKey']
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('username', data, msg="data is : {}".format(data))
            self.assertEqual(data['email'], 'steve@steve.com')
            self.assertEqual(data['username'], 'steve',
                             msg="data is : {}".format(data))
            self.assertEqual(data['group'], 'adminGroup')
            self.assertEqual(data['isAdmin'], 'False')
            self.assertTrue(response.content_type == 'application/json')

            patchResponse = self.client.patch(
                '/api/user/',
                headers={
                    'Authorization': nonAdmin['authKey']
                },
                data=json.dumps({
                    'id': nonAdmin['user'].public_id,
                    'username': "bob",
                    'email': "bob@bob.com",
                    'group': 'adminGroup',
                    'isAdmin': 'False',
                    'password': "newpassword"
                }),
                content_type='application/json'
            )
            data = json.loads(patchResponse.data.decode())
            self.assertEqual(patchResponse.status_code, 200,
                             msg="data is : {}".format(data))
            self.assertIn('username', data, msg="data is : {}".format(data))
            self.assertEqual(data['email'], 'bob@bob.com')
            self.assertEqual(data['username'], 'bob',
                             msg="data is : {}".format(data))
            self.assertEqual(data['group'], 'adminGroup')
            self.assertEqual(data['isAdmin'], 'False')
            self.assertIsNone(data['password'])
            self.assertTrue(response.content_type == 'application/json')

    def test_admin_user_update_other(self):
        admin = create_admin_user(self)
        nonAdmin = create_nonadmin_user(self, groupId=admin['group'].id)

        with self.client:
            response = self.client.get(
                '/api/user/{}'.format(nonAdmin['user'].public_id),
                headers=dict(
                    Authorization=admin['authKey']
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('username', data, msg="data is : {}".format(data))
            self.assertEqual(data['email'], 'steve@steve.com')
            self.assertEqual(data['username'], 'steve',
                             msg="data is : {}".format(data))
            self.assertEqual(data['group'], 'adminGroup')
            self.assertEqual(data['isAdmin'], 'False')
            self.assertTrue(response.content_type == 'application/json')

            patchResponse = self.client.patch(
                '/api/user/',
                headers={
                    'Authorization': admin['authKey']
                },
                data=json.dumps({
                    'id': nonAdmin['user'].public_id,
                    'username': "bob",
                    'email': "bob@bob.com",
                    'group': 'adminGroup',
                    'isAdmin': 'False',
                    'password': "newpassword"
                }),
                content_type='application/json'
            )
            data = json.loads(patchResponse.data.decode())
            self.assertEqual(patchResponse.status_code, 200,
                             msg="data is : {}".format(data))
            self.assertIn('username', data, msg="data is : {}".format(data))
            self.assertEqual(data['email'], 'bob@bob.com')
            self.assertEqual(data['username'], 'bob',
                             msg="data is : {}".format(data))
            self.assertEqual(data['group'], 'adminGroup')
            self.assertEqual(data['isAdmin'], 'False')
            self.assertIsNone(data['password'])
            self.assertTrue(response.content_type == 'application/json')

    def test_nonadmin_user_update_other(self):
        admin = create_admin_user(self)
        nonAdmin = create_nonadmin_user(self, groupId=admin['group'].id)

        with self.client:
            response = self.client.get(
                '/api/user/{}'.format(admin['user'].public_id),
                headers=dict(
                    Authorization=admin['authKey']
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('username', data, msg="data is : {}".format(data))
            self.assertEqual(data['email'], 'admin@example.com')
            self.assertEqual(data['username'], 'admin',
                             msg="data is : {}".format(data))
            self.assertEqual(data['group'], 'adminGroup')
            self.assertEqual(data['isAdmin'], 'True')
            self.assertTrue(response.content_type == 'application/json')

            patchResponse = self.client.patch(
                '/api/user/',
                headers={
                    'Authorization': nonAdmin['authKey']
                },
                data=json.dumps({
                    'id': admin['user'].public_id,
                    'username': "bob",
                    'email': "bob@bob.com",
                    'group': 'adminGroup',
                    'isAdmin': 'False',
                    'password': "newpassword"
                }),
                content_type='application/json'
            )
            data = json.loads(patchResponse.data.decode())
            self.assertEqual(patchResponse.status_code, 403,
                             msg="data is : {}".format(data))
            self.assertEqual(
                data['message'], 'You do not have permission to update this user')
            self.assertTrue(response.content_type == 'application/json')

    def test_unloggedin_user_update_other(self):
        admin = create_admin_user(self)
        nonAdmin = create_nonadmin_user(self, groupId=admin['group'].id)

        with self.client:
            response = self.client.get(
                '/api/user/{}'.format(admin['user'].public_id),
                headers=dict(
                    Authorization=admin['authKey']
                ),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('username', data, msg="data is : {}".format(data))
            self.assertEqual(data['email'], 'admin@example.com')
            self.assertEqual(data['username'], 'admin',
                             msg="data is : {}".format(data))
            self.assertEqual(data['group'], 'adminGroup')
            self.assertEqual(data['isAdmin'], 'True')
            self.assertTrue(response.content_type == 'application/json')

            patchResponse = self.client.patch(
                '/api/user/',
                data=json.dumps({
                    'id': admin['user'].public_id,
                    'username': "bob",
                    'email': "bob@bob.com",
                    'group': 'adminGroup',
                    'isAdmin': 'False',
                    'password': "newpassword"
                }),
                content_type='application/json'
            )
            data = json.loads(patchResponse.data.decode())
            self.assertEqual(patchResponse.status_code, 401,
                             msg="data is : {}".format(data))
            self.assertEqual(data['status'], 'fail')
            self.assertEqual(
                data['message'], 'You must be logged in to do that.')
            self.assertTrue(response.content_type == 'application/json')
