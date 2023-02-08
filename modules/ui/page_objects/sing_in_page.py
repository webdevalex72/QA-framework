from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self, headless=None, no_sandbox=None) -> None:
        super().__init__(headless, no_sandbox)

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Search login field for typing Username
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Typing incorrect login
        login_elem.send_keys(username)

        # Search password field
        password_elem = self.driver.find_element(By.ID, "password")

        # Typing incorrect password
        password_elem.send_keys(password)

        # Search "Sign-in" button by attr. - name
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Emulation LCM (left click mouse)
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
