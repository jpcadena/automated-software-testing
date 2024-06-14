"""
A module for user in the restful api.app.api.router package.
"""

from flask import Flask

from restful_api.app.resources.user import post_user


def register_user(app: Flask) -> None:
    """
    Register routes to the RESTful API
    :param app: The Flask application
    :type app: Flask
    :return: None
    :rtype: NoneType
    """
    app.add_url_rule("/user/register", "register", post_user, methods=["POST"])
