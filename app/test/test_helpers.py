import unittest

from app.main import db
from app.main.model.blacklist import BlacklistToken
import json
from app.test.base import BaseTestCase
from app.test.helpers import create_group, create_admin_user, create_nonadmin_user, get_admin_authKey, get_nonadmin_authKey


class TestHelpers(BaseTestCase):

    def test_create_group(self):
        """ Test for direct creation of groups into the database """
        create_group(self)

    def test_create_admin_user(self):
        """ Test for direct creation of admin user into the database """
        create_admin_user(self)

    def test_create_nonadmin_user(self):
        """ Test for direct creation of nonadmin user into the database """
        create_admin_user(self)

    def test_get_admin_authKey(self):
        """ Test for creation of an admin user, and then logging it in"""
        get_admin_authKey(self)

    def test_get_nonadmin_authKey(self):
        """ Test for creation of an nonadmin user, and then logging it in"""
        get_nonadmin_authKey(self)


if __name__ == '__main__':
    unittest.main()
