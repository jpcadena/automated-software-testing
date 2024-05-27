"""
A module for test store in the restful api.tests.unit.models package.
"""

from unittest import TestCase

# from restful_api.app.models.item import Item
from restful_api.app.models.store import Store


class StoreTest(TestCase):
    def test_create_store(self) -> None:
        store: Store = Store(
            "test",
        )
        self.assertEqual(
            store.name,
            "test",
            "The name of the store after creation does not equal the"
            " constructor argument.",
        )

    def test_store_json(self) -> None:
        store: Store = Store(
            "test",
        )
        expected: dict[str, str | list[dict[str, str | float | int]]] = {
            "name": "test",
            "items": [item.json() for item in store.items],
        }
        self.assertEqual(
            store.json(),
            expected,
            f"The JSON representation of store is incorrect. Received "
            f"{store.json()}, expected {expected}.",
        )
