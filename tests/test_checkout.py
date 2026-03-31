from pages.checkout_page import CheckoutPage
from utils.test_data import user_data
from pages.products_page import ProductsPage

class TestCheckout:

    def test_complete_checkout_successfully(self, driver, skip_login_and_checkout):
        page = CheckoutPage(driver)
        page.fill_info(**user_data)
        page.continue_checkout()
        page.scroll_to_finish_and_click()
        assert page.is_order_confirmed() , "Failed to place order"

    def test_order_total_is_displayed(self, driver, skip_login_and_checkout):
        page = CheckoutPage(driver)
        page.fill_info(**user_data)
        page.continue_checkout()
        total = page.get_order_total()
        assert "Total" in total, f"Order total not displayed. Got: {total}"

    def test_missing_firstname_error(self, driver, skip_login_and_checkout):
        page = CheckoutPage(driver)
        page.fill_info("", user_data['last_name'], user_data['zip_code'])
        page.continue_checkout()
        assert "require" in page.get_error_message(), "Error message not displayed as expected!"

    def test_missing_lastname_error(self, driver, skip_login_and_checkout):
        page = CheckoutPage(driver)
        page.fill_info(user_data['first_name'], "", user_data['zip_code'])
        page.continue_checkout()
        assert "require" in page.get_error_message(), "Error message not displayed as expected!"

    def test_missing_zip_code_error(self, driver, skip_login_and_checkout):
        page = CheckoutPage(driver)
        page.fill_info(user_data['first_name'], user_data['last_name'], "")
        page.continue_checkout()
        assert "require" in page.get_error_message(), "Error message not displayed as expected!"

    def test_cancel_returns_to_products(self, driver, skip_login_and_checkout):
        page = CheckoutPage(driver)
        page.cancel()
        products = ProductsPage(driver)
        assert products.is_products_page_loaded(), "Cancel button failed to return to products page"