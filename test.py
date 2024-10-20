import json
import os

file_path = os.path.join("storage", "blog_posts.json")
with open(file_path, "r") as file:
    data = json.load(file)

for item in data:
    print(item)
    print(item["author"])
    print(item["title"])
    print(item["content"])
    print("------------------")


