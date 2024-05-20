"""
A module for run in the restful_api package.
"""

from flask import Flask

from restful_api.app.app import create_app
from restful_api.app.config.config import Config

app: Flask = create_app()

if __name__ == "__main__":
    app.run(
        debug=Config.DEBUG,
        use_reloader=Config.USE_RELOADER,
    )
