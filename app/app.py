"""
Flask main app.
"""

import os

from flask import Flask, Response, jsonify, send_from_directory

from restful_api.app.config.config import Config

app: Flask = Flask(__name__)


@app.route("/")
def home() -> Response:
    """
    Home endpoint function
    :return: Message object
    :rtype: Response
    """
    return jsonify(
        {
            "message": "Hello, World!",
        }
    )


@app.route("/favicon.ico")
def favicon() -> Response:
    """
    The favicon path operation
    :return: Redirect to favicon directory
    :rtype: Response
    """
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    app.run(
        debug=Config.DEBUG,
        use_reloader=Config.USE_RELOADER,
    )
