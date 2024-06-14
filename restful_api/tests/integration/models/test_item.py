"""
A module for test item in the restful api.tests.integration.models package.
"""

from typing import Any

from werkzeug.test import TestResponse

from restful_api.app.core.utils import encode_jwt
from restful_api.app.db.db import Session
from restful_api.app.models.item import Item
from restful_api.app.models.store import Store
from restful_api.tests.test_base import BaseTest


class ItemTest(BaseTest):
    def get_token(self) -> str:
        return encode_jwt(identity=1)

    def create_item_get_token(self, store: Store, session: Any) -> str:
        item: Item = Item(name="test_item", price=2.99, store_id=store.id)
        item.save_to_db(session)
        return self.get_token()

    def test_create_item(self) -> None:
        """
        Test the creation of an item
        :return: None
        :rtype: NoneType
        """
        session = Session()
        store: Store = Store(name="test_store")
        store.save_to_db(session)
        token: str = self.create_item_get_token(store, session)
        test_response: TestResponse = self.app.post(
            "/item/test_item",
            json={
                "price": 10.99,
                "store_id": 1,
            },
            headers={"Authorization": f"Bearer {token}"},
        )
        self.assertEqual(test_response.status_code, 201)
        self.assertEqual(
            test_response.json,
            {
                "name": "test_item",
                "price": 10.99,
                "store_id": 1,
            },
        )

    def test_get_item(self) -> None:
        """
        Test retrieving an item
        :return: None
        :rtype: NoneType
        """
        session = Session()
        store: Store = Store(name="test_store")
        store.save_to_db(session)
        token: str = self.create_item_get_token(store, session)
        self.app.post(
            "/item/test_item",
            json={
                "price": 10.99,
                "store_id": 1,
            },
            headers={"Authorization": f"Bearer {token}"},
        )
        test_response: TestResponse = self.app.get(
            "/item/test_item",
            headers={"Authorization": f"Bearer {token}"},
        )
        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(
            test_response.json,
            {
                "name": "test_item",
                "price": 10.99,
                "store_id": 1,
            },
        )

    def test_delete_item(self) -> None:
        """
        Test deleting an item
        :return: None
        :rtype: NoneType
        """
        session = Session()
        store: Store = Store(name="test_store")
        store.save_to_db(session)
        token: str = self.create_item_get_token(store, session)
        self.app.post(
            "/item/test_item",
            json={
                "price": 10.99,
                "store_id": 1,
            },
            headers={"Authorization": f"Bearer {token}"},
        )
        test_response: TestResponse = self.app.delete(
            "/item/test_item",
            headers={"Authorization": f"Bearer {token}"},
        )
        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(test_response.json, {"message": "Item deleted"})
        test_response = self.app.get(
            "/item/test_item",
            headers={"Authorization": f"Bearer {token}"},
        )
        self.assertEqual(test_response.status_code, 404)
        self.assertEqual(test_response.json, {"message": "Item not found"})

    def test_update_item(self) -> None:
        """
        Test updating an item
        :return: None
        :rtype: NoneType
        """
        session = Session()
        store: Store = Store(name="test_store")
        store.save_to_db(session)
        token: str = self.create_item_get_token(store, session)
        self.app.post(
            "/item/test_item",
            json={
                "price": 10.99,
                "store_id": 1,
            },
            headers={"Authorization": f"Bearer {token}"},
        )
        test_response: TestResponse = self.app.put(
            "/item/test_item",
            json={
                "price": 15.99,
                "store_id": 1,
            },
            headers={"Authorization": f"Bearer {token}"},
        )
        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(
            test_response.json,
            {
                "name": "test_item",
                "price": 15.99,
                "store_id": 2,
            },
        )

    def test_store_relationship(self) -> None:
        session = Session()
        with self.app_context:
            store: Store = Store("Test Store")
            item: Item = Item("test", 19.99, 1)
            store.save_to_db(session)
            item.save_to_db(session)
            self.assertEqual(item.store.name, "Test Store")
