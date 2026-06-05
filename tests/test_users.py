import pytest
from services.user_service import UserService
from utils.helpers import is_valid_user

@pytest.fixture
def user_service(base_url):
    return UserService(base_url)

class TestGetUsers:

    def test_get_all_users_status_code(self, user_service):
        response = user_service.get_all_users()
        assert response.status_code == 200

    def test_get_all_users_returns_list(self, user_service):
        response = user_service.get_all_users()
        data = response.json()
        assert isinstance(data, list)

    def test_get_all_users_count(self, user_service):
        response = user_service.get_all_users()
        data = response.json()
        assert len(data) == 10

    def test_get_all_users_valid_structure(self, user_service):
        response = user_service.get_all_users()
        users = response.json()
        for user in users:
            assert is_valid_user(user)

    def test_get_user_by_id_status_code(self, user_service):
        response = user_service.get_user_by_id(1)
        assert response.status_code == 200

    def test_get_user_by_id_correct_id(self, user_service):
        response = user_service.get_user_by_id(1)
        data = response.json()
        assert data["id"] == 1

    def test_get_user_by_id_has_email(self, user_service):
        response = user_service.get_user_by_id(1)
        data = response.json()
        assert "@" in data["email"]

    def test_get_user_by_id_has_address(self, user_service):
        response = user_service.get_user_by_id(1)
        data = response.json()
        assert "address" in data
        assert "city"