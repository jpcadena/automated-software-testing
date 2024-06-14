"""
A module for user in the restful api.app.resources package.
"""

from typing import Any

from flask import Response, request

from ..core.utils import generate_response
from ..db.db import Session
from ..models.user import User


def post_user() -> Response:
    """
    Create a new user.
    :return: JSON response containing the created user data or an error message.
    :rtype: Response
    """
    data: dict[str, Any] = request.get_json()
    username: str | None = data.get("username")
    password: str | None = data.get("password")
    if not username or not password:
        return generate_response(
            {"message": "Username and password are required"}, 400
        )
    session = Session()
    if User.find_by_username(session, username):
        return generate_response({"message": "User already exists"}, 400)
    new_user: User = User(username=username, password=password)
    new_user.save_to_db(session)
    return generate_response({"message": "User created successfully."}, 201)
