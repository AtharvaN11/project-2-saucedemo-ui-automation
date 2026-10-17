import pytest

from test_data.data import PRODUCTS


@pytest.mark.smoke
def test_add_single_item_to_cart(inventory_page, cart_page):
    inventory_page.add_to_cart(PRODUCTS[0])
    assert inventory_page.get_cart_count() == 1

    inventory_page.open_cart()
    assert cart_page.get_item_names() == [PRODUCTS[0]]


@pytest.mark.regression
def test_add_multiple_items_to_cart(inventory_page, cart_page):
    for product in PRODUCTS:
        inventory_page.add_to_cart(product)
    assert inventory_page.get_cart_count() == len(PRODUCTS)

    inventory_page.open_cart()
    assert sorted(cart_page.get_item_names()) == sorted(PRODUCTS)


@pytest.mark.regression
def test_remove_item_from_inventory_page(inventory_page):
    inventory_page.add_to_cart(PRODUCTS[0])
    inventory_page.remove_from_cart(PRODUCTS[0])
    assert inventory_page.get_cart_count() == 0


@pytest.mark.regression
def test_remove_item_from_cart_page(inventory_page, cart_page):
    inventory_page.add_to_cart(PRODUCTS[0])
    inventory_page.add_to_cart(PRODUCTS[1])
    inventory_page.open_cart()

    cart_page.remove_item(PRODUCTS[0])
    assert cart_page.get_item_names() == [PRODUCTS[1]]
