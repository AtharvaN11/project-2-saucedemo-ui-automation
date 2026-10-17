"""
conftest.py is a special pytest file. Anything defined here is automatically
available to every test, with no imports needed.

It contains:
  1. a command-line option (--env)
  2. fixtures (reusable setup code)
  3. a hook that takes a screenshot whenever a test fails
"""
import os
from datetime import datetime

import pytest

from config.settings import DEFAULT_ENV, ENVIRONMENTS
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.data import VALID_USER

SCREENSHOT_DIR = "screenshots"


# 1. Command-line option -----------------------------------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default=DEFAULT_ENV,
        choices=list(ENVIRONMENTS),
        help="Which environment to test: prod or staging",
    )


# 2. Fixtures ----------------------------------------------------------------
@pytest.fixture(scope="session")
def app_url(request) -> str:
    """The base URL for the chosen environment."""
    env = request.config.getoption("--env")
    return ENVIRONMENTS[env]["base_url"]


@pytest.fixture
def login_page(page, app_url) -> LoginPage:
    """A LoginPage already opened in the browser. `page` comes from pytest-playwright."""
    return LoginPage(page).open(app_url)


@pytest.fixture
def inventory_page(page, login_page) -> InventoryPage:
    """Logs in with a valid user and hands back the products page."""
    login_page.login(**VALID_USER)
    return InventoryPage(page)


@pytest.fixture
def cart_page(page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page) -> CheckoutPage:
    return CheckoutPage(page)


# 3. Screenshot on failure ----------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = item.name.replace("/", "_").replace("[", "_").replace("]", "")
            path = f"{SCREENSHOT_DIR}/{safe_name}_{stamp}.png"
            page.screenshot(path=path, full_page=True)
            print(f"\nScreenshot saved: {path}")
