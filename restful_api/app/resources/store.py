"""
A module for store in the restful api.app.resources package.
"""

from flask import Response
from sqlalchemy.exc import SQLAlchemyError

from ..core.utils import generate_response
from ..db.db import Session
from ..models.store import Store


def get_store(name: str) -> Response:
    """
    Retrieve a store by name.
    :param name: The name of the store to retrieve.
    :type name: str
    :return: JSON response containing the store data or an error message.
    :rtype: Response
    """
    session = Session()
    if store := Store.find_by_name(session, name):
        return generate_response(store.json(), 200)
    return generate_response({"message": "Store not found"}, 404)


def post_store(name: str) -> Response:
    """
    Create a new store.
    :param name: The name of the store to create.
    :type name: str
    :return: JSON response containing the created store data or an error
    message.
    :rtype: Response
    """
    session = Session()
    if Store.find_by_name(session, name):
        return generate_response(
            {"message": f"A store with name '{name}' already exists."}, 400
        )
    store = Store(name)
    try:
        store.save_to_db(session)
        return generate_response(store.json(), 201)
    except SQLAlchemyError as e:
        session.rollback()
        return generate_response(
            {"message": f"An error occurred inserting the store: {str(e)}"}, 500
        )


def delete_store(name: str) -> Response:
    """
    Delete a store by name.
    :param name: The name of the store to delete.
    :type name: str
    :return: JSON response containing a success or error message.
    :rtype: Response
    """
    session = Session()
    if store := Store.find_by_name(session, name):
        store.delete_from_db(session)
        return generate_response({"message": "Store deleted"}, 200)
    return generate_response({"message": "Store not found"}, 404)


def get_stores() -> Response:
    """
    Retrieve all stores.
    :return: JSON response containing a list of all stores.
    :rtype: Response
    """
    session = Session()
    stores: list[Store] = session.query(Store).all()
    return generate_response(
        {"stores": [store.json() for store in stores]}, 200
    )
