from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Login') or contains(text(),'Sign in')]")
    ERROR_MSG = (By.CSS_SELECTOR, ".error, .text-danger, .alert-danger")

    def login(self, email: str, password: str):
        self.find(self.EMAIL_INPUT).clear()
        self.find(self.EMAIL_INPUT).send_keys(email)
        self.find(self.PASSWORD_INPUT).clear()
        self.find(self.PASSWORD_INPUT).send_keys(password)
        self.click(self.LOGIN_BTN)

    def is_error_visible(self) -> bool:
        return self.is_displayed(self.ERROR_MSG)
