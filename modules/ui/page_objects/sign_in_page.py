# modules/ui/page_object/sign_in_page.py
"""This module defines the class SignInPage to test UI pages."""
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    """Define const & methods for testing Login GitHub page"""
    URL = 'https://github.com/login'

    def __init__(self, headless=None, no_sandbox=None) -> None:
        """Initialize parent class & define options
        for Chrome.driver (--headless, --no-sandbox)
        """
        super().__init__(headless, no_sandbox)

    def go_to(self) -> None:
        """Open sign-in page"""
        self.driver.get(SignInPage.URL)

    def try_login(self, username: str, password: str) -> None:
        """Try to login

        Args:
            username: login username
            password: user's password
        """
        # Search the login field by typing Username
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Typing incorrect login
        login_elem.send_keys(username)

        # Search password field
        password_elem = self.driver.find_element(By.ID, "password")

        # Typing an incorrect password
        password_elem.send_keys(password)

        # Search the "Sign-in" button by attr. - name
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Emulation LCM (left click mouse)
        btn_elem.click()

    def check_title(self, expected_title: str) -> bool:
        """Get the content of the title tag &
        compare it with what is expected.
        """
        return self.driver.title == expected_title
