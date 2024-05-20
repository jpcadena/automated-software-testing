"""
A module for test home in the app.tests.system package.
"""

import json

from werkzeug.test import TestResponse

from app.tests.system.test_base import TestBase


class TestHome(TestBase):
    def test_home(self) -> None:
        with self.flask_client:
            test_response: TestResponse = self.flask_client.get("/")
            self.assertEqual(test_response.status_code, 200)
            self.assertEqual(
                json.loads(test_response.get_data()),
                {
                    "message": "Hello, World!",
                },
            )
