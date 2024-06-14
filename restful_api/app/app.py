"""
A module for app in the restful_api package.
"""

from typing import Any

from authlib.integrations.flask_client import OAuth
from authlib.jose import JWTClaims, JoseError
from authlib.oauth2 import ResourceProtector
from flask import Flask, Response, g, request

from restful_api.app.api.router.item import register_item
from restful_api.app.api.router.store import register_store
from restful_api.app.api.router.user import register_user
from restful_api.app.config.config import Config
from restful_api.app.core.security.jwt import CustomJWTBearerTokenValidator
from restful_api.app.core.security.password import authenticate
from restful_api.app.core.utils import encode_jwt, generate_response
from restful_api.app.db.db import init_db
from restful_api.app.models.user import User


def create_app() -> Flask:
    """
    Create a new Flask application
    :return: The new Flask instance
    :rtype: Flask
    """
    flask: Flask = Flask(__name__)
    flask.config.from_object(Config)
    init_db(flask)
    register_item(flask)
    register_store(flask)
    register_user(flask)
    oauth: OAuth = OAuth(flask)
    resource_protector: ResourceProtector = ResourceProtector()
    validator: CustomJWTBearerTokenValidator = CustomJWTBearerTokenValidator(
        Config.HOST, "my-resource-server"
    )
    resource_protector.register_token_validator(validator)

    @flask.route("/user/auth", methods=["POST"])
    def auth() -> Response:
        """
        Authenticate a user and return a JWT token.
        :return: A response object containing the JWT token or an error message.
        :rtype: Response
        """
        data: dict[str, Any] | None = request.json
        if data is None:
            return generate_response({"message": "Invalid JSON payload"}, 400)
        username: str | None = data.get("username")
        password: str | None = data.get("password")
        if not username or not password:
            return generate_response(
                {"message": "Username and password required"}, 400
            )
        user: User | None = authenticate(username, password)
        if not user:
            return generate_response({"message": "Invalid credentials"}, 401)
        token: str = encode_jwt(user.id)
        return generate_response({"access_token": token}, 200)

    @flask.errorhandler(JoseError)
    def auth_error(err: JoseError) -> Response:
        """
        Handle JWT authentication errors.
        :param err: The JoseError instance.
        :type err: JoseError
        :return: A response object with an error message.
        :rtype: Response
        """
        return generate_response(
            {
                "message": "Could not authorize. Did you include a valid"
                " Authorization header?"
            },
            401,
        )

    @flask.before_request
    def check_oauth_token() -> None:
        """
        Check the OAuth token before processing the request.
        :return: None
        :rtype: NoneType
        """
        token: JWTClaims = resource_protector.validate_request(
            scopes=None, request=request
        )
        g.token = token

    return flask
