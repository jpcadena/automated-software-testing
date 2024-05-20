"""
A module for managing a blogging application.
This module allows users to interact with a blogging system, enabling them
to create blogs, add posts to them, and view them through a console-based
menu system.
"""

from cli.blog import Blog
from cli.post import Post

MENU_PROMPT: str = (
    "Enter 'c' to create a blog, 'l' to list all blogs, 'r' to"
    " read one, 'p' to create a post, or 'q' to quit."
)
POST_TEMPLATE: str = """
--- {} ---
{}
"""
blogs: dict[str, Blog] = {}


def menu() -> None:
    """
    Executes the main menu loop, processing user commands until they choose to
     quit.
    :return: None
    :rtype: NoneType
    """
    print_blogs()
    selection: str = input(MENU_PROMPT)
    print("Debug: Printed menu prompt", selection)
    while selection != "q":
        try:
            match selection:
                case "c":
                    ask_create_blog()
                case "l":
                    print_blogs()
                case "r":
                    ask_read_blog()
                case "p":
                    ask_create_post()
                case _:
                    print("Invalid option, please choose a valid command.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            selection = input(MENU_PROMPT)


def ask_create_blog() -> None:
    """
    Prompts the user to enter details for a new blog and creates it.
    Asks for the blog's title and author, then creates a new Blog instance and
     stores it.
    :return: None
    :rtype: NoneType
    """
    title: str = input("Enter the title of the blog: ")
    author: str = input("Enter the author of the blog: ")
    blogs[title] = Blog(title, author)


def ask_read_blog() -> None:
    """
    Prompts the user to enter the title of a blog to read and displays its
     posts.
    If the blog does not exist, notifies the user.
    :return: None
    :rtype: NoneType
    """
    title: str = input("Enter the blog title to read: ")
    try:
        print_posts(blogs[title])
    except KeyError:
        print("Blog not found.")


def ask_create_post() -> None:
    """
    Prompts the user for details to create a post in a specified blog.
    Asks for the blog title, post title, and content. If the blog exists, adds
     a new post to it.
    If the blog does not exist, notifies the user.
    :return: None
    :rtype: NoneType
    """
    blog_title: str = input("Enter the blog title to add a post to: ")
    if blog_title in blogs:
        post_title: str = input("Enter the post title: ")
        post_content: str = input("Enter the post content: ")
        blogs[blog_title].create_post(title=post_title, content=post_content)
        print(f"Post '{post_title}' added to blog '{blog_title}'.")
    else:
        print("Blog not found.")


def print_blogs() -> None:
    """
    Prints a summary of all blogs in the system.
    Lists each blog's name and a description, or notifies that no blogs are
     available.
    :return: None
    :rtype: NoneType
    """
    if blogs:
        for key, description in blogs.items():
            print(f"- Blog Name: {key}, Description: {description}")
    else:
        print("No blogs available.")


def print_posts(blog: Blog) -> None:
    """
    Prints all posts within a specified blog.
    :param blog: The blog from which to print posts.
    :type blog: Blog
    :return: None
    :rtype: NoneType
    """
    if blog.posts:
        for post in blog.posts:
            print_post(post)
    else:
        print("\n    --- No posts available ---\n")


def print_post(post: Post) -> None:
    """
    Prints a single post using a predefined template.
    :param post: The post to print.
    :type post: Post
    :return: None
    :rtype: NoneType
    """
    print(POST_TEMPLATE.format(post.title, post.content))


def main() -> None:
    """
    Main function for the application
    :return: None
    :rtype: NoneType
    """
    menu()


if __name__ == "__main__":
    main()
