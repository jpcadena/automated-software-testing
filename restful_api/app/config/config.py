"""
A module for config in the restful_api.config package.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class
    """

    HOST: str = os.environ.get("HOST", "localhost")
    PORT: int = int(os.environ.get("PORT", 5000))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    USE_RELOADER: bool = os.getenv("USE_RELOADER", "false").lower() == "true"
    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///data.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")
    OAUTH2_PROVIDER_TOKEN_EXPIRES_IN: int = int(
        os.getenv("OAUTH2_PROVIDER_TOKEN_EXPIRES_IN", "3600")
    )
