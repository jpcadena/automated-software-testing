"""
A module for item in the restful_api.api.router package.
"""

from flask import Flask

from restful_api.app.resources.item import (
    delete_item,
    get_item,
    get_items,
    post_item,
    put_item,
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
        "/item/<string:name>", "get_item", get_item, methods=["GET"]
    )
    app.add_url_rule(
        "/item/<string:name>", "post_item", post_item, methods=["POST"]
    )
    app.add_url_rule(
        "/item/<string:name>", "delete_item", delete_item, methods=["DELETE"]
    )
    app.add_url_rule(
        "/item/<string:name>", "put_item", put_item, methods=["PUT"]
    )
    app.add_url_rule("/items", "get_items", get_items, methods=["GET"])
