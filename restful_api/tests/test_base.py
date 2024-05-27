"""
A module for test base in the restful api-tests package.
This class should be the parent class of each non-unit test.
It allows for instantiation of the database dynamically and makes sure that
it is a new, blank database each time.
"""

from unittest import TestCase

from restful_api.app.db import db
from restful_api.app.db.db import Base, Session, engine
from restful_api.app.models.store import Store
from restful_api.run import app


class BaseTest(TestCase):
    def setUp(self) -> None:
        """
        Set up the test base module
        :return: None
        :rtype: NoneType
        """
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            "postgresql://postgres:1234@localhost:5432/test"
        )
        app.config["TESTING"] = True
        # SQLite does not support Foreign keys
        with app.app_context():
            db.init_db(app)
            session = Session()
            store: Store = Store(name="Test Store")
            session.add(store)
            session.commit()
        self.app = app.test_client()
        self.app_context = app.app_context()

    def tearDown(self) -> None:
        """
        Tear down the database connection
        :return: None
        :rtype: NoneType
        """
        with app.app_context():
            Session.remove()
            Base.metadata.drop_all(bind=engine)
