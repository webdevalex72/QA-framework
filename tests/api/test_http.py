import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    print(f'\nResponse Boby is ...\n{"-" * 25}\n {r.json()}\n')
    print("-" * 25)
    print(f'Response Status code is ... {r.status_code}')
    print("-" * 25)
    print(f'Response Headers are ...\n{"-" * 25}\n {r.headers}')
# pytest -m http -s (last flag (-s) for display print() in test)
