"""
A module for test base in the app.tests.system package.
"""

import unittest

from flask.testing import FlaskClient

from app.app import app


class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up the test base module
        :return: None
        :rtype: NoneType
        """
        app.testing = True
        self.flask_client: FlaskClient = app.test_client()
