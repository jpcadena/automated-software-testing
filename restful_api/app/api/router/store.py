"""
A module for store in the restful api.app.api.router package.
"""

from flask import Flask

from restful_api.app.resources.store import (
    delete_store,
    get_store,
    get_stores,
    post_store,
)


def register_routes(app: Flask) -> None:
    """
    Register routes to the RESTful API
    :param app: The Flask application
    :type app: Flask
    :return: None
    :rtype: NoneType
    """
    app.add_url_rule(
        "/store/<string:name>", "get_store", get_store, methods=["GET"]
    )
    app.add_url_rule(
        "/store/<string:name>", "post_store", post_store, methods=["POST"]
    )
    app.add_url_rule(
        "/store/<string:name>", "delete_store", delete_store, methods=["DELETE"]
    )
    app.add_url_rule("/stores", "get_stores", get_stores, methods=["GET"])
