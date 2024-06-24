"""
A module for app in the bdd package.
"""

from flask import Flask, redirect, render_template, request, url_for

app: Flask = Flask(__name__)

posts = []


@app.route("/")
def homepage() -> str:
    return render_template("templates/home.html")


@app.route("/blog")
def blog_page() -> str:
    return render_template("templates/blog.html", posts=posts)


@app.route("/post", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        global posts
        posts.append({"title": title, "content": content})
        return redirect(url_for("blog_page"))
    return render_template("templates/new_post.html")


@app.route("/post/<string:title>")
def see_post(title: str) -> str:
    global posts
    for post in posts:
        if post["title"] == title:
            return render_template("templates/post.html", post=post)

    return render_template("templates/post.html", post=None)


if __name__ == "__main__":
    app.run()
