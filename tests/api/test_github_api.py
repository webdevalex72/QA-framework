import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists():
    api = GitHub()
    user = api.get_user_defunkt()
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exist():
    api = GitHub()
    r = api.get_non_exist_user()
    assert r['message'] == 'Not Found'
