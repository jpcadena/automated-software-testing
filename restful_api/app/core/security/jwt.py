"""
A module for jwt in the restful_api.app.core.security package.
"""

from authlib.jose import JWTClaims, JsonWebToken
from authlib.oauth2.rfc9068 import JWTBearerTokenValidator

from restful_api.app.config.config import Config


class CustomJWTBearerTokenValidator(JWTBearerTokenValidator):  # type: ignore
    def __init__(self, issuer: str, resource_server: str):
        super().__init__(issuer, resource_server)

    def authenticate_token(self, token_string: str) -> JWTClaims:
        json_web_token: JsonWebToken = JsonWebToken(["HS256"])
        claims: JWTClaims = json_web_token.decode(
            token_string, Config.SECRET_KEY
        )
        claims.validate()
        return claims
