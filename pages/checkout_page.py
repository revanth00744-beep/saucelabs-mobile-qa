from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException

from utils.helper import Helper

class CheckoutPage(Helper):
    CHECKOUT_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="CHECKOUT: INFORMATION"]')
    FIRST_NAME = (AppiumBy.ACCESSIBILITY_ID, 'test-First Name')
    LAST_NAME = (AppiumBy.ACCESSIBILITY_ID, 'test-Last Name')
    ZIP_CODE = (AppiumBy.ACCESSIBILITY_ID, 'test-Zip/Postal Code')
    CONTINUE_BTN = (AppiumBy.ACCESSIBILITY_ID, 'test-CONTINUE')
    CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, 'test-CANCEL')
    ERROR_MESSAGE = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"require")]')
    FINISH_BTN = (AppiumBy.ACCESSIBILITY_ID, 'test-FINISH')
    ORDER_TOTAL = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Total:")]')
    SUCCESS_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="THANK YOU FOR YOU ORDER"]')

    def fill_info(self, first_name, last_name, zip_code):
        self.wait_and_type(self.FIRST_NAME, first_name)
        self.wait_and_type(self.LAST_NAME, last_name)
        self.wait_and_type(self.ZIP_CODE, zip_code)

    def continue_checkout(self):
        self.wait_and_click(self.CONTINUE_BTN)

    def scroll_to_finish_and_click(self):
        selector = 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("test-FINISH"))'
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector).click()

    def is_order_confirmed(self):
        try:
            return self.wait_for_element(self.SUCCESS_HEADER).is_displayed()
        except TimeoutException:
            return False

    def get_error_message(self):
        return self.wait_for_element(self.ERROR_MESSAGE).text

    def cancel(self):
        self.wait_and_click(self.CANCEL_BTN)

    def get_order_total(self):
        selector = 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textStartsWith("Total:"))'
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector).text