"""
A module for base test in the restful api.tests.system package.
"""

from unittest import TestCase

from restful_api.app.db import db
from restful_api.app.db.db import Base, Session, engine
from restful_api.run import app


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up the base class for tests
        :return: None
        :rtype: NoneType
        """
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            "postgresql://postgres:1234@127.0.0.1:5432/test"
        )
        app.config["DEBUG"] = True
        with app.app_context():
            Base.metadata.create_all(bind=engine)

    def setUp(self) -> None:
        """
        Set up the test base module
        :return: None
        :rtype: NoneType
        """
        with app.app_context():
            db.init_db(app)
            Base.metadata.create_all(bind=engine)  # Ensure tables are created
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self) -> None:
        """
        Tear down the database connection
        :return: None
        :rtype: NoneType
        """
        with app.app_context():
            Session.remove()
            Base.metadata.drop_all(bind=engine)
