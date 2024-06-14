"""
A module for utility functions in the restful_api.app.core package.
"""

from typing import Any

from authlib.jose import jwt
from flask import Response, jsonify, make_response

from restful_api.app.config.config import Config


def generate_response(message: dict[str, Any], status_code: int) -> Response:
    """
    Generate a JSON response with the given message and status code.
    :param message: The message to include in the response.
    :type message: dict[str, Any]
    :param status_code: The HTTP status code for the response.
    :type status_code: int
    :return: The generated response object.
    :rtype: Response
    """
    response: Response = make_response(jsonify(message), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


def encode_jwt(identity: int) -> str:
    """
    Encode a JWT token with the given identity.
    :param identity: The user identity to include in the token.
    :type identity: int
    :return: The encoded JWT token.
    :rtype: str
    """
    header: dict[str, str] = {"alg": "HS256"}
    payload: dict[str, int] = {"identity": identity}
    token: bytes = jwt.encode(header, payload, Config.SECRET_KEY)
    return token.decode()
