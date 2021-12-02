import unittest

from app.main import db
from app.main.model.blacklist import BlacklistToken
import json
from app.test.base import BaseTestCase
from app.test.helpers import create_admin_user, get_admin_authKey, get_nonadmin_authKey, admin_email, admin_password


class TestAuthLogin(BaseTestCase):

    def test_login_registered_user(self):
        """ Test for login of registered-user login """
        with self.client:
            # user registration
            bootstrap = create_admin_user(self)
            # registered user login
            response = self.client.post(
                '/api/auth/login',
                data=json.dumps(dict(
                    email=admin_email,
                    password=admin_password
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success',
                            msg="Login response is : %s" % data)
            self.assertTrue(data['message'] == 'Successfully logged in.')
            self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_login_nonexistent_user(self):
        """ Test for login of non-registered user """
        with self.client:
            response = self.client.post(
                '/api/auth/login',
                data=json.dumps(dict(
                    email='admin@example.com',
                    password='admin'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            print(data['message'])
            self.assertTrue(data['message'] ==
                            'email or password does not match.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)

    def test_login_bad_password(self):
        """ Test for login of registered user with the wrong password"""
        bootstrap = create_admin_user(self)
        with self.client:
            response = self.client.post(
                '/api/auth/login',
                data=json.dumps(dict(
                    email=admin_email,
                    password='badpassword'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            print(data['message'])
            self.assertTrue(data['message'] ==
                            'email or password does not match.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)


class TestAuthLogout(BaseTestCase):
    def test_valid_logout(self):
        """ Test for logout before token expires """
        with self.client:
            bootstrap = create_admin_user(self)
            # registered user login
            loginResponse = self.client.post(
                '/api/auth/login',
                data=json.dumps(dict(
                    email=admin_email,
                    password=admin_password
                )),
                content_type='application/json'
            )
            responseData = json.loads(loginResponse.data.decode())

            if 'Authorization' not in responseData:
                raise Exception(
                    f'responseData missing Authorization: {responseData}')
            # valid token logout
            response = self.client.post(
                '/api/auth/logout',
                headers=dict(
                    Authorization=responseData['Authorization']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged out.')
            self.assertEqual(response.status_code, 200)

    def test_valid_blacklisted_token_logout(self):
        """ Test for logout after a valid token gets blacklisted """
        with self.client:
            authKey = get_nonadmin_authKey(self)
            # blacklist a valid token
            blacklist_token = BlacklistToken(
                token=authKey)
            db.session.add(blacklist_token)
            db.session.commit()
            # blacklisted valid token logout
            response = self.client.post(
                '/api/auth/logout',
                headers=dict(
                    Authorization=authKey
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] ==
                            'Token blacklisted. Please log in again.')
            self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
