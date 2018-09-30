from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, webdriver):
        self._webdriver = webdriver

    def wait_for_element_visible(self, locator):
        WebDriverWait(self._webdriver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def set_text(self, locator, user_name):
        element = self._webdriver.find_element(*locator)
        element.send_keys(user_name)
