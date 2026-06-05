import pytest
from services.post_service import PostService
from services.user_service import UserService

@pytest.fixture
def post_service(base_url):
    return PostService(base_url)

@pytest.fixture
def user_service(base_url):
    return UserService(base_url)

class TestInvalidPostRequests:

    def test_get_nonexistent_post_returns_404(self, post_service):
        response = post_service.get_post_by_id(99999)
        assert response.status_code == 404

    def test_get_nonexistent_post_returns_empty_body(self, post_service):
        response = post_service.get_post_by_id(99999)
        data = response.json()
        assert data == {}

    def test_delete_nonexistent_post_returns_200(self, post_service):
        response = post_service.delete_post(99999)
        assert response.status_code == 200

    def test_create_post_empty_payload_returns_201(self, post_service):
        response = post_service.create_post({})
        assert response.status_code == 201

    def test_update_nonexistent_post_returns_500(self, post_service):
        payload = {"userId": 1, "title": "Ghost Post", "body": "Does not exist"}
        response = post_service.update_post(99999, payload)
        assert response.status_code == 500

class TestInvalidUserRequests:

    def test_get_nonexistent_user_returns_404(self, user_service):
        response = user_service.get_user_by_id(99999)
        assert response.status_code == 404