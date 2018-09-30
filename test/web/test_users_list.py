import pytest

from test.common import create_user
from test.data import simple_user


class TestUsersList:

    @pytest.fixture
    def create_user_fixture(self):
        response = create_user(simple_user)
        if response.status_code != 200:
            raise RuntimeError('Unable to create user')

    @pytest.mark.usefixtures('clean_up_users_fixture', 'create_user_fixture')
    def test_user_list(self, set_up_webdriver_fixture):
        user_list_page = set_up_webdriver_fixture
        assert user_list_page.get_user(1) == simple_user
