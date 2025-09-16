import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def _create_chrome(headless: bool):
    opts = ChromeOptions()
    if headless:
        opts.add_argument("--headless=new")
        opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
    return driver

def _create_firefox(headless: bool):
    opts = FirefoxOptions()
    if headless:
        opts.add_argument("-headless")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)
    return driver

@pytest.fixture(scope="session")
def base_url():
    return "https://www.guvi.in"

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser") or "chrome"
    headless = request.config.getoption("--headless")
    if browser.lower() == "chrome":
        driver = _create_chrome(headless)
    elif browser.lower() == "firefox":
        driver = _create_firefox(headless)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    request.addfinalizer(driver.quit)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", default=False, help="run headless")
