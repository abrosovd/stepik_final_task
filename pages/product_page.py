from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Add-to-basket button not found"

    def should_be_added_to_basket_notification(self):
        how, what = ProductPageLocators.NOTIFICATION_ADDED_TO_BASKET
        assert self.is_element_present(how, what.format(self.get_product_name())), "Added-to-basket notification not found"

    def should_be_basket_price_notification(self):
        how, what = ProductPageLocators.NOTIFICATION_BASKET_PRICE
        assert self.is_element_present(how, what.format(self.get_product_price())), "Basket-price notification not found"
