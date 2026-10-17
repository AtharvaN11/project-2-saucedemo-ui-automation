from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """The three checkout screens: your info -> overview -> complete."""

    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    FINISH_BUTTON = "[data-test='finish']"
    ERROR_MESSAGE = "[data-test='error']"
    CONFIRMATION_HEADER = ".complete-header"
    SUMMARY_TOTAL = ".summary_total_label"

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.POSTAL_CODE, postal_code)
        self.page.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.page.click(self.FINISH_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def get_confirmation(self) -> str:
        return self.get_text(self.CONFIRMATION_HEADER)

    def get_total_text(self) -> str:
        return self.get_text(self.SUMMARY_TOTAL)
