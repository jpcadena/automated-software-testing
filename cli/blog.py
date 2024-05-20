"""
A module for blog in the project.
"""

from typing import TypeAlias

from cli.post import Post

BlogJson: TypeAlias = dict[str, str | list[dict[str, str]]]


class Blog:
    """
    Blog representation as a class
    """

    def __init__(self, title: str, author: str):
        self.title: str = title
        self.author: str = author
        self.posts: list[Post] = []

    def __repr__(self) -> str:
        return (
            f"{self.title} by {self.author} ({len(self.posts)}"
            f" post{'s' if len(self.posts) != 1 else ''})"
        )

    def create_post(self, title: str, content: str) -> None:
        """
        Create a new post in the blog
        :param title: The title of the post
        :type title: str
        :param content: The content of the post
        :type content: str
        """
        self.posts.append(Post(title=title, content=content))

    def json(self) -> BlogJson:
        """
        Parse the blog object as JSON
        :return: The json representation for the blog
        :rtype: BlogJson
        """
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }
