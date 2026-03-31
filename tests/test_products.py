from pages.products_page import ProductsPage

class TestProductsPage:
    def test_products_page_loaded(self, driver, skip_login):
        page = ProductsPage(driver)
        assert page.is_products_page_loaded()

    def test_sort_by_name_a_to_z(self, driver, skip_login):
        page = ProductsPage(driver)
        page.sort_by('az')
        names = page.get_two_product_names()
        assert names[0].lower() <= names[1].lower(), f"Items are not sorted: {names[0]} comes after {names[1]}"

    def test_sort_by_name_z_to_a(self, driver, skip_login):
        page = ProductsPage(driver)
        page.sort_by('za')
        names = page.get_two_product_names()
        assert names[0].lower() >= names[1].lower(), f"Items are not sorted: {names[0]} comes after {names[1]}"

    def test_sort_by_price_low_to_high(self, driver, skip_login):
        page = ProductsPage(driver)
        page.sort_by('lohi')
        prices = page.get_two_product_prices()
        assert prices[0] <= prices[1], f"Items are not sorted: {prices[0]} comes after {prices[1]}"

    def test_sort_by_price_high_to_low(self, driver, skip_login):
        page = ProductsPage(driver)
        page.sort_by('hilo')
        prices = page.get_two_product_prices()
        assert prices[0] >= prices[1], f"Items are not sorted: {prices[0]} comes after {prices[1]}"

    def test_add_to_cart_updates_badge(self, driver, skip_login):
        page = ProductsPage(driver)
        page.add_first_item_to_cart()
        assert page.get_cart_badge_count() != 0, "Cart badge count did not update"

    def test_swipe_scroll_product_list(self, driver, skip_login):
        page = ProductsPage(driver)
        page.swipe_up()
        assert page.is_products_page_loaded(), "Products page crashed or disappeared after swipe/scroll"