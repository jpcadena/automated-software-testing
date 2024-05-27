"""
A module for item in the restful_api-resources package.
"""

from typing import Any

from flask import Response, jsonify, make_response, request
from sqlalchemy.exc import SQLAlchemyError

from ..db.db import Session
from ..models.item import Item


def get_item(name: str) -> Response:
    """
    Retrieve an item by name.
    :param name: The name of the item to retrieve.
    :type name: str
    :return: JSON response containing the item data or an error message.
    :rtype: Response
    """
    session = Session()
    if item := Item.find_by_name(session, name):
        response: Response = make_response(jsonify(item.json()), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    return make_response(jsonify({"message": "Item not found"}), 404)


def post_item(name: str) -> Response:
    """
    Create a new item.
    :param name: The name of the item to create.
    :type name: str
    :return: JSON response containing the created item data or an error message.
    :rtype: Response
    """
    session = Session()
    response: Response
    if Item.find_by_name(session, name):
        response = make_response(
            jsonify({"message": f"An item with name '{name}' already exists."}),
            400,
        )
        response.headers["Content-Type"] = "application/json"
        return response
    data: dict[str, Any] = request.get_json()
    item: Item = Item(name, **data)
    try:
        item.save_to_db(session)
    except SQLAlchemyError as e:
        session.rollback()
        response = make_response(
            jsonify(
                {"message": f"An error occurred inserting the item: {str(e)}"}
            ),
            500,
        )
        response.headers["Content-Type"] = "application/json"
        return response
    response = make_response(jsonify(item.json()), 201)
    response.headers["Content-Type"] = "application/json"
    return response


def delete_item(name: str) -> Response:
    """
    Delete an item by name.
    :param name: The name of the item to delete.
    :type name: str
    :return: JSON response containing a success or error message.
    :rtype: Response
    """
    session = Session()
    if item := Item.find_by_name(session, name):
        item.delete_from_db(session)
        response: Response = make_response(
            jsonify({"message": "Item deleted"}), 200
        )
        response.headers["Content-Type"] = "application/json"
        return response
    return make_response(jsonify({"message": "Item not found"}), 404)


def put_item(name: str) -> Response:
    """
    Update an existing item or create a new one if it doesn't exist.
    :param name: The name of the item to update or create.
    :type name: str
    :return: JSON response containing the updated or created item data.
    :rtype: Response
    """
    session = Session()
    data: dict[str, Any] = request.get_json()
    item: Item | None = Item.find_by_name(session, name)
    if item is None:
        item = Item(name, **data)
    else:
        item.price = data["price"]
    item.save_to_db(session)
    response: Response = make_response(jsonify(item.json()), 200)
    response.headers["Content-Type"] = "application/json"
    return response


def get_items() -> Response:
    """
    Retrieve all items.
    :return: JSON response containing a list of all items.
    :rtype: Response
    """
    session = Session()
    items: list[Item] = session.query(Item).all()
    response: Response = make_response(
        jsonify({"items": [item.json() for item in items]}), 200
    )
    response.headers["Content-Type"] = "application/json"
    return response
