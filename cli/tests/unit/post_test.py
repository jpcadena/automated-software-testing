"""
A module for post test in the tests package.
"""

from unittest import TestCase

from cli.post import Post


class PostTest(TestCase):
    def test_create_post(self) -> None:
        post: Post = Post("Test", "Test content")
        self.assertEqual("Test", post.title)
        self.assertEqual("Test content", post.content)

    def test_json(self) -> None:
        post: Post = Post("Test", "Test content")
        expected_json: dict[str, str] = {
            "title": "Test",
            "content": "Test content",
        }
        self.assertDictEqual(expected_json, post.json())
