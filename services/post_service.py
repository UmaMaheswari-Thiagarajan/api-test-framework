import requests

class PostService:
    def __init__(self, base_url):
        self.base_url = base_url
        self.endpoint = f"{base_url}/posts"

    def get_all_posts(self):
        return requests.get(self.endpoint)

    def get_post_by_id(self, post_id):
        return requests.get(f"{self.endpoint}/{post_id}")

    def create_post(self, payload):
        return requests.post(self.endpoint, json=payload)

    def update_post(self, post_id, payload):
        return requests.put(f"{self.endpoint}/{post_id}", json=payload)

    def delete_post(self, post_id):
        return requests.delete(f"{self.endpoint}/{post_id}")