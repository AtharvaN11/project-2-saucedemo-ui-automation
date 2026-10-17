import pytest

from test_data.data import PRODUCTS


@pytest.mark.smoke
def test_six_products_are_shown(inventory_page):
    """Verify that all six products are displayed on the inventory page."""
    product_names = inventory_page.get_product_names()

    assert len(product_names) == 6


@pytest.mark.regression
@pytest.mark.parametrize("product", PRODUCTS)
def test_product_card_exists(inventory_page, product):
    """Verify that each expected product is present in the inventory."""
    product_names = inventory_page.get_product_names()

    assert product in product_names, (
        f"Expected product '{product}' was not found. "
        f"Available products: {product_names}"
    )


@pytest.mark.regression
def test_unknown_product_is_not_displayed(inventory_page):
    """Verify that a product that does not exist is not displayed."""
    product_names = inventory_page.get_product_names()

    assert "Not A Real Product" not in product_names


@pytest.mark.regression
def test_sort_name_a_to_z(inventory_page):
    """Verify that products can be sorted alphabetically."""
    inventory_page.sort_by("az")

    names = inventory_page.get_product_names()

    assert names == sorted(names)


@pytest.mark.regression
def test_sort_name_z_to_a(inventory_page):
    """Verify that products can be sorted in reverse alphabetical order."""
    inventory_page.sort_by("za")

    names = inventory_page.get_product_names()

    assert names == sorted(names, reverse=True)


@pytest.mark.regression
def test_sort_price_low_to_high(inventory_page):
    """Verify that products can be sorted by ascending price."""
    inventory_page.sort_by("lohi")

    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices)


@pytest.mark.regression
def test_sort_price_high_to_low(inventory_page):
    """Verify that products can be sorted by descending price."""
    inventory_page.sort_by("hilo")

    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices, reverse=True)
