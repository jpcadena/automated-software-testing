"""
A module for jwt in the restful_api.app.core.security package.
"""

from authlib.jose import JWTClaims, JoseError, JsonWebToken
from authlib.oauth2.rfc9068 import JWTBearerTokenValidator

from restful_api.app.config.config import Config


class CustomJWTBearerTokenValidator(JWTBearerTokenValidator):  # type: ignore
    def __init__(self, issuer: str, resource_server: str, audience: str):
        super().__init__(issuer, resource_server)
        self.issuer: str = issuer
        self.audience: str = audience

    def authenticate_token(self, token_string: str) -> JWTClaims:
        json_web_token: JsonWebToken = JsonWebToken(["HS256"])
        try:
            print(f"Decoding token: {token_string}")
            claims: JWTClaims = json_web_token.decode(
                token_string, Config.SECRET_KEY
            )
            print(f"Decoded claims: {claims}")
            if claims.get("iss") != self.issuer:
                print(
                    f"Invalid issuer: expected {self.issuer}, got {claims.get('iss')}"
                )
                raise JoseError(
                    f"Invalid issuer: expected {self.issuer}, got {claims.get('iss')}"
                )

            if claims.get("aud") != self.audience:
                print(
                    f"Invalid audience: expected {self.audience}, got {claims.get('aud')}"
                )
                raise JoseError(
                    f"Invalid audience: expected {self.audience}, got {claims.get('aud')}"
                )
            claims.validate()
            print("Token validated successfully")
            return claims
        except JoseError as e:
            print(f"Token validation error: {e}")
            raise e
