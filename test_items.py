import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_addToBasketButtonVisible(browser):
    browser.get(link)
    time.sleep(10)
    addToBasketButton = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]').text
    assert addToBasketButton is not None, f"Кнопка 'Добавить в корзину' не найдена. '{addToBasketButton}'"
