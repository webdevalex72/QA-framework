# modules/ui/page_object/base_page.py
"""This module defines the class BasePage to connect
& set options web-driver."""
from config.config import config_dict
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# import for setup chrome options
from selenium.webdriver.chrome.options import Options


class BasePage:
    """Initialize web-driver with defined options.

    Attributes:
        PATH (str): Set path to the driver from config_dict.
    """
    PATH = config_dict['UI']['driver_path']

    def __init__(self, headless=False, no_sandbox=False) -> None:
        """Init options & web-driver Chrome.

        Args:
            headless (bool): if `True` GUI is off.
            no_sandbox (bool): if `True` it run without the sandbox.
                Usefull to run apps with docker or k8s
                (without will be error).
        """
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
        """Provide a close method for the driver."""
        self.driver.close()
