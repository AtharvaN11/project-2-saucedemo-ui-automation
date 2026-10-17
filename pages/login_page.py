from pages.base_page import BasePage


class LoginPage(BasePage):
    """Everything you can see or do on the login screen."""

    # Locators: how Playwright finds elements. Kept in ONE place so that if
    # the website changes, we fix it here only.
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def open(self, base_url: str):
        self.page.goto(base_url)
        return self

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
