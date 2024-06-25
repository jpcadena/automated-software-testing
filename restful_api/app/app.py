"""
A module for app in the restful_api package.
"""

from typing import Any

from authlib.integrations.base_client import UnsupportedTokenTypeError
from authlib.integrations.flask_client import OAuth
from authlib.jose import JoseError, JWTClaims
from authlib.oauth2 import ResourceProtector
from authlib.oauth2.rfc6749 import MissingAuthorizationError
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
    print(Config.HOST)
    validator: CustomJWTBearerTokenValidator = CustomJWTBearerTokenValidator(
        Config.HOST, "127.0.0.1", "127.0.0.1"
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
        token: str = encode_jwt(user.id, Config.HOST, Config.HOST)
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
    def check_oauth_token() -> Response | None:
        """
        Check the OAuth token before processing the request.
        Skip token validation for public routes.
        :return: A response object with an error message for missing auth.
        :rtype: Response | None
        """
        public_routes: list[str] = [
            "/user/register",
            "/",
            "/user/auth",
        ]
        path = request.path
        if path in public_routes:
            return None
        try:
            token: JWTClaims = resource_protector.validate_request(
                scopes=None, request=request
            )
            g.token = token
            print(f"Token claims: {token}")  # Debugging line
        except MissingAuthorizationError as e:
            print(f"MissingAuthorizationError: {e}")
            return generate_response(
                {"message": "Authorization header is missing or invalid"}, 401
            )
        except UnsupportedTokenTypeError as e:
            print(f"UnsupportedTokenTypeError: {e}")
            return generate_response(
                {"message": "Token type is not supported"}, 401
            )
        except JoseError as e:
            print(f"JoseError: {e}")
            return generate_response(
                {"message": "Could not authorize. Invalid token."}, 401
            )
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return generate_response(
                {
                    "message": "An unexpected error occurred during"
                    " authorization"
                },
                500,
            )
        return None

    return flask
