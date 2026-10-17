from pages.base_page import BasePage


class CartPage(BasePage):
    """The shopping cart screen."""

    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    CONTINUE_SHOPPING = "[data-test='continue-shopping']"

    def get_item_names(self) -> list[str]:
        return self.page.locator(self.ITEM_NAME).all_inner_texts()

    def remove_item(self, product_name: str):
        item = self.page.locator(self.CART_ITEM).filter(has_text=product_name)
        item.get_by_role("button", name="Remove").click()

    def proceed_to_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)
