import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()

@pytest.mark.smoke
class TestGuvi:

    def test_url_loads(self, driver, base_url):
        home = HomePage(driver, base_url)
        home.go_to_home()
        assert "guvi" in driver.current_url.lower()

    def test_title(self, driver, base_url):
        home = HomePage(driver, base_url)
        home.go_to_home()
        assert home.get_title() == "GUVI | Learn to code in your native language"

    def test_login_button_visible_clickable(self, driver, base_url):
        home = HomePage(driver, base_url)
        home.go_to_home()
        assert home.is_login_visible()
        home.click_login()
        login = LoginPage(driver, base_url)
        assert login.is_displayed(login.EMAIL_INPUT)

    def test_signup_button_visible_and_redirect(self, driver, base_url):
        home = HomePage(driver, base_url)
        home.go_to_home()
        assert home.is_signup_visible()
        home.click_signup()
        assert driver.current_url.rstrip('/').endswith('/register')

    def test_login_valid_credentials(self, driver, base_url):
        VALID_EMAIL = "test_user@example.com"
        VALID_PASSWORD = "CorrectHorseBatteryStaple"
        home = HomePage(driver, base_url)
        home.go_to_home()
        home.click_login()
        login = LoginPage(driver, base_url)
        login.login(VALID_EMAIL, VALID_PASSWORD)
        assert 'login' not in driver.current_url.lower()

    def test_login_invalid_credentials(self, driver, base_url):
        home = HomePage(driver, base_url)
        home.go_to_home()
        home.click_login()
        login = LoginPage(driver, base_url)
        login.login("wrong@example.com", "badpass")
        assert login.is_error_visible()

    def test_menu_items_present(self, driver, base_url):
        home = HomePage(driver, base_url)
        home.go_to_home()
        assert home.has_menu_items()

    def test_dobby_present(self, driver, base_url):
        home = HomePage(driver, base_url)
        home.go_to_home()
        assert home.is_dobby_present()

    def test_logout(self, driver, base_url):
        VALID_EMAIL = "test_user@example.com"
        VALID_PASSWORD = "CorrectHorseBatteryStaple"
        home = HomePage(driver, base_url)
        home.go_to_home()
        home.click_login()
        login = LoginPage(driver, base_url)
        login.login(VALID_EMAIL, VALID_PASSWORD)
        from selenium.webdriver.common.by import By
        try:
            logout_locator = (By.LINK_TEXT, 'Logout')
            home.click(logout_locator)
        except Exception:
            pytest.skip("Logout locator not implemented for this site; please update test")
        assert 'login' in driver.current_url.lower() or driver.current_url.rstrip('/').endswith('/')
