import pytest
from selenium.webdriver import Chrome

from test.common import clean_up_users
from test.config import host
from test.web.pages.user_list_page import UserListPage


@pytest.fixture
def clean_up_users_fixture():
    response = clean_up_users()
    if response.status_code != 200:
        raise RuntimeError("Unable to clean up users")


@pytest.fixture
def set_up_webdriver_fixture(request):
    webdriver = Chrome()
    webdriver.get(host)
    yield UserListPage(webdriver)

    def fin():
        webdriver.quit()

    request.addfinalizer(fin)
