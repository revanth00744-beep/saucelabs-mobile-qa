from typing import Literal
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException

from utils.helper import Helper

class ProductsPage(Helper):
    PRODUCTS_SCREEN = (AppiumBy.XPATH,'//android.widget.TextView[@text="PRODUCTS"]')
    SORT_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Modal Selector Button"]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
    SORT_SCREEN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sort items by...")')
    SORT_OPTION_AZ = (AppiumBy.XPATH, '//android.widget.TextView[@text="Name (A to Z)"]')
    SORT_OPTION_ZA = (AppiumBy.XPATH, '//android.widget.TextView[@text="Name (Z to A)"]')
    SORT_OPTION_LOHI = (AppiumBy.XPATH,'//android.widget.TextView[@text="Price (low to high)"]')
    SORT_OPTION_HILO = (AppiumBy.XPATH, '//android.widget.TextView[@text="Price (high to low)"]')
    FIRST_PRODUCT_NAME = (AppiumBy.XPATH, '//(android.view.ViewGroup[@content-desc="test-Item"])[1]//*[@content-desc="test-Item title"]')
    FIRST_PRODUCT_PRICE = (AppiumBy.XPATH, '//(android.view.ViewGroup[@content-desc="test-Item"])[1]//*[@content-desc="test-Price"]')
    SECOND_PRODUCT_NAME = (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-Item"])[2]//*[@content-desc="test-Item title"]')
    SECOND_PRODUCT_PRICE = (AppiumBy.XPATH, '//(android.view.ViewGroup[@content-desc="test-Item"])[2]//*[@content-desc="test-Price"]')
    ADD_TO_CART_BUTTON = (AppiumBy.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[1]')
    CART_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]')
    CART_BADGE = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]//android.widget.TextView')
    OPTIONS = { 'az' : SORT_OPTION_AZ,
                'za' : SORT_OPTION_ZA,
                'lohi' : SORT_OPTION_LOHI,
                'hilo' : SORT_OPTION_HILO,
    }

    def is_products_page_loaded(self):
        try:
            return self.wait_for_element(self.PRODUCTS_SCREEN)
        except ElementNotVisibleException:
            return False

    def get_two_product_names(self):
        first_item_name = self.wait_for_element(self.FIRST_PRODUCT_NAME).text
        second_item_name = self.wait_for_element(self.SECOND_PRODUCT_NAME).text
        names = (first_item_name, second_item_name)
        return names

    def get_two_product_prices(self):
        first_item_price = self.wait_for_element(self.FIRST_PRODUCT_PRICE).text
        second_item_price = self.wait_for_element(self.SECOND_PRODUCT_PRICE).text
        prices = (float(first_item_price.replace("$","")), float(second_item_price.replace("$","")))
        return prices

    def sort_by(self, option:Literal['az','za','lohi','hilo']):
        self.wait_and_click(self.SORT_BUTTON)
        self.wait_and_click(self.OPTIONS[option])

    def add_first_item_to_cart(self):
        self.wait_and_click(self.ADD_TO_CART_BUTTON)

    def get_cart_badge_count(self):
        try:
            return int(self.wait_for_element(self.CART_BADGE).text)
        except ElementNotVisibleException:
            return 0

    def go_to_cart(self):
           self.wait_and_click(self.CART_BUTTON)