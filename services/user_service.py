import requests

class UserService:
    def __init__(self, base_url):
        self.base_url = base_url
        self.endpoint = f"{base_url}/users"

    def get_all_users(self):
        return requests.get(self.endpoint)

    def get_user_by_id(self, user_id):
        return requests.get(f"{self.endpoint}/{user_id}")

    def get_posts_by_user(self, user_id):
        return requests.get(f"{self.base_url}/posts?userId={user_id}")