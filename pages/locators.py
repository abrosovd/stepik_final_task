from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[name = "login_submit"]')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[name = "registration_submit"]')
    FIELD_NEW_USER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    FIELD_NEW_USER_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    FIELD_NEW_USER_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NOTIFICATION_ADDED_TO_BASKET = (By.XPATH, '//div//strong[text()="{0}"]')
    NOTIFICATION_BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')


class BasketPageLocators:
    NOTIFICATION_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    NOTIFICATION_ANY_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-title")
