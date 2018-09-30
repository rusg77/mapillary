from selenium.webdriver.common.by import By

from test.web.pages.base_page import BasePage
from test.web.pages.create_user_page import CreateUserPage


class UserListPage(BasePage):
    USERS_TABLE = (By.ID, 'users_table')
    CREATE_USER_LINK = (By.ID, 'create_user')

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.wait_for_page_ready()

    def click_create_user(self):
        element = self._webdriver.find_element(*self.CREATE_USER_LINK)
        element.click()
        return CreateUserPage(self._webdriver)

    def wait_for_page_ready(self):
        self.wait_for_element_visible(self.USERS_TABLE)

    def get_username(self, index):
        return self._webdriver.find_element_by_id('username-{}'.format(index)).text

    def get_birthdate(self, index):
        return self._webdriver.find_element_by_id('birthdate-{}'.format(index)).text

    def get_email(self, index):
        return self._webdriver.find_element_by_id('email-{}'.format(index)).text

    def get_address(self, index):
        return self._webdriver.find_element_by_id('address-{}'.format(index)).text

    def get_user(self, index):
        return {'username': self.get_username(index),
                'birthdate': self.get_birthdate(index),
                'email': self.get_email(index),
                'address': self.get_address(index)}
