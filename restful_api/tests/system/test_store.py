"""
A module for test store in the restful api.tests.system package.
"""

import json

from werkzeug.test import TestResponse

from restful_api.app.core.utils import encode_jwt
from restful_api.app.db.db import Session
from restful_api.app.models.item import Item
from restful_api.app.models.store import Store
from restful_api.tests.system.base_test import BaseTest


class StoreTest(BaseTest):
    def get_token(self) -> str:
        return encode_jwt(1, "my-server-resource", "my-server-resource")

    def test_create_store(self) -> None:
        with self.app() as client:
            with self.app_context():
                token = self.get_token()
                test_response: TestResponse = client.post(
                    "/store/test",
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {token}",
                    },
                )
                self.assertEqual(test_response.status_code, 201)

    def test_create_duplicate_store(self) -> None:
        with self.app() as client:
            with self.app_context():
                token = self.get_token()
                client.post(
                    "/store/test",
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {token}",
                    },
                )
                test_response: TestResponse = client.post(
                    "/store/test",
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {token}",
                    },
                )
                self.assertEqual(test_response.status_code, 400)

    def test_delete_store(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                store: Store = Store(name="test_store")
                store.save_to_db(session)
                token = self.get_token()
                test_response: TestResponse = client.delete(
                    "/store/test_store",
                    headers={"Authorization": f"Bearer {token}"},
                )
                self.assertEqual(test_response.status_code, 200)

    def test_store_found(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                store: Store = Store(name="test_store")
                store.save_to_db(session)
                token = self.get_token()
                test_response: TestResponse = client.get(
                    "/store/test_store",
                    headers={"Authorization": f"Bearer {token}"},
                )
                self.assertEqual(test_response.status_code, 200)
                self.assertDictEqual(
                    d1={"name": "test_store", "items": []},
                    d2=json.loads(test_response.data),
                )

    def test_store_list(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                Store(name="test_store").save_to_db(session)
                token = self.get_token()
                test_response: TestResponse = client.get(
                    "/stores", headers={"Authorization": f"Bearer {token}"}
                )
                self.assertDictEqual(
                    d1={"stores": [{"name": "test_store", "items": []}]},
                    d2=json.loads(test_response.data),
                )

    def test_store_not_found(self) -> None:
        with self.app() as client:
            token: str = self.get_token()
            test_response: TestResponse = client.get(
                "/store/non_existent_store",
                headers={"Authorization": f"Bearer {token}"},
            )
            self.assertEqual(test_response.status_code, 404)

    def test_store_with_items_found(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                store: Store = Store(name="test_store")
                store.save_to_db(session)
                item: Item = Item(
                    name="test_item", price=2.99, store_id=store.id
                )
                item.save_to_db(session)
                token = self.get_token()
                test_response: TestResponse = client.get(
                    "/store/test_store",
                    headers={"Authorization": f"Bearer {token}"},
                )
                self.assertEqual(test_response.status_code, 200)
                self.assertDictEqual(
                    d1={
                        "name": "test_store",
                        "items": [
                            {
                                "name": "test_item",
                                "price": 2.99,
                                "store_id": store.id,
                            }
                        ],
                    },
                    d2=json.loads(test_response.data),
                )

    def test_store_with_items_list(self) -> None:
        with self.app() as client:
            with self.app_context():
                session = Session()
                store: Store = Store(name="test_store")
                store.save_to_db(session)
                item: Item = Item(
                    name="test_item", price=17.99, store_id=store.id
                )
                item.save_to_db(session)
                token = self.get_token()
                test_response: TestResponse = client.get(
                    "/stores", headers={"Authorization": f"Bearer {token}"}
                )
                self.assertDictEqual(
                    d1={
                        "stores": [
                            {
                                "name": "test_store",
                                "items": [
                                    {
                                        "name": "test_item",
                                        "price": 17.99,
                                        "store_id": store.id,
                                    }
                                ],
                            }
                        ]
                    },
                    d2=json.loads(test_response.data),
                )
