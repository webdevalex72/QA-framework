# modules/api/clients/github.py
"""This module defines the class to test API GitHub."""
import requests
from config.config import config_dict


class GitHub:
    """Class provides several methods to use GitHub API."""

    def __init__(self) -> None:
        """Set conf. values for API."""
        self.conf = config_dict["API"]

    def get_user(self, username: str) -> dict:
        """Provides publicly available information about \
        someone with a GitHub account.

        Args:
            username: A username of a GitHub account.

        Returns:
            A dictionary with several public information.
            """
        # r = requests.get(f'https://api.github.com/users/{username}')
        r = requests.get(self.conf["users"] + username)
        body = r.json()

        return body

    def search_repo(self, name: str) -> dict:
        """Provides publicly available information about \
        someone with a GitHub account.

        Args:
            name: The query contains one or more search keywords and \
                qualifiers. Qualifiers allow you to limit your search to \
                specific areas of GitHub.
        Returns:
            A dictionary with several pieces of information.
        """
        r = requests.get(self.conf["repositories"], params={"q": name})
        body = r.json()

        return body
