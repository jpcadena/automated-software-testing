"""
Flask main app.
"""

from flask import Flask

app: Flask = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    """
    Home endpoint function
    :return: Message object
    :rtype: str
    """
    return "Hello World!"


if __name__ == "__main__":
    app.run()
