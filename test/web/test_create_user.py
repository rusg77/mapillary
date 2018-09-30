import pytest

from test.common import get_users
from test.data import simple_user


class TestUsersList:

    @pytest.mark.usefixtures('clean_up_users_fixture')
    def test_user_list(self, set_up_webdriver_fixture):
        user_list_page = set_up_webdriver_fixture
        create_user_page = user_list_page.click_create_user()
        create_user_page.create_user(simple_user)
        assert get_users().json() == {'users': [simple_user]}
