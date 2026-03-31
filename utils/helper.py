from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Helper:
    TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located(locator))

    def wait_and_click(self, locator):
        el = self.wait_for_element(locator)
        el.click()
        return el

    def wait_and_type(self, locator, text):
        el = self.wait_for_element(locator)
        el.clear()
        el.send_keys(text)

    def swipe_up(self):
        size = self.driver.get_window_size()
        self.driver.swipe(
            int(size['width']*0.5),
            int(size['height']*0.8),
            int(size['width']*0.5),
            int(size['height']*0.2),
            800
        )
