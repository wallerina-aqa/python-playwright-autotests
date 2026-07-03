import re

import allure
from faker import Faker
from playwright.sync_api import expect

from pages.base_page import BasePage

faker = Faker()


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.URL_ENDPOINT = "accounts/login/"
        self.URL = self.BASE_URL + self.URL_ENDPOINT

        self.LOGIN_FORM = self.PAGE.locator("#login_form")
        self.REGISTER_FORM = self.PAGE.locator("#register_form")

        self.REGISTRATION_FORM_EMAIL_INPUT = self.PAGE.locator("#id_registration-email")
        self.REGISTRATION_FORM_PASSWORD_INPUT = self.PAGE.locator(
            "#id_registration-password1"
        )
        self.REGISTRATION_FORM_CONFIRM_PASSWORD_INPUT = self.PAGE.locator(
            "#id_registration-password2",
        )
        self.SUBMIT_REGISTRATION_BUTTON = self.PAGE.locator(
            "[name='registration_submit']"
        )
        self.THANKS_FOR_REGISTRATION_ALERT = self.PAGE.locator(".alert-success")

    @allure.step("Open Login page")
    def open_login_page(self):
        self.open(self.URL)

    @allure.step("Assert Login page url")
    def should_be_login_url(self):
        expect(self.PAGE).to_have_url(re.compile(f"{self.URL_ENDPOINT}$"))

    @allure.step("Assert page contains login form")
    def should_be_login_form(self):
        expect(self.LOGIN_FORM).to_be_visible()

    @allure.step("Assert page contains register form")
    def should_be_register_form(self):
        expect(self.REGISTER_FORM).to_be_visible()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step("Register new user")
    def register_new_user(self):
        new_user_email = faker.email()
        new_user_password = faker.password()

        self.REGISTRATION_FORM_EMAIL_INPUT.fill(new_user_email)
        self.REGISTRATION_FORM_PASSWORD_INPUT.fill(new_user_password)
        self.REGISTRATION_FORM_CONFIRM_PASSWORD_INPUT.fill(new_user_password)
        self.SUBMIT_REGISTRATION_BUTTON.click()

        expect(self.THANKS_FOR_REGISTRATION_ALERT).to_be_visible()
