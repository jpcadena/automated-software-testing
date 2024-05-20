"""
A module for app in the restful_api package.
"""

from flask import Flask

from restful_api.app.api.router.item import register_routes
from restful_api.app.config.config import Config
from restful_api.app.db.db import init_db


def create_app() -> Flask:
    """
    Create a new Flask application
    :return: The new Flask instance
    :rtype: Flask
    """
    flask: Flask = Flask(__name__)
    flask.config.from_object(Config)
    init_db(flask)
    register_routes(flask)
    return flask
