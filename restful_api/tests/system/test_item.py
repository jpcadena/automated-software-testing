"""
A module for test item in the restful api.tests.system package.
"""

import json
from typing import Any

from werkzeug.test import TestResponse

from restful_api.app.core.utils import encode_jwt
from restful_api.app.db.db import Session
from restful_api.app.models.item import Item
from restful_api.app.models.store import Store
from restful_api.tests.system.base_test import BaseTest


class ItemTest(BaseTest):
    def get_token(self) -> str:
        return encode_jwt(identity=1)

    def test_item_found(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                store: Store = Store(name="test_store")
                try:
                    store.save_to_db(session)
                    token = self.create_item_get_token(store, session)
                    test_response: TestResponse = client.get(
                        "/item/test_item",
                        headers={"Authorization": f"Bearer {token}"},
                    )
                    print(f"Token: {token}")  # Debugging line
                    print(
                        f"Response Data: {test_response.data}"
                    )  # Debugging line
                    self.assertEqual(test_response.status_code, 200)
                    self.assertDictEqual(
                        d1={
                            "name": "test_item",
                            "price": 2.99,
                            "store_id": store.id,
                        },
                        d2=json.loads(test_response.data),
                    )
                except Exception as e:
                    session.rollback()
                    raise e

    def test_item_not_found(self) -> None:
        with self.app() as client:
            with self.app_context():
                token: str = self.get_token()
                test_response: TestResponse = client.get(
                    "/item/test", headers={"Authorization": f"Bearer {token}"}
                )
                print("test_item_not_found")
                print(test_response.status)
                self.assertEqual(test_response.status_code, 404)

    def test_create_item(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                store: Store = Store(name="test_store")
                try:
                    store.save_to_db(session)
                    token = self.get_token()
                    test_response: TestResponse = client.post(
                        "/item/test_item",
                        json={"price": 2.99, "store_id": store.id},
                        headers={
                            "Content-Type": "application/json",
                            "Authorization": f"Bearer {token}",
                        },
                    )
                    self.assertEqual(test_response.status_code, 201)
                    self.assertIsNotNone(
                        Item.find_by_name(session, "test_item")
                    )
                    self.assertDictEqual(
                        d1={
                            "name": "test_item",
                            "price": 2.99,
                            "store_id": store.id,
                        },
                        d2=json.loads(test_response.data),
                    )
                except Exception as e:
                    session.rollback()
                    raise e

    def test_create_duplicate_item(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                store: Store = Store(name="test_store")
                try:
                    store.save_to_db(session)
                    client.post(
                        "/item/test_item",
                        json={"price": 2.99, "store_id": store.id},
                        headers={
                            "Content-Type": "application/json",
                            "Authorization": f"Bearer {self.get_token()}",
                        },
                    )
                    test_response: TestResponse = client.post(
                        "/item/test_item",
                        json={"price": 2.99, "store_id": store.id},
                        headers={
                            "Content-Type": "application/json",
                            "Authorization": f"Bearer {self.get_token()}",
                        },
                    )
                    self.assertEqual(test_response.status_code, 400)
                except Exception as e:
                    session.rollback()
                    raise e

    def test_delete_item(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                store: Store = Store(name="test_store")
                try:
                    store.save_to_db(session)
                    token = self.create_item_get_token(store, session)
                    test_response: TestResponse = client.delete(
                        "/item/test_item",
                        headers={"Authorization": f"Bearer {token}"},
                    )
                    self.assertEqual(test_response.status_code, 200)
                    self.assertDictEqual(
                        d1={"message": "Item deleted"},
                        d2=json.loads(test_response.data),
                    )
                except Exception as e:
                    session.rollback()
                    raise e

    def test_item_list(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                store: Store = Store(name="test_store")
                try:
                    store.save_to_db(session)
                    Item(
                        name="test_item", price=2.99, store_id=store.id
                    ).save_to_db(session)
                    token = self.get_token()
                    test_response: TestResponse = client.get(
                        "/items", headers={"Authorization": f"Bearer {token}"}
                    )
                    self.assertDictEqual(
                        d1={
                            "items": [
                                {
                                    "name": "test_item",
                                    "price": 2.99,
                                    "store_id": store.id,
                                }
                            ]
                        },
                        d2=json.loads(test_response.data),
                    )
                except Exception as e:
                    session.rollback()
                    raise e

    def test_update_item(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                store: Store = Store(name="test_store")
                try:
                    store.save_to_db(session)
                    token = self.create_item_get_token(store, session)
                    test_response: TestResponse = client.put(
                        "/item/test_item",
                        json={"price": 3.99, "store_id": store.id},
                        headers={
                            "Content-Type": "application/json",
                            "Authorization": f"Bearer {token}",
                        },
                    )
                    self.assertEqual(test_response.status_code, 200)
                    self.assertDictEqual(
                        d1={
                            "name": "test_item",
                            "price": 3.99,
                            "store_id": store.id,
                        },
                        d2=json.loads(test_response.data),
                    )
                except Exception as e:
                    session.rollback()
                    raise e

    def create_item_get_token(self, store: Store, session: Any) -> str:
        item: Item = Item(name="test_item", price=2.99, store_id=store.id)
        item.save_to_db(session)
        return self.get_token()
