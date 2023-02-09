from config.config import config_dict
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# import for setup chrome options
from selenium.webdriver.chrome.options import Options


class BasePage:
    # Set path to chromedriver as per your configuration
    PATH = config_dict['UI']['driver_path']

    def __init__(self, headless=False, no_sandbox=False) -> None:
        self.chrome_options = Options()
        if headless:
            self.chrome_options.add_argument("--headless")
        if no_sandbox:
            self.chrome_options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH),
            options=self.chrome_options,
        )

    def close(self):
        self.driver.close()
