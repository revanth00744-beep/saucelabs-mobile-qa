from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException

from utils.helper import Helper

class CartPage(Helper):
    CART_PAGE = (AppiumBy.XPATH,'//android.widget.TextView[@text="YOUR CART"]')
    CART_FIRST_ITEM_NAME = (AppiumBy.XPATH,'((//*[@content-desc="test-Description"])[1]//*)[1]')
    CHECKOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'test-CHECKOUT')
    FIRST_ITEM_REMOVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'test-REMOVE')
    CONTINUE_SHOPPING_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'test-CONTINUE SHOPPING')

    def is_cart_page_loaded(self):
        try:
            return self.wait_for_element(self.CART_PAGE).is_displayed()
        except TimeoutException:
            return False

    def get_item_name(self):
        return self.wait_for_element(self.CART_FIRST_ITEM_NAME).text

    def remove_first_item(self):
        self.wait_and_click(self.FIRST_ITEM_REMOVE_BUTTON)

    def proceed_to_checkout(self):
        self.wait_and_click(self.CHECKOUT_BUTTON)

    def is_cart_empty(self):
        try:
            self.wait_for_element(self.CART_FIRST_ITEM_NAME)
            return False
        except TimeoutException:
            return True

    def click_continue_shopping(self):
        self.wait_and_click(self.CONTINUE_SHOPPING_BUTTON)