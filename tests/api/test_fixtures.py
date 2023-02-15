# test/api/test_fixtures.py
"""This module defines some API tests."""
import pytest


@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Oleksandr'


@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == 'Khomenko'
