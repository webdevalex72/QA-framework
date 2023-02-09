import requests
from config.config import config_dict


class GitHub:
    def __init__(self) -> None:
        self.conf = config_dict['API']

    def get_user(self, username):
        # r = requests.get(f'https://api.github.com/users/{username}')
        r = requests.get(self.conf["users"] + username)
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            self.conf["repositories"], params={"q": name}
        )
        body = r.json()

        return body
