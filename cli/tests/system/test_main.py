"""
A module for main test in the tests-system package.
"""

from unittest import TestCase
from unittest.mock import patch

from cli import main
from cli.blog import Blog
from cli.post import Post


class AppTest(TestCase):
    def setUp(self) -> None:
        """
        Set up the test suite
        :return: None
        :rtype: NoneType
        """
        blog: Blog = Blog("Test", "Test author")
        main.blogs = {"Test": blog}

    def test_print_blogs(self) -> None:
        with patch("builtins.print") as mocked_print:
            main.print_blogs()
            mocked_print.assert_called_with(
                "- Blog Name: Test, Description: Test by Test author (0 posts)"
            )

    def test_menu_print_prompts(self) -> None:
        with (
            patch(
                "builtins.input", side_effect=lambda _: "q", return_value="q"
            ) as mocked_input,
            patch("builtins.print") as mocked_print,
        ):
            main.blogs = {"Sample": Blog("Sample", "Author")}
            main.menu()
            expected_prompt: str = main.MENU_PROMPT
            mocked_input.assert_called_with(expected_prompt)
            actual_prints = [
                call_args.args[0]
                for call_args in mocked_print.call_args_list
                if call_args.args
            ]
            print("Printed calls during test:", actual_prints)

    def test_menu_calls_print_blogs(self) -> None:
        with (
            patch("cli.main.print_blogs") as mocked_print_blogs,
            patch("builtins.input", return_value="q"),
        ):
            main.menu()
            mocked_print_blogs.assert_called()

    def test_ask_create_blog(self) -> None:
        with patch("builtins.input", side_effect=("Test", "Test author")):
            main.ask_create_blog()
            self.assertIn("Test", main.blogs)

    def test_ask_read_blog(self) -> None:
        with (
            patch("builtins.input", return_value="Test"),
            patch("cli.main.print_posts") as mocked_print,
        ):
            main.ask_read_blog()
            mocked_print.assert_called_with(main.blogs["Test"])

    def test_print_posts(self) -> None:
        blog: Blog = Blog("Test", "Test author")
        blog.create_post("Test post", "Test content")
        with patch("cli.main.print_post") as mocked_print_post:
            main.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self) -> None:
        post: Post = Post("Post title", "Post content")
        expected_print: str = main.POST_TEMPLATE.format(
            post.title, post.content
        )
        with patch("builtins.print") as mocked_print:
            main.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_ask_read_blog_not_found(self) -> None:
        main.blogs = {}
        with (
            patch("builtins.input", return_value="Test"),
            patch("builtins.print") as mocked_print,
        ):
            main.ask_read_blog()
            mocked_print.assert_called_with("Blog not found.")

    def test_ask_create_post(self) -> None:
        with (
            patch(
                "builtins.input",
                side_effect=("Test", "Post Title", "Post Content"),
            ),
            patch("builtins.print") as mocked_print,
        ):
            main.ask_create_post()
            self.assertEqual(len(main.blogs["Test"].posts), 1)
            self.assertEqual(main.blogs["Test"].posts[0].title, "Post Title")
            mocked_print.assert_called_with(
                "Post 'Post Title' added to blog 'Test'."
            )

    def test_ask_read_blog_found(self) -> None:
        with (
            patch("builtins.input", return_value="Test"),
            patch("builtins.print") as mocked_print,
        ):
            main.ask_read_blog()
            mocked_print.assert_called_once_with(
                "\n    --- No posts available ---\n"
            )

    def test_ask_create_post_blog_found(self) -> None:
        with (
            patch(
                "builtins.input",
                side_effect=("Test", "New Post", "Content of new post"),
            ),
            patch("builtins.print") as mocked_print,
        ):
            main.ask_create_post()
            mocked_print.assert_called_with(
                "Post 'New Post' added to blog 'Test'."
            )

    def test_ask_create_post_blog_not_found(self) -> None:
        main.blogs = {}
        with (
            patch("builtins.input", return_value="Nonexistent Blog"),
            patch("builtins.print") as mocked_print,
        ):
            main.ask_create_post()
            mocked_print.assert_called_with("Blog not found.")

    def test_menu_calls_create_blog(self) -> None:
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = (
                "c",
                "Test create blog",
                "Test author",
                "q",
            )
            main.menu()
            self.assertIsNotNone(main.blogs["Test create blog"])
