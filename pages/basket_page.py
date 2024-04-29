from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NOTIFICATION_ANY_PRODUCT_IN_BASKET), \
            "Some product in basket, but should not be"

    def should_be_empty_basket_notification(self):
        assert self.is_element_present(*BasketPageLocators.NOTIFICATION_EMPTY_BASKET), "No empty basket notification"
