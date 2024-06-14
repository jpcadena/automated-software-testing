"""
A module for test user in the restful api.tests.unit.models package.
"""

from unittest import TestCase

from restful_api.app.models.user import User


class UserTest(TestCase):
    def test_create_user(self) -> None:
        user: User = User("test", "P@$5w0Rd.")
        self.assertEqual(
            user.username,
            "test",
            "The username of the user after creation does not equal the"
            " constructor argument.",
        )
        self.assertEqual(
            user.password,
            "P@$5w0Rd.",
            "The password of the user after creation does not equal the"
            " constructor argument.",
        )
