"""
A module for test user in the restful api.tests.system package.
"""

from typing import Any

from flask.testing import FlaskClient
from werkzeug.test import TestResponse

from restful_api.app.core.utils import encode_jwt
from restful_api.tests.system.base_test import BaseTest


class UserTest(BaseTest):
    def get_token(self) -> str:
        return encode_jwt(identity=1)

    def test_register_user(self) -> None:
        """
        Test registration for User
        :return: None
        :rtype: NoneType
        """
        with self.app() as client:
            with self.app_context():
                token = self.get_token()
                test_response: TestResponse = client.post(
                    "/user/register",
                    json={  # form data
                        "username": "test",
                        "password": "P@$5w0Rd.",
                    },
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {token}",
                    },
                )
                self.assertEqual(test_response.status_code, 201)

    def test_register_duplicate_user(self) -> None:
        """
        Test registration of a duplicate user.
        :return: None
        :rtype: NoneType
        """
        with self.app() as client:
            with self.app_context():
                token = self.get_token()
                test_response = self.register_validate(
                    client, "/user/register", 400, token
                )

    def test_register_and_login(self) -> None:
        """
        Test registration and login for User
        :return: None
        :rtype: NoneType
        """
        with self.app() as client:
            with self.app_context():
                token: str = self.get_token()
                register_response: TestResponse = client.post(
                    "/user/register",
                    json={
                        "username": "test",
                        "password": "P@$5w0Rd.",
                    },
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {token}",
                    },
                )
                self.assertEqual(register_response.status_code, 201)
                login_response: TestResponse = client.post(
                    "/user/login",
                    json={
                        "username": "test",
                        "password": "P@$5w0Rd.",
                    },
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {token}",
                    },
                )
                self.assertEqual(login_response.status_code, 200)
                json_data: dict[str, Any] = login_response.json
                self.assertIn("access_token", json_data)

    def register_validate(
        self, client: FlaskClient, endpoint: str, status_code: int, token: str
    ) -> TestResponse:
        client.post(
            "/user/register",
            json={"username": "test", "password": "P@$5w0Rd."},
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
        )
        result: TestResponse = client.post(
            endpoint,
            json={"username": "test", "password": "P@$5w0Rd."},
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
        )
        self.assertEqual(result.status_code, status_code)
        return result

    def test_user_not_found(self) -> None:
        """
        Test login for a non-existent User
        :return: None
        :rtype: NoneType
        """
        with self.app() as client:
            token = self.get_token()
            test_response: TestResponse = client.post(
                "/user/login",
                json={
                    "username": "nonexistent",
                    "password": "P@$5w0Rd.",
                },
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}",
                },
            )
            self.assertEqual(test_response.status_code, 404)
