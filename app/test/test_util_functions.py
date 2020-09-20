import unittest
import datetime

from app.main import db
from app.test.base import BaseTestCase

import app.main.util.utilFunctions as utilFunctions


class TestStartOfLocalDay(BaseTestCase):
    def test_startOfLocalDay_returns_correct_value(self):
        testDate = datetime.datetime(
            year=2008, month=3, day=24, hour=14, minute=34, second=3, microsecond=49358)

        result = utilFunctions.startOfLocalDay(testDate)

        self.assertTrue(isinstance(result, datetime.datetime))
        self.assertEquals(result.ctime(), "Mon Mar 24 00:00:00 2008")


class TestEndOfLocalDay(BaseTestCase):
    def test_startOfLocalDay_returns_correct_value(self):
        testDate = datetime.datetime(
            year=2008, month=3, day=24, hour=14, minute=34, second=3, microsecond=49358)

        result = utilFunctions.endOfLocalDay(testDate)

        self.assertTrue(isinstance(result, datetime.datetime))
        self.assertEquals(result.ctime(), "Mon Mar 24 23:59:59 2008")


if __name__ == '__main__':
    unittest.main()
