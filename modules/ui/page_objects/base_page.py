import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# import for setup chrome options
from selenium.webdriver.chrome.options import Options


class BasePage:
    # Set path to chromedriver as per your configuration
    HOMEDIR = os.path.expanduser("~")
    PATH = HOMEDIR + "/chromedriver/stable/"
    DRIVER_NAME = "chromedriver"

    def __init__(self, headless=False, no_sandbox=False) -> None:
        self.chrome_options = Options()
        if headless:
            self.chrome_options.add_argument("--headless")
        if no_sandbox:
            self.chrome_options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME),
            options=self.chrome_options,
        )

    def close(self):
        self.driver.close()
