import pytest
from config.config import config_dict


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# import for search Elememts
from selenium.webdriver.common.by import By
# import for setup chrome options
from selenium.webdriver.chrome.options import Options

# import time module for delay after send_keys
# import time


@pytest.mark.ui
def test_check_incorrect_username():
    # Setup chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    # chrome_options.add_argument("--no-sandbox")

    # Set path to chromedriver as per your configuration
    # & Choose Chrome Browser
    driver = webdriver.Chrome(
        service=Service(config_dict['UI']['driver_path']),
        options=chrome_options
    )

    # open web-page https://github.com/login
    driver.get("https://github.com/login")

    # Search login field for typing Username
    login_elem = driver.find_element(By.ID, "login_field")

    # Typing incorrect login
    login_elem.send_keys("sergiibutenko@wrong_email.com")

    # Search password field
    password_elem = driver.find_element(By.ID, "password")

    # Typing incorrect password
    password_elem.send_keys("wrong_password")

    # Search "Sign-in" button by attr. - name
    btn_elem = driver.find_element(By.NAME, "commit")

    # Emulation LCM (left click mouse)
    btn_elem.click()

    # Check title page
    assert driver.title == "Sign in to GitHub · GitHub"
    # time.sleep(3)

    # Close browser
    driver.close()
