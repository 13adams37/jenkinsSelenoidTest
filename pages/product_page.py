from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def ProductCheck(self):
        self.AddProductToCart()
        self.solve_quiz_and_get_code()
        self.ProductNameCheck()
        self.ProductPriceCheck()

    def AddProductToCart(self):
        # Добавить товар в корзину
        self.browser.find_element(*ProductPageLocators.PRODUCT_ADDTOCARTBUTTON).click()

    def ProductNameCheck(self):
        # Сравнение названия
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ALERT_NAME).text
        assert product_name == alert_name, "Название товара не соответсвует названию в алерте"

    def ProductPriceCheck(self):
        # Сравнение цены
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        card_price = self.browser.find_element(*ProductPageLocators.PRODUCT_CART_PRICE).text
        alert_price = self.browser.find_element(*ProductPageLocators.PRODUCT_ALERT_PRICE).text
        assert product_price in card_price, "Цена товара не соответсвует цене в корзине!"
        assert product_price == alert_price, "Цена товара не соответсвует цене в алерте (корзине)"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
