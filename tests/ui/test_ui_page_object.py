from modules.ui.page_objects.sing_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # creating Page object
    sign_in_page = SignInPage(headless=True)

    # open page
    sign_in_page.go_to()

    # try login
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # check title page
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # close browser
    sign_in_page.close()
