import pytest
from services.post_service import PostService
from utils.helpers import is_valid_post, has_no_empty_values

@pytest.fixture
def post_service(base_url):
    return PostService(base_url)

class TestGetPosts:

    def test_get_all_posts_status_code(self, post_service):
        response = post_service.get_all_posts()
        assert response.status_code == 200

    def test_get_all_posts_returns_list(self, post_service):
        response = post_service.get_all_posts()
        data = response.json()
        assert isinstance(data, list)

    def test_get_all_posts_count(self, post_service):
        response = post_service.get_all_posts()
        data = response.json()
        assert len(data) == 100

    def test_get_all_posts_valid_structure(self, post_service):
        response = post_service.get_all_posts()
        posts = response.json()
        for post in posts[:5]:
            assert is_valid_post(post)

    def test_get_post_by_id_status_code(self, post_service):
        response = post_service.get_post_by_id(1)
        assert response.status_code == 200

    def test_get_post_by_id_correct_id(self, post_service):
        response = post_service.get_post_by_id(1)
        data = response.json()
        assert data["id"] == 1

    def test_get_post_by_id_no_empty_values(self, post_service):
        response = post_service.get_post_by_id(1)