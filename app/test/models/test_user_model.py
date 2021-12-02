import unittest

import datetime

from app.main import db
from app.main.model.user import User
from app.test.base import BaseTestCase

import jwt


class TestUserModel(BaseTestCase):
    def test_can_create_User_instance(self):
        user = User(
            email='test@test.com',
            password='test',
            group_id='testGroup',
            registered_on=datetime.datetime.utcnow()
        )
        self.assertTrue(isinstance(user, User))

    def test_jwt_coding_actually_works(self):
        payload = {"key": "test"}
        key = "secret"
        encoded = jwt.encode(
            payload,
            key,
            algorithm='HS256'
        )
        decoded = jwt.decode(
            encoded,
            key,
            algorithms='HS256'
        )
        self.assertEqual(payload, decoded)

    def test_basic_token_actions(self):
        auth_token = User.encode_auth_token(10)

        self.assertTrue(isinstance(auth_token, str))

        decoded = User.decode_auth_token(auth_token)

        self.assertEqual(decoded, 10)

    def test_encode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test',
            group_id='testGroup',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, str))

    def test_decode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test',
            group_id='testGroup',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, str))
        self.assertEqual(User.decode_auth_token(auth_token), user.id)


if __name__ == '__main__':
    unittest.main()
