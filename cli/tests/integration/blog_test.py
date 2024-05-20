"""
A module for test blog in the tests-integration package.
"""

from unittest import TestCase

from cli.blog import Blog, BlogJson


class BlogTest(TestCase):
    def test_create_post_in_blog(self) -> None:
        blog: Blog = Blog("Test", "Test author")
        blog.create_post("Test post", "Test content")
        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, "Test post")
        self.assertEqual(blog.posts[0].content, "Test content")

    def test_json(self) -> None:
        blog: Blog = Blog("Test", "Test author")
        blog.create_post("Test post", "Test content")
        expected: BlogJson = {
            "title": "Test",
            "author": "Test author",
            "posts": [{"title": "Test post", "content": "Test content"}],
        }
        self.assertDictEqual(blog.json(), expected)

    def test_json_no_posts(self) -> None:
        blog: Blog = Blog("Test", "Test author")
        expected: BlogJson = {
            "title": "Test",
            "author": "Test author",
            "posts": [],
        }
        self.assertDictEqual(blog.json(), expected)
