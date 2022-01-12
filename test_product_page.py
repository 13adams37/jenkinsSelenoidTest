from .pages.product_page import ProductPage
import pytest

promos = [pytest.param(num, marks=pytest.mark.xfail(reason='bug')) if num == 7 else num for num in range(10)]


@pytest.mark.parametrize('promo_number', promos)
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
    page = ProductPage(browser, link)
    page.open()
    page.ProductCheck()
