"""
A module for test store in the restful api.tests.integration.models package.
"""

from typing import Any

from restful_api.app.db.db import Session
from restful_api.app.models.item import Item
from restful_api.app.models.store import Store
from restful_api.tests.test_base import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_emtpy(self) -> None:
        """
        Test the creation of a store items as empty list
        :return: None
        :rtype: NoneType
        """
        store: Store = Store("test")
        self.assertListEqual(
            store.items.all(),  # type: ignore
            [],
            "The store's items length was not 0 even though no items were"
            " added.",
        )

    def test_crud(self) -> None:
        """
        Test CRUD operations for Store
        :return: None
        :rtype: NoneType
        """
        with self.app_context:
            store: Store = Store("test")
            session = Session()
            self.assertIsNone(Store.find_by_name(session, "test"))
            store.save_to_db(session)
            self.assertIsNotNone(Store.find_by_name(session, "test"))
            store.delete_from_db(session)
            self.assertIsNone(Store.find_by_name(session, "test"))

    def test_store_relationship(self) -> None:
        """
        Test the Store relationship from database
        :return: None
        :rtype: NoneType
        """
        with self.app_context:
            session = Session()
            store: Store = Store("test")
            store.save_to_db(session)
            store_id: int = store.id
            item: Item = Item("test item", 19.99, store_id)
            item.save_to_db(session)
            self.assertEqual(store.items.count(), 1)  # type: ignore
            self.assertEqual(
                store.items.first().name,  # type: ignore
                "test item",
            )

    def test_store_json(self) -> None:
        """
        Test the Store json from database
        :return: None
        :rtype: NoneType
        """
        store: Store = Store("test")
        expected: dict[str, str | list[Any]] = {
            "name": "test",
            "items": [],
        }
        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self) -> None:
        """
        Test store json with items
        :return: None
        :rtype: NoneType
        """
        with self.app_context:
            session = Session()
            store: Store = Store("test")
            store.save_to_db(session)
            store_id: int = store.id
            item: Item = Item("test item", 19.99, store_id)
            item.save_to_db(session)
            expected: dict[str, str | list[dict[str, str | float]]] = {
                "name": "test",
                "items": [
                    {
                        "name": "test item",
                        "price": 19.99,
                        "store_id": store_id,
                    },
                ],
            }
            self.assertDictEqual(store.json(), expected)
