from typing import Optional

from playwright.async_api import Page

from src.ui.components.navbar import Navbar


class BasePage:
    def __init__(self, page: Page, navbar: Optional[Navbar] = None) -> None:
        self._page = page
        self._navbar = navbar

    @property
    def page(self) -> Page:
        return self._page
