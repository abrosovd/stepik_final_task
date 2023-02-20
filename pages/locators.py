from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[name = "login_submit"]')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[name = "registration_submit"]')
