"""
A module for test item in the restful api.tests.integration.models package.
"""

from werkzeug.test import TestResponse

from restful_api.tests.test_base import BaseTest


class ItemTest(BaseTest):
    def test_create_item(self) -> None:
        """
        Test the creation of an item
        :return: None
        :rtype: NoneType
        """
        response: TestResponse = self.app.post(
            "/item/test_item",
            json={
                "price": 10.99,
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"name": "test_item", "price": 10.99})

    def test_get_item(self) -> None:
        """
        Test retrieving an item
        :return: None
        :rtype: NoneType
        """
        self.app.post("/item/test_item", json={"price": 10.99})
        response: TestResponse = self.app.get("/item/test_item")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"name": "test_item", "price": 10.99})

    def test_delete_item(self) -> None:
        """
        Test deleting an item
        :return: None
        :rtype: NoneType
        """
        self.app.post("/item/test_item", json={"price": 10.99})
        response: TestResponse = self.app.delete("/item/test_item")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Item deleted"})
        response = self.app.get("/item/test_item")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Item not found"})

    def test_update_item(self) -> None:
        """
        Test updating an item
        :return: None
        :rtype: NoneType
        """
        self.app.post("/item/test_item", json={"price": 10.99})
        response: TestResponse = self.app.put(
            "/item/test_item", json={"price": 15.99}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"name": "test_item", "price": 15.99})
