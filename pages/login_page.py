from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.BUTTON_LOGIN), "Login button not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.BUTTON_REGISTRATION), "Registration button not found"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.FIELD_NEW_USER_EMAIL)
        email_field.send_keys(email)
        password1_field = self.browser.find_element(*LoginPageLocators.FIELD_NEW_USER_PASSWORD1)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(*LoginPageLocators.FIELD_NEW_USER_PASSWORD2)
        password2_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        registration_button.click()
