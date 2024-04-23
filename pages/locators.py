from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[name = "login_submit"]')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[name = "registration_submit"]')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NOTIFICATION_ADDED_TO_BASKET = (By.XPATH, '//div//strong[text()="{0}"]')
    NOTIFICATION_BASKET_PRICE = (By.XPATH, '//div//strong[text()="{0}"]')
