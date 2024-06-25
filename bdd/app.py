"""
A module for app in the bdd package.
"""

from flask import Flask, redirect, render_template, request, url_for
from werkzeug import Response

app: Flask = Flask(
    __name__, static_folder="../app/static", template_folder="../templates"
)

posts: list[dict[str, str]] = [
    {"title": "First Post", "content": "Content of the first post"},
    {"title": "Second Post", "content": "Content of the second post"},
]


@app.route("/")
def homepage() -> str:
    """
    The homepage method
    :return: The home rendered template
    :rtype: str
    """
    return render_template("home.html")


@app.route("/blog")
def blog_page() -> str:
    """
    Path to the blog section
    :return: The blog rendered template
    :rtype: str
    """
    return render_template("blog.html", posts=posts)


@app.route("/post", methods=["GET", "POST"])
def add_post() -> Response | str:
    """
    Add a post to the blog
    :return: The new post rendered template or a redirected response to blog
    page
    :rtype: Response or str
    """
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        global posts
        posts.append({"title": title, "content": content})
        return redirect(url_for("blog_page"))
    return render_template("new_post.html")


@app.route("/post/<string:title>")
def see_post(title: str) -> str:
    """
    Search for a post given a title
    :param title: The title of the post to seek
    :type title: str
    :return: The post rendered template
    :rtype: str
    """
    global posts
    for post in posts:
        if post["title"] == title:
            return render_template("post.html", post=post)

    return render_template("post.html", post=None)


if __name__ == "__main__":
    app.run()
