"""
All test data lives here, away from the test logic.
Tests import these lists and feed them into @pytest.mark.parametrize.
"""

VALID_USER = {"username": "standard_user", "password": "secret_sauce"}

CHECKOUT_INFO = {"first_name": "Asha", "last_name": "Patil", "postal_code": "402107"}

# (username, password, expected error message)
INVALID_LOGINS = [
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
    ("standard_user", "wrong_password", "Username and password do not match"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
]

# (sort option value on the page, how to verify it)
SORT_OPTIONS = ["az", "za", "lohi", "hilo"]

PRODUCTS = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
]

# (first name, last name, postal code, expected error)
INVALID_CHECKOUT_INFO = [
    ("", "Patil", "402107", "First Name is required"),
    ("Asha", "", "402107", "Last Name is required"),
    ("Asha", "Patil", "", "Postal Code is required"),
]
