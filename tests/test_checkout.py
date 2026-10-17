import pytest

from test_data.data import CHECKOUT_INFO, INVALID_CHECKOUT_INFO, PRODUCTS


def go_to_checkout(inventory_page, cart_page):
    """Helper: add one product and reach the checkout form."""
    inventory_page.add_to_cart(PRODUCTS[0])
    inventory_page.open_cart()
    cart_page.proceed_to_checkout()


@pytest.mark.smoke
def test_complete_checkout_flow(inventory_page, cart_page, checkout_page):
    go_to_checkout(inventory_page, cart_page)
    checkout_page.fill_information(**CHECKOUT_INFO)
    checkout_page.finish_order()
    assert checkout_page.get_confirmation() == "Thank you for your order!"


@pytest.mark.regression
@pytest.mark.parametrize("first, last, postal, expected_error", INVALID_CHECKOUT_INFO)
def test_checkout_requires_all_fields(
    inventory_page, cart_page, checkout_page, first, last, postal, expected_error
):
    go_to_checkout(inventory_page, cart_page)
    checkout_page.fill_information(first, last, postal)
    assert expected_error in checkout_page.get_error_message()


@pytest.mark.regression
def test_order_total_is_shown(inventory_page, cart_page, checkout_page):
    go_to_checkout(inventory_page, cart_page)
    checkout_page.fill_information(**CHECKOUT_INFO)
    assert "Total: $" in checkout_page.get_total_text()
