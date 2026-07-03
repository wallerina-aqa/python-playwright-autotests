import allure

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Open Main page")
    def open_main_page(self):
        self.open(self.BASE_URL)
