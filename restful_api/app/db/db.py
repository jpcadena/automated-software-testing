"""
A module for db in the restful_api.db package.
"""

from typing import Type

from flask import Flask
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    declarative_base,
    scoped_session,
    sessionmaker,
)

from ..config.config import Config

engine: Engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
    future=True,
)
Session = scoped_session(sessionmaker(bind=engine))
Base: Type[DeclarativeBase] = declarative_base()


def init_db(app: Flask) -> None:
    """
    Initialize the database connection and its tables
    :param app: The Flask application
    :type app: Flask
    :return: None
    :rtype: NoneType
    """
    with app.app_context():
        if app.config["DEBUG"]:
            Base.metadata.create_all(engine)
