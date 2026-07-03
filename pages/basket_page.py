import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.PRODUCTS_IN_BASKET = self.PAGE.locator("#basket_formset")
        self.EMPTY_BASKET_MESSAGE = self.PAGE.locator("#content_inner p")

    @allure.step("Assert basket has no products")
    def assert_basket_has_no_products(self):
        self.is_not_element_present(
            self.PRODUCTS_IN_BASKET
        ), "There should be no products in basket, but it contains some",

    @allure.step("Assert basket has message that it is empty")
    def assert_basket_empty_message(self):
        expect(self.EMPTY_BASKET_MESSAGE).to_be_visible()
