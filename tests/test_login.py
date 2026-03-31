from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.test_data import VALID_USER, LOCKED_USER, WRONG_PASSWORD

class TestLogin:
    def test_valid_login(self, driver):
        login = LoginPage(driver)
        login.login(**VALID_USER)
        product_page =ProductsPage(driver)
        assert product_page.is_products_page_loaded(), "The products page did not load successfully"

    def test_missing_username(self, driver):
        login = LoginPage(driver)
        login.login("","secret_sauce")
        assert login.is_error_displayed(), "The error message is not displayed"
        error_text = login.get_error_message()
        assert "Username is required" in error_text, f"Expected error 'Username is required', but got {error_text}"

    def test_missing_password(self, driver):
        login = LoginPage(driver)
        login.login("standard_user","")
        assert login.is_error_displayed(), "The error message is not displayed"
        error_text = login.get_error_message()
        assert "Password is required" in error_text, f"Expected error 'Password is required', but got {error_text}"

    def test_locked_out_user(self, driver):
        login = LoginPage(driver)
        login.login(**LOCKED_USER)
        assert login.is_error_displayed(), "The error message is not displayed"
        error_text = login.get_error_message()
        assert "Sorry, this user has been locked out." in error_text, f"Expected error 'Sorry, this user has been locked out.', but got {error_text}"

    def test_wrong_password(self, driver):
        login = LoginPage(driver)
        login.login(**WRONG_PASSWORD)
        assert login.is_error_displayed(), "The error message is not displayed"
        error_text = login.get_error_message()
        assert "Username and password do not match" in error_text, f"Expected error 'Username and password do not match any user in this service', but got {error_text}"