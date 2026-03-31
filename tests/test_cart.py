import time

from pages.cart_page import CartPage
from pages.products_page import ProductsPage

class TestCart:

    def test_cart_page_loads(self, driver, skip_login_and_add_item):
        page = CartPage(driver)
        assert page.is_cart_page_loaded(), "Cart page failed to load successfully"

    def test_cart_shows_item_added(self, driver, skip_login_and_add_item):
        page = CartPage(driver)
        item_name = page.get_item_name()
        assert item_name is not None, "Item name not found in cart page"

    def test_continue_shopping_returns_to_products(self, driver, skip_login_and_add_item):
        CartPage(driver).click_continue_shopping()
        assert ProductsPage(driver).is_products_page_loaded(), "Failed to return to products page"