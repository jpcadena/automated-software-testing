"""
A module for test user in the restful api.tests.integration.models package.
"""

from restful_api.app.db.db import Session
from restful_api.app.models.user import User
from restful_api.tests.test_base import BaseTest


class UserTest(BaseTest):
    def test_crud(self) -> None:
        """
        Test CRUD operations for User
        :return: None
        :rtype: NoneType
        """
        with self.app_context:
            user: User = User("test", "P@$5w0Rd.")
            session = Session()
            self.assertIsNone(User.find_by_username(session, "test"))
            self.assertIsNone(User.find_by_id(session, 1))
            user.save_to_db(session)
            self.assertIsNotNone(User.find_by_username(session, "test"))
            self.assertIsNotNone(User.find_by_id(session, 1))
