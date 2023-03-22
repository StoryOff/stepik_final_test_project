from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group > .btn:nth-child(1)")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_STRONG_TEXT_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner")


class BasketPageLocators:
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_PARAGRAPH_IN_CONTENT_INNER = (By.CSS_SELECTOR, "#content_inner p")
