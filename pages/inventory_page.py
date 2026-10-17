from pages.base_page import BasePage


class InventoryPage(BasePage):
    """The products page shown after a successful login."""

    TITLE = ".title"
    PRODUCT_CARD = ".inventory_item"
    PRODUCT_NAME = ".inventory_item_name"
    PRODUCT_PRICE = ".inventory_item_price"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    CART_LINK = ".shopping_cart_link"
    CART_BADGE = ".shopping_cart_badge"

    def get_title(self) -> str:
        return self.get_text(self.TITLE)

    def get_product_names(self) -> list[str]:
        return self.page.locator(self.PRODUCT_NAME).all_inner_texts()

    def get_product_prices(self) -> list[float]:
        texts = self.page.locator(self.PRODUCT_PRICE).all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def sort_by(self, option_value: str):
        """option_value is one of: az, za, lohi, hilo"""
        self.page.select_option(self.SORT_DROPDOWN, option_value)

    def search_product(self, name: str):
        """
        This demo site has no search box, so we 'search' by finding the
        product card whose name matches. Returns a locator (or count 0).
        """
        return self.page.locator(self.PRODUCT_CARD).filter(has_text=name)

    def add_to_cart(self, product_name: str):
        card = self.search_product(product_name)
        card.get_by_role("button", name="Add to cart").click()

    def remove_from_cart(self, product_name: str):
        card = self.search_product(product_name)
        card.get_by_role("button", name="Remove").click()

    def get_cart_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        return int(badge.inner_text()) if badge.count() else 0

    def open_cart(self):
        self.page.click(self.CART_LINK)
