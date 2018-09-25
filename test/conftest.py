import pytest

from test.common import clean_up_users


@pytest.fixture
def clean_up_users_fixture():
    response = clean_up_users()
    if response.status_code != 200:
        raise RuntimeError("Unable to clean up users")
