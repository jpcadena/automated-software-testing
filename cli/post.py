"""
A module for post in the project.
"""


class Post:
    """
    Post representation as a class
    """

    def __init__(self, title: str, content: str):
        self.title: str = title
        self.content: str = content

    def json(self) -> dict[str, str]:
        return {
            "title": self.title,
            "content": self.content,
        }
