from flask import Flask, render_template
from storage.storage import StorageJson
import os


app = Flask(__name__)
file_path = os.path.join("storage", "blog_posts.json")
storage = StorageJson(file_path)


@app.route('/')
def index():
    blog_posts = storage.list_data()
    return render_template("index.html", posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
