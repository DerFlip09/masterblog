import json


class StorageJson:
    def __init__(self, file_path):
        self._file = file_path

    def list_data(self):
        with open(self._file, "r") as file:
            blog_data = json.load(file)
        return blog_data

    def add_data(self, author, title, content):
        blog_data = self.list_data()
        blog_data.append({"id": len(blog_data) + 1, "author": author, "title": title, "content": content})
        self.update_storage_file(blog_data)
        return "Blog Post successfully added!"

    def update_data(self, id, subject, changes):
        blog_data = self.list_data()
        for blog in blog_data:
            if blog["id"] == id:
                blog[subject.lower] = changes
                self.update_storage_file(blog_data)
                return "Blog Post successfully updated"
        raise IndexError(f"Could not find the Post with id {id}")

    def delete_data(self, id):
        blog_data = self.list_data()
        for blog in blog_data:
            if blog["id"] == id:
                del blog
                self.update_storage_file(blog_data)
                return "Blog post successfully deleted"
        raise IndexError(f"Could not find the Post with id {id}")

    def update_storage_file(self, data):
        with open(self._file, "w") as file:
            json.dump(data, file, indent=4)
