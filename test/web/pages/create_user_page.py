from selenium.webdriver.common.by import By

from test.web.pages.base_page import BasePage


class CreateUserPage(BasePage):
    USER_FORM = (By.ID, 'user-form')
    USERNAME_INPUT = (By.ID, 'username-input')
    EMAIL_INPUT = (By.ID, 'email-input')
    BIRTHDATE_INPUT = (By.ID, 'birthdate-input')
    ADDRESS_INPUT = (By.ID, 'address-input')
    USER_FORM_SUBMIT = (By.ID, 'user-form-submit')

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.wait_for_page_ready()

    def wait_for_page_ready(self):
        self.wait_for_element_visible(self.USER_FORM)

    def set_username(self, user_name):
        self.set_text(self.USERNAME_INPUT, user_name)

    def set_email(self, email):
        self.set_text(self.EMAIL_INPUT, email)

    def set_birthdate(self, birthdate):
        self.set_text(self.BIRTHDATE_INPUT, birthdate)

    def set_address(self, address):
        self.set_text(self.ADDRESS_INPUT, address)

    def submit_form(self):
        self._webdriver.find_element(*self.USER_FORM_SUBMIT).click()

    def create_user(self, user):
        self.set_username(user['username'])
        self.set_email(user['email'])
        self.set_birthdate(user['birthdate'])
        self.set_address(user['address'])
        self.submit_form()
