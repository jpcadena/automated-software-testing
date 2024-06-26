"""
A module for password in the restful api.app.core.security package.
"""

from authlib.jose import JoseError, JWTClaims, jwt

from restful_api.app.config.config import Config
from restful_api.app.core.security.jwt import CustomJWTBearerTokenValidator
from restful_api.app.db.db import Session
from restful_api.app.models.user import User


def authenticate(username: str, password: str) -> User | None:
    """
    Authenticate a user by username and password.
    :param username: The username
    :type username: str
    :param password: The plaintext password
    :type password: str
    :return: The user if authentication is successful, None otherwise
    :rtype: User
    """
    session = Session()
    user: User | None = User.find_by_username(session, username)
    return user if user and user.check_password(password) else None


def identity(payload: JWTClaims) -> User | None:
    """
    Identify a user by their ID from the payload.
    :param payload: The JWT payload
    :type payload: JWTClaims
    :return: The user if found, None otherwise
    :rtype: User
    """
    user_id: int = payload["identity"]
    session = Session()
    return User.find_by_id(session, user_id)


def decode_token(token: str) -> User | None:
    """
    Decode the JWT token.
    :param token: The JWT token
    :type token: str
    :return: The payload if the token is valid, None otherwise
    :rtype: User
    """
    claims_options = {
        "iss": {"value": Config.HOST},
        "aud": {"value": "my-resource-server"},
    }
    validator = CustomJWTBearerTokenValidator(
        Config.HOST, Config.HOST, Config.HOST
    )
    try:
        payload = jwt.decode(
            token,
            Config.SECRET_KEY,
            claims_options=claims_options,
        )
        validator.authenticate_token(token)
        return identity(payload)
    except JoseError:
        return None
