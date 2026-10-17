from playwright.sync_api import Page


class BasePage:
    """
    Parent class for every page object.

    Holds the Playwright `page` (the browser tab) and small helper methods
    that all pages share, so we don't repeat code.
    """

    def __init__(self, page: Page):
        self.page = page

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def current_url(self) -> str:
        return self.page.url
