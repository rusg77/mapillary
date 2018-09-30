import pytest

from test.data import simple_user, cyrillic_user, chinese_user, max_length_user
from test.common import create_user, get_users


class TestGetUsers:

    @pytest.fixture
    def create_users(self, request):
        users = request.param
        for user in users:
            response = create_user(user)
            if response.status_code != 200:
                raise RuntimeError("Unable to create user")
        return users

    @pytest.mark.parametrize("test_name, create_users", [
        ('no_user', []),
        ('simple_user', [simple_user]),
        ('cyrillic_user', [cyrillic_user]),
        ('chinese_user', [chinese_user]),
        ('max_length_user', [max_length_user]),
        ('multiple_users', [simple_user,
                            cyrillic_user,
                            chinese_user,
                            max_length_user]),
    ], indirect=['create_users'])
    @pytest.mark.usefixtures('clean_up_users_fixture')
    def test_get_users(self, test_name, create_users):
        users = create_users
        response = get_users()
        assert response.headers['Content-type'] == 'application/json'
        assert response.status_code == 200
        assert response.json() == {'users': users}
