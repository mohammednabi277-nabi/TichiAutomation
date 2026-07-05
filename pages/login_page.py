from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Locators
    SIGN_IN_BUTTON = (By.XPATH, "//button[normalize-space()='Sign In']")
    EMAIL = (By.ID, "email")
    CONTINUE_BUTTON = (By.XPATH, "//button[normalize-space()='Continue']")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_application(self):
        self.driver.get("https://tichi-app-webapp-stage.web.app")
        self.driver.maximize_window()

    def click_sign_in(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SIGN_IN_BUTTON)
        ).click()

    def enter_email(self, email):
        email_box = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        )
        email_box.clear()
        email_box.send_keys(email)

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def enter_password(self, password):
        password_box = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        password_box.clear()
        password_box.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url