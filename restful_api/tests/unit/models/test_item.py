"""
A module for test item in the restful api.tests.unit.models package.
"""

from unittest import TestCase

from restful_api.app.models.item import Item


class ItemTest(TestCase):
    def test_create_item(self) -> None:
        item: Item = Item("test", 19.99, 1)
        self.assertEqual(
            item.name,
            "test",
            "The name of the item after creation does not equal the"
            " constructor argument.",
        )
        self.assertEqual(
            item.price,
            19.99,
            "The price of the item after creation does not equal the"
            " constructor argument.",
        )
        self.assertEqual(
            item.store_id,
            1,
        )
        self.assertIsNone(
            item.store,
        )

    def test_item_json(self) -> None:
        item: Item = Item("test", 19.99, 1)
        expected: dict[str, str | float | int] = {
            "name": "test",
            "price": 19.99,
            "store_id": 1,
        }
        self.assertEqual(
            item.json(),
            expected,
            f"The JSON representation of item is incorrect. Received "
            f"{item.json()}, expected {expected}.",
        )
