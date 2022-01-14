from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_emptiness(self):
        self.no_items_in_basket()
        self.basket_empty_text()

    def no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), \
            "Items in basket is presented, but should not be"

    def basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
            "Empty text is not presented, but should be"
