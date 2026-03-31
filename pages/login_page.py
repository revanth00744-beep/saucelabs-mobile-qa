from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from utils.helper import Helper


class LoginPage(Helper):
    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN_BTN = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    ERROR_MSG = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Error message"]/android.widget.TextView')

    def login(self, username, password):
        self.wait_and_type(self.USERNAME_FIELD, username)
        self.wait_and_type(self.PASSWORD_FIELD, password)
        self.wait_and_click(self.LOGIN_BTN)

    def is_error_displayed(self):
        try:
            return self.wait_for_element(self.ERROR_MSG).is_displayed()
        except NoSuchElementException:
            return False

    def get_error_message(self):
        return self.wait_for_element(self.ERROR_MSG).text