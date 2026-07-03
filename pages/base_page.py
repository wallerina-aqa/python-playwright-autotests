import math

import allure
from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class BasePage:
    def __init__(self, page: Page):
        self.PAGE = page
        self.BASE_URL = "https://selenium1py.pythonanywhere.com/"

        self.LOGIN_LINK = self.PAGE.locator("#login_link")
        self.VIEW_BASKET_LINK = self.PAGE.locator(".basket-mini a")

        self.USER_ICON = self.PAGE.locator(".icon-user")

        self.PRODUCTS_CATALOGUE_URL = "https://selenium1py.pythonanywhere.com/catalogue"

    def open(self, url):
        self.PAGE.goto(url)

    @allure.step("Assert page contains link to Login page")
    def should_be_login_link(self):
        expect(self.LOGIN_LINK).to_be_visible()
        expect(self.LOGIN_LINK).to_be_enabled()

    @allure.step("Click login link")
    def click_login_link(self):
        self.LOGIN_LINK.click()

    @staticmethod
    def is_not_element_present(locator, timeout=5000):
        try:
            locator.wait_for(state="visible", timeout=timeout)
        except PlaywrightTimeoutError:
            return True

        return False

    @allure.step("Click View basket link")
    def click_view_basket_link(self):
        self.VIEW_BASKET_LINK.click()

    @allure.step("Assert user icon is displayed")
    def should_be_authorized_user(self):
        expect(self.USER_ICON).to_be_visible()

    @allure.step("Solve quiz and send code in alert")
    def solve_quiz_and_send_code(self):
        def handle_dialog(dialog):
            number = dialog.message.split("\n", 1)[0].split("=")[1].strip()
            answer = str(math.log(abs(12 * math.sin(float(number)))))
            dialog.accept(answer)

        self.PAGE.once("dialog", handle_dialog)
