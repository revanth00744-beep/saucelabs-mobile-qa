import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.login_page import LoginPage
from utils.test_data import VALID_USER
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
import os

def get_local_options():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automationName = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.no_reset = False
    options.auto_grant_permissions = True
    return options, "http://localhost:4723"

def get_browserstack_options():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.set_capability("platformVersion", "13.0")
    options.set_capability("deviceName", "Google Pixel 7")
    options.set_capability("app", os.environ["BS_APP_URL"])
    options.set_capability("bstack:options", {
        "userName": os.environ["BS_USERNAME"],
        "accessKey": os.environ["BS_ACCESS_KEY"],
        "projectName": "Saucelabs Mobile QA",
        "buildName": "GitHub Actions CI",
        "sessionName": "Appium Test Run",
    })
    bs_url = (
        f"https://{os.environ['BS_USERNAME']}:{os.environ['BS_ACCESS_KEY']}"
        f"@hub-cloud.browserstack.com/wd/hub"
    )
    return options, bs_url

@pytest.fixture(scope="function")
def driver():
    use_bs = os.environ.get("USE_BROWSERSTACK", "false").lower() == "true"
    if use_bs:
        options, url = get_browserstack_options()
    else:
        options, url = get_local_options()

    driver = webdriver.Remote(command_executor=url, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def skip_login(driver):
    LoginPage(driver).login(**VALID_USER)

@pytest.fixture(scope="function")
def skip_login_and_add_item(driver, skip_login):
    product = ProductsPage(driver)
    product.add_first_item_to_cart()
    product.go_to_cart()

@pytest.fixture(scope="function")
def skip_login_and_checkout(driver, skip_login_and_add_item):
    CartPage(driver).proceed_to_checkout()


