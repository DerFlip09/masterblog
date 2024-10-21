from flask import Flask, render_template, request, redirect, url_for
from storage.storage import StorageJson
import os


app = Flask(__name__)
file_path = os.path.join("storage", "blog_posts.json")
storage = StorageJson(file_path)


@app.route("/")
def index():
    blog_posts = storage.list_data()
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        storage.add_data(author, title, content)
        return redirect(url_for("index"))
    return render_template("add.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
