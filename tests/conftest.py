from pathlib import Path

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def pytest_configure(config):
    allure_dir = PROJECT_ROOT / "allure-results"
    allure_dir.mkdir(exist_ok=True)
    config.option.allure_report_dir = str(allure_dir)


def pytest_addoption(parser):
    # fmt: off
    parser.addoption("--language", action="store", default="en-gb",
        help="Choose language: ",
        choices=("ar", "ca", "cs", "da", "de", "en-gb", "el",
                 "es", "fi", "fr", "it", "ko", "nl", "pl",
                 "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans")

    )
    # fmt: on


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, request):
    language = request.config.getoption("--language")

    return {
        **browser_context_args,
        "locale": language,
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.fixture()
def main_page(page):
    return MainPage(page)


@pytest.fixture()
def login_page(page):
    return LoginPage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)


@pytest.fixture()
def basket_page(page):
    return BasketPage(page)


@pytest.fixture()
def authorized_user(login_page):
    login_page.open_login_page()
    login_page.register_new_user()
    login_page.should_be_authorized_user()
