import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode.")
    parser.addoption("--driver_name", action="store", default="chrome",
                     help="Specify the driver to use: chrome or firefox.")

@pytest.fixture(scope='function', autouse=True)
def driver(request):
    driver_name = request.config.getoption("driver_name")
    headless = request.config.getoption("headless")
    driver = None

    if driver_name == "chrome":
        print("\nStarting Chrome browser..")
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif driver_name == "firefox":
        print("\nStarting Firefox browser..")
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    else:
        raise pytest.UsageError("--driver_name should be chrome or firefox")

    yield driver

    if driver is not None:
        print("\nQuitting browser..")
        driver.quit()