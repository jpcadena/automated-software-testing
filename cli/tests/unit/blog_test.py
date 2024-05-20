"""
A module for blog test in the tests package.
"""

from unittest import TestCase

from cli.blog import Blog
from cli.post import Post


class BlogTest(TestCase):
    def test_create_post(self) -> None:
        blog: Blog = Blog("Test", "Test author")
        self.assertEqual("Test", blog.title)
        self.assertEqual("Test author", blog.author)
        self.assertListEqual([], blog.posts)
        # self.assertEqual(0, len(blog.posts))

    def test_repr(self) -> None:
        blog: Blog = Blog("Test", "Test author")
        another_blog: Blog = Blog("My day", "Rolf")

        self.assertEqual(blog.__repr__(), "Test by Test author (0 posts)")
        self.assertEqual(another_blog.__repr__(), "My day by Rolf (0 posts)")

    def test_repr_multiple_posts(self) -> None:
        blog: Blog = Blog("Test", "Test author")
        blog.posts = [Post("Test", "Test content")]
        another_blog: Blog = Blog("My day", "Rolf")
        another_blog.posts = [
            Post("Test", "Test content"),
            Post("Test", "Another test content"),
        ]
        self.assertEqual(blog.__repr__(), "Test by Test author (1 post)")
        self.assertEqual(another_blog.__repr__(), "My day by Rolf (2 posts)")
