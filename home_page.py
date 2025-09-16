from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    LOGIN_BTN = (By.LINK_TEXT, "Login")
    SIGNUP_BTN = (By.LINK_TEXT, "Sign Up")
    COURSES_MENU = (By.XPATH, "//a[contains(text(), 'Courses')]")
    LIVE_CLASSES_MENU = (By.XPATH, "//a[contains(text(), 'LIVE Classes')]")
    PRACTICE_MENU = (By.XPATH, "//a[contains(text(), 'Practice')]")
    DOBBY_WIDGET = (By.CSS_SELECTOR, "#dobby, .dobby, [data-dobby]")

    def go_to_home(self):
        self.open("")

    def is_login_visible(self):
        return self.is_displayed(self.LOGIN_BTN)

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def is_signup_visible(self):
        return self.is_displayed(self.SIGNUP_BTN)

    def click_signup(self):
        try:
            self.click(self.SIGNUP_BTN)
        except Exception:
            self.open("/register/")

    def has_menu_items(self):
        return (self.is_displayed(self.COURSES_MENU) and
                self.is_displayed(self.LIVE_CLASSES_MENU) and
                self.is_displayed(self.PRACTICE_MENU))

    def is_dobby_present(self):
        return self.is_displayed(self.DOBBY_WIDGET)
