# conftest.py
"""This module provides a fixture for pytest."""
import pytest
from modules.api.clients.github import GitHub


class User:
    """Class User for test API."""
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        """Create user properties."""
        self.name = 'Oleksandr'
        self.second_name = 'Khomenko'

    def remove(self):
        """Clean user properties."""
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user  # Повертає об’єкт  в тести

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api
