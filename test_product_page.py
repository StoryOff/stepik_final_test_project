import pytest
from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}?promo=offer{no}" if no != "???"
        else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]


@pytest.mark.parametrize("link", urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_with_promo()
