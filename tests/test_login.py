import pytest

from test_data.data import INVALID_LOGINS, VALID_USER


@pytest.mark.smoke
def test_valid_login(login_page, inventory_page):
    assert "inventory" in login_page.current_url()
    assert inventory_page.get_title() == "Products"


@pytest.mark.regression
@pytest.mark.parametrize("username, password, expected_error", INVALID_LOGINS)
def test_invalid_login(login_page, username, password, expected_error):
    login_page.login(username, password)
    assert expected_error in login_page.get_error_message()
