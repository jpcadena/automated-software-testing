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

    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    USE_RELOADER: bool = os.getenv("USE_RELOADER", "false").lower() == "true"
    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///data.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
