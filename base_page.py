from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url: str = None):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, 15)

    def open(self, path: str = ""):
        url = f"{self.base_url}{path}" if self.base_url else path
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def is_displayed(self, locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def get_title(self) -> str:
        return self.driver.title

    def current_url(self) -> str:
        return self.driver.current_url
