from playwright.async_api import Page

class BaseComponent:
    def __init__(self, page: Page) -> None:
        self._page = page

    @property
    def page(self) -> Page:
        return self._page