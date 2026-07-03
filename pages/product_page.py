import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.PRODUCT_NAME = self.PAGE.locator(".product_main h1")
        self.PRODUCT_PRICE = self.PAGE.locator(".product_main .price_color")

        self.ADD_TO_BASKET_BUTTON = self.PAGE.locator(".btn-add-to-basket")

        self.SUCCESS_ALERT = self.PAGE.locator(
            ".alert-success:nth-child(1) .alertinner strong",
        )
        self.PRODUCT_PRICE_IN_SUCCESS_ALERT = self.PAGE.locator(".alert-info strong")

    @allure.step("Open Product page")
    def open_product_page(self, link):
        self.open(link)

    @allure.step("Click Add to basket button")
    def click_add_to_basket_button(self):
        self.ADD_TO_BASKET_BUTTON.click()

    @allure.step("Assert success alert is displayed")
    def assert_success_alert(self):
        expect(self.SUCCESS_ALERT).to_be_visible()

    @allure.step("Assert success alert is not displayed")
    def assert_success_alert_absence(self):
        assert self.is_not_element_present(
            self.SUCCESS_ALERT
        ), "Success alert is displayed, but should not be"

    @allure.step("Check product name in successful message")
    def assert_product_name_matches_original_product_name(self):
        expect(self.SUCCESS_ALERT).to_have_text(self.PRODUCT_NAME.inner_text())

    @allure.step("Check product price in successful alert")
    def assert_product_price_matches_original_product_price(self):
        expect(self.PRODUCT_PRICE_IN_SUCCESS_ALERT).to_have_text(
            self.PRODUCT_PRICE.inner_text()
        )

    def assert_basket_messages(self):
        self.assert_success_alert()
        self.assert_product_name_matches_original_product_name()
        self.assert_product_price_matches_original_product_price()
