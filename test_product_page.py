import pytest
from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}?promo=offer{no}" if no != "???"
        else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]


@pytest.mark.skip
@pytest.mark.parametrize("link", urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_with_promo()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/", timeout=0)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/", timeout=0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/", timeout=0)
    page.open()
    page.add_to_basket()
    page.should_disappeared()
