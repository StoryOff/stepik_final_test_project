from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_SUMMARY), \
            "Basket summary is not present, but should"

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Basket summary present, but shouldn't"

    def is_message_in_empty_cart_is_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_PARAGRAPH_IN_CONTENT_INNER), \
            "Message in empty cart is not present, but should"

    def is_message_in_empty_cart_is_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PARAGRAPH_IN_CONTENT_INNER), \
            "Message in empty cart is present, but shouldn't"
