"""
A module for store in the restful api.app.resources package.
"""

from typing import Any

from flask import Response, jsonify, make_response, request
from sqlalchemy.exc import SQLAlchemyError

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
    store = Store.find_by_name(session, name)
    print(type(store))
    if store:
        response: Response = make_response(jsonify(store.json()), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    return make_response(jsonify({"message": "Store not found"}), 404)


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
    response: Response
    if Store.find_by_name(session, name):
        response = make_response(
            jsonify(
                {"message": f"A store with name '{name}' already " f"exists."}
            ),
            400,
        )
        response.headers["Content-Type"] = "application/json"
        return response
    data: dict[str, Any] = request.get_json()
    store = Store(name, **data)
    print(type(store))
    try:
        store.save_to_db(session)
    except SQLAlchemyError as e:
        session.rollback()
        response = make_response(
            jsonify(
                {"message": f"An error occurred inserting the store: {str(e)}"}
            ),
            500,
        )
        response.headers["Content-Type"] = "application/json"
        return response
    response = make_response(jsonify(store.json()), 201)
    response.headers["Content-Type"] = "application/json"
    return response


def delete_store(name: str) -> Response:
    """
    Delete a store by name.
    :param name: The name of the store to delete.
    :type name: str
    :return: JSON response containing a success or error message.
    :rtype: Response
    """
    session = Session()
    store = Store.find_by_name(session, name)
    print(type(store))
    if store:
        store.delete_from_db(session)
        response: Response = make_response(
            jsonify({"message": "Store deleted"}), 200
        )
        response.headers["Content-Type"] = "application/json"
        return response
    return make_response(jsonify({"message": "Store not found"}), 404)


def get_stores() -> Response:
    """
    Retrieve all stores.
    :return: JSON response containing a list of all stores.
    :rtype: Response
    """
    session = Session()
    stores: list[Store] = session.query(Store).all()
    response: Response = make_response(
        jsonify({"stores": [store.json() for store in stores]}), 200
    )
    response.headers["Content-Type"] = "application/json"
    return response
