import pytest
from utilities.driver_factory import get_driver
from pages.login_page import LoginPage


class TestLogin:

    @pytest.fixture
    def driver(self):
        driver = get_driver()
        yield driver
        driver.quit()

    def test_valid_login(self, driver):

        login = LoginPage(driver)

        login.open_application()

        login.click_sign_in()

        login.enter_email("mohammednabi277@gmail.com")

        login.click_continue()

        login.enter_password("Nabi@0786")

        login.click_login()

        import time

        time.sleep(5)

        print("Current URL:", driver.current_url)
        print("Page Title:", driver.title)